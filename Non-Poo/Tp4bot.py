import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot1 = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print("Le bot est pret")

@bot.command(name='del')
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    for each_message in messages:
        await each_message.delete()
""""
@bot.command(name='ping')
async def on_message(ctx):
    if ctx.content.lower() == "ping":
        await ctx.channel.send("pong")
"""
"""
@bot1.ext.command(name='yolo')
async def ping(self,ctx):
    await ctx.send(f"pong")
"""

@bot1.command(name='dele')
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    for each_message in messages:
        await each_message.delete()
"""
 @discord.ext.commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'A wild {member.mention} has appeared!')
"""
bot.run("OTU5MzQ4MTE2OTA4Mjc3ODIw.Ykakjg.GUp3hut-CTwP5-iP6XMU_DDvWY0")