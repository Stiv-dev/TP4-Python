import os

import discord
from dotenv import load_dotenv
#from discord.ext import commands

load_dotenv(dotenv_path="config")


client = discord.Client()
"""
@client.event
async def on_ready():
    print("Le bot est pret.")
"""


client.run(os.getenv("TOKEN"))