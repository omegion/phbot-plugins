import json

from classes import VERSION
from classes.plugins.BasePlugin import BasePlugin


class ForceTools(BasePlugin):
    def __init__(self, gui=None):
        """This is a helper for force chars."""

        super().__init__(
            plugin_name=self.__class__.__name__,
        )

        self.gui = gui

        self.active_skill_edit = None
        self.party_member_hp_edit = 50

    def save(self):
        self.initialize()

        active_skill = self.bot.qt.text(self.gui, self.active_skill_edit)
        party_member_hp = self.bot.qt.text(self.gui, self.party_member_hp_edit)
        self.config.set('active_skill', active_skill)
        self.config.set('party_member_hp', party_member_hp)

        with open(self.bot.get_config_path(), 'r') as f:
            configs = json.load(f)

        members = self.bot.get_party()
        if members:
            configs['Conditions'] = []
            configs['Skills']['Party Buffs']['Magical Buff'] = []
            configs['Skills']['Party Buffs']['Physical Buff'] = []
            for key in members.keys():
                member_name = members[key]['name']

                if member_name == self.char.name:
                    continue

                # Set conditions
                configs['Conditions'].append({
                    "Enabled": True,
                    "if": [
                        {
                            "if": 62,
                            "op": 4,
                            "value_1": member_name,
                            "value_2": str(party_member_hp)
                        },
                        {
                            "if": 0,
                            "op": 2,
                            "value_1": member_name,
                            "value_2": ""
                        },
                        {
                            "if": 11,
                            "op": 2,
                            "value_1": "",
                            "value_2": ""
                        },
                        {
                            "if": 12,
                            "op": 2,
                            "value_1": "",
                            "value_2": ""
                        }
                    ],
                    "then": [
                        {
                            "then": 60,
                            "value": active_skill,
                            "value_2": member_name
                        }
                    ]
                })

                # Set Party buffs
                configs['Skills']['Party Buffs']['Magical Buff'].append(member_name)
                configs['Skills']['Party Buffs']['Physical Buff'].append(member_name)

        with open(self.bot.get_config_path(), "w") as f:
            f.write(json.dumps(configs, indent=4, sort_keys=True))

        self.bot.reload_config()

    def setup(self):
        self.initialize()

        active_skill = self.config.get('active_skill')
        party_member_hp = self.config.get('party_member_hp')

        self.bot.qt.createLabel(self.gui, self.__init__.__doc__, 10, 10)
        self.bot.qt.createLabel(self.gui, VERSION, 680, 270)
        self.active_skill_edit = self.bot.qt.createLineEdit(self.gui, str(active_skill), 6, 25, 180, 19)
        self.party_member_hp_edit = self.bot.qt.createLineEdit(self.gui, str(party_member_hp), 6, 55, 50, 19)
        self.bot.qt.createButton(self.gui, 'save', 'save', 95, 250)
