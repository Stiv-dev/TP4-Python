import discord
from discord import Client

client = discord.Client()

@client.event
async def on_ready():
    print("Le bot est pret.")

@client.event
async def on_message(message):
    print(message.content)
client.run("OTU5MzQ4MTE2OTA4Mjc3ODIw.Ykakjg.88QgJ_0F2QEWXwGASjSvdcuEbw0")

"""@client.event
async def on_message(message):
    pass

@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("Pong")"""

"""class MyBot(Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        self.log.infolog(f"{self.user} has connected to Discord!")"""