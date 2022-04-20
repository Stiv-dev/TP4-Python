import discord
from discord.ext import commands

class Greetings(discord.ext.commands.Cog, name='Greetings module'):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="hey")
    async def adhoc_play(self, ctx):
        await ctx.send(f'Hey {ctx.author.name}')

    @discord.ext.commands.command(name="delete")
    async def on_message(self,ctx,number_of_message:int):
            messages = await ctx.channel.history(limit=number_of_message+1).flatten()
            
            for each_message in messages:
                await each_message.delete() 
        
    @discord.ext.commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'A wild {member.mention} has appeared!')

