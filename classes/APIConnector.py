import json
import urllib
import urllib.request

from classes.PhBot import PhBot
from classes.plugins.online_manager.tasks import tasks

API_ENDPOINT = "http://127.0.0.1:8000"


# API_ENDPOINT = "https://sro-manager.omegion.icu"


class APIConnector(object):
    def __init__(self, bot: PhBot, token):
        self.endpoint = API_ENDPOINT
        self.token = token
        self.bot = bot
        self.headers = {
            'content-type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
        }

    def dispatch_event(self, event_name, character_info):
        if self.token is None:
            self.bot.log('No token set.')
            return

        url = "{}/events/".format(
            self.endpoint,
        )

        data = {
            'name': event_name,
            'data': character_info
        }

        data = json.dumps(data).encode('utf8')
        req = urllib.request.Request(url, data=data, headers=self.headers)
        try:
            urllib.request.urlopen(req)
            self.bot.log('Event sent.')
        except Exception as err:
            self.bot.log_to_file(err)
            self.bot.log('Event send failed.')

    def execute_queued_tasks(self):
        url = "{}/tasks/?status=PENDING".format(
            self.endpoint,
        )

        req = urllib.request.Request(url, headers=self.headers)

        try:
            res = urllib.request.urlopen(req)
        except Exception as err:
            self.bot.log_to_file(err)
            self.bot.log('Getting task queue failed.')
            return

        received_tasks = json.loads(res.read().decode(res.info().get_param('charset') or 'utf-8'))
        for task in received_tasks:
            task_func = tasks.get(task['name'], None)
            if task_func:
                task_instance = task_func(
                    api=self,
                    task_id=task['id'],
                    data=task['data'],
                )

                try:
                    task_instance.execute()
                except Exception as err:
                    self.bot.exception(err)

                self.mark_done_queued_task(task['id'])

    def mark_done_queued_task(self, task_id):
        url = "{}/tasks/{}/".format(
            self.endpoint,
            task_id,
        )

        data = {
            "status": "DONE"
        }
        data = json.dumps(data).encode('utf8')
        req = urllib.request.Request(url, method="PATCH", data=data, headers=self.headers)
        try:
            urllib.request.urlopen(req)
        except Exception as err:
            self.bot.log_to_file(err)
            self.bot.log('Task marking failed.')
