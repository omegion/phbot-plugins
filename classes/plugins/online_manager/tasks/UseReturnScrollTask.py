from classes.plugins.online_manager.tasks.BaseTask import BaseTask


class UseReturnScrollTask(BaseTask):
    name = "use_return_scroll"

    def execute(self):
        self.api.bot.use_return_scroll()
