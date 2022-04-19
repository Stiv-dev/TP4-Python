import discord
from discord import Client

#pr config le token
from dotenv import load_dotenv
load_dotenv(dotenv_path="config")
import os

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)


"client = discord.Client()"

@client.event
async def on_ready():
    print("Le bot est pret.")

@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(959382781996187700)
    await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")

@client.event
async def on_member_remove(member):
    general_channel: discord.TextChannel = client.get_channel(959382781996187700)
    await general_channel.send(content=f"Va te faire {member.display_name} !")

@client.event 
async def on_message(message):
    if message.content.startswith("!je_suis_venere"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number +1).flatten()

        for each_message in messages:
            await each_message.delete()
            

"""
@client.event
async def on_message(message):
    print(message.content)"""


@client.event
async def on_message(message):
    if message.content.lower() == "ping":
        await message.channel.send("pong")
        #await message.channel.send("pong", delete_after=5)

client.run(os.getenv("TOKEN"))



"""@client.event
async def on_message(message):
    pass
"""
"""
@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("Pong")
"""
"""class MyBot(Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        self.log.infolog(f"{self.user} has connected to Discord!")"""