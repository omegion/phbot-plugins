from classes.Logger import Logger


class Character(object):
    def __init__(self):
        self.sp = 0
        self.server = ''
        self.hp_max = 0
        self.current_exp = 0
        self.level = 0
        self.x = 0.0
        self.dead = False
        self.account_id = 0
        self.locale = 22
        self.job_max_exp = 0
        self.job_current_exp = 0
        self.job_name = ''
        self.player_id = 0
        self.model = 0
        self.mp = 0
        self.gold = 0
        self.guild = ''
        self.name = ''
        self.y = 0.0
        self.hp = 0
        self.mp_max = 0
        self.max_exp = 0
        self.region = 23431
        self.log = Logger().log

    def is_joined(self):
        return self.name != ""

    def set(self, info):
        for key, value in info.items():
            setattr(self, key, value)

        return self
