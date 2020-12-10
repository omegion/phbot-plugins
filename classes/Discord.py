import json
import urllib
import urllib.request

WEBHOOK_URL = "https://discord.com/api/webhooks/778332828944433203/YITfHi5SIiWTHxeuAgcDJW6_ufwidPnJJ2EoMmILtlJq8ZsnMaZcSQ_hp8tBycrERTsU"


class Discord(object):
    def __init__(self):
        self.webhook = WEBHOOK_URL
        self.data = None

    def message(self, title, text):
        self.data = {
            "username": "SuperParty",
            "embeds": [{
                "title": str(title),
                "description": str(text),
            }]
        }

        return self

    def send(self):
        if not self.data:
            raise Exception("Discord data is empty.")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            "Content-Type": "application/json",
        }

        data = json.dumps(self.data).encode()
        req = urllib.request.Request(self.webhook, data=data, headers=headers)
        try:
            urllib.request.urlopen(req)
        except Exception:
            raise Exception('Discord message could not send.')


class DiscordMessage(object):
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def send(self):
        discord = Discord()
        return discord.message(self.title, self.text).send()
