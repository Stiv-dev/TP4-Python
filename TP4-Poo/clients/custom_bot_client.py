import discord
from discord.ext import commands

class CustomClient(commands.Bot):
    async def on_ready(self):
        print(f'{self.user} bot user is ready to rumble!')

 

