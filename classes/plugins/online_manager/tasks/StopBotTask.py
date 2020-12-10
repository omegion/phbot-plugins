from classes.plugins.online_manager.tasks.BaseTask import BaseTask


class StopBotTask(BaseTask):
    name = "stop_bot"

    def execute(self):
        self.api.bot.stop()
