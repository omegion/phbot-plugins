class BaseTask(object):
    def __init__(self, api: 'APIConnector', task_id, data):
        self.api = api
        self.task_id = task_id
        self.data = data
