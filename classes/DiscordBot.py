import asyncio
import time
from threading import Thread

import discord

TOKEN = "Nzc4MzM3NTA1NjY1NDgyODIy.X7QhSg.9ac1cs01XuysMMEPwYfdwo2tKw0"


class DiscordHost(discord.Client):
    async def on_ready(self):
        pass

    async def on_message(self, message):
        if message.author == self.user:
            return

        await message.channel.send('Hello!')


class DiscordBot(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.loop = asyncio.get_event_loop()
        self.setDaemon(True)
        self.start()

    async def starter(self):
        self.discord_client = DiscordHost()
        await self.discord_client.start(TOKEN)

    def run(self):
        current_milli_time = lambda: int(round(time.time() * 1000))

        self.name = str(current_milli_time())

        self.loop.create_task(self.starter())
        self.loop.run_forever()
