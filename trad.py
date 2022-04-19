import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")
@bot.event
async def on_ready():
    print("Your Bot is Ready !")
@bot.command()
async def dire(ctx, *message):
    await ctx.send(" ".join(message))
@bot.command()
async def traduire_chinese(ctx, *text):
    Caractere_chinois = "????????????????Q????V??Y?"
Texte_chinois = []
for word in text:
    for char in word:
        if char.isalpha():
            index = ord(char) - ord("a")
            transformed = Caractere_chinois[index]
            Texte_chinois.append(transformed)
        else:
            Texte_chinois.append(char)
            Texte_chinois.append(" ")
        await ctx.send("".join(Texte_chinois))

bot.run("OTU5MzQ4MTE2OTA4Mjc3ODIw.Ykakjg._VcQOnmllsZA56YwZHp5HeaPoj0")