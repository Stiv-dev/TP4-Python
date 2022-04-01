import discord
from discord import Client

client = discord.Client()
client.run("OTU5MzQ4MTE2OTA4Mjc3ODIw.Ykakjg.apXORzqsql1PR-Qm1wp-3CtjuE4")

class MyBot(Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        self.log.infolog(f"{self.user} has connected to Discord!")