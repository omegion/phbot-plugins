from classes.plugins.BasePlugin import BasePlugin, exception_handler
from classes.trade.JobPouch import JobPouch


class AutoTrade(BasePlugin):
    def __init__(self, gui=None):
        """This is a plugin for stuff"""

        super().__init__(
            plugin_name=self.__class__.__name__,
        )

        self.gui = gui

        self.pouch = None
        self.cursor = None

    @exception_handler
    def start_trade(self):
        self.bot.log('Trade is started.')

        self.bot.stop()
        self.bot.set_profile('Trade')

        self.cursor = self.bot.db.cursor()
        self.cursor = self._update_pickfilter_take_pots(self.cursor, action='take')
        self._update_townfilter_buy_pots(self.cursor, action='buy')
        self.bot.db.commit()
        self.cursor.close()

        self.bot.use_return_scroll()
        self.bot.start(delay=20)

    @exception_handler
    def stop_trade(self):
        self.bot.log('Trade is finished.')

        self.initialize()
        self.bot.stop()
        self.bot.set_profile(self.char.name)

        self.cursor = self.bot.db.cursor()
        self.cursor = self._update_pickfilter_take_pots(self.cursor, action='donttake')
        self._update_townfilter_buy_pots(self.cursor, action='dontbuy')
        self.bot.db.commit()
        self.cursor.close()

        self.bot.use_return_scroll()
        self.bot.start(delay=20)

    @exception_handler
    def check_pouch(self):
        self.initialize()

        self.pouch = JobPouch(pouch=self.bot.get_job_pouch())

        self.bot.log("Job pouch capacity {}/{}".format(
            self.pouch.get_items_count(),
            self.pouch.total_items_count(),
        ))

    @exception_handler
    def event_loop(self):
        return
        self.run_thread(self.check_pouch, delay=2)

    @exception_handler
    def setup(self):
        self.initialize()

        self.bot.qt.createButton(self.gui, 'start_trade', 'Start Trade', 10, 250)
        self.bot.qt.createButton(self.gui, 'stop_trade', 'Stop Trade', 95, 250)
        self.bot.qt.createButton(self.gui, 'check_pouch', 'Check Job Pouch', 195, 250)

        self.bot.log('loaded')

    def _update_pickfilter_take_pots(self, cursor, action='take'):
        sql = '''UPDATE pickfilter
                    SET store = ?,
                        takestorage = ?
                    WHERE name = ?'''

        if action == 'take':
            cursor.execute(sql, (0, 1, 'Recovery kit (x-large)'))
            cursor.execute(sql, (0, 1, 'Anormal state recovery potion (medium)'))
        elif action == 'donttake':
            cursor.execute(sql, (1, 0, 'Recovery kit (x-large)'))
            cursor.execute(sql, (1, 0, 'Anormal state recovery potion (medium)'))

        return cursor

    def _update_townfilter_buy_pots(self, cursor, action='buy'):
        sql = '''UPDATE town
                    SET enabled = ?,
                        quantity = ?
                    WHERE item_name = ?'''

        if action == 'buy':
            cursor.execute(sql, (1, 700, 'Recovery kit (x-large)'))
            cursor.execute(sql, (1, 200, 'Anormal state recovery potion (medium)'))
        elif action == 'dontbuy':
            cursor.execute(sql, (1, 20, 'Recovery kit (x-large)'))
            cursor.execute(sql, (0, 0, 'Anormal state recovery potion (medium)'))

        return cursor
