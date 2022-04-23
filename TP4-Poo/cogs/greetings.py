import discord


class Greetings(discord.ext.commands.Cog, name='Greetings module'):
    def __init__(self, bot):
        self.bot = bot

    #fonction qui répond hey
    @discord.ext.commands.command(name="hey")
    async def addhoc_play(self, ctx):
        await ctx.send(f'Hey {ctx.author.name}')

    # oublié pas mettre des _ et pas d'espaces
    @discord.ext.commands.command(name="Puis_je_avoir_20")
    async def addhoc_ple(self, ctx):
        #await ctx.send(f'Oui, Eduardo c est une salope {ctx.author.name}')
        await ctx.send(f'Oui_Steeve_tu_peux_avoir_20 {ctx.author.name}')

    #fonction permettant de supprimer des messages sur le serveur discord
    @discord.ext.commands.command(name="delete")
    async def on_message(self,ctx,number_of_message:int):
            messages = await ctx.channel.history(limit=number_of_message+1).flatten()
            
            for each_message in messages:
                await each_message.delete() 

    # fct de test
    @discord.ext.commands.command(name="yolo")
    async def addhoc_pla(self, ctx):
        await ctx.send(f'Yolo is the word of {ctx.author.name}')
        
    # fonction qui permet d'envoyer un message de bienvenue
    @discord.ext.commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Un mec chelou {member.mention} est apparu!')

    # fonction qui permet d'envoyer un message d'adieu
    """
    @discord.ext.commands.Cog.listener()
    async def on_member_remove(self, member):
        channel1 = member.guild.system_channel
        if channel1 is None:
            await channel1.send(f'A fils de Molière {member.mention} has disparu!')
    """


