import discord 

class logins(discord.ext.commands.Cog, name = 'journalisation'):
    def __init__(self, bot):
        self.bot = bot
    """
    @discord.ext.commands.Cog.listener(name='on_command')
    async def print(self,ctx):
        server = ctx.guild.name
        user = ctx.author
        command = ctx.command

        print(f'{server}>{user}>{command}')
    """
    # première fonction qui permet d'afficher seulement les commandes du bot et dans le terminal pas dans un fichier txt
    
    @discord.ext.commands.Cog.listener(name='on_message')
    async def print(self, ctx):
        server= ctx.guild.name
        user = ctx.author
        content = ctx.content
        with open("logs.txt","a") as text_file:
            print(f'{server}>{user}>{content}',file=text_file)

    # fonction final qui affiche l'historique de tout ce qui est tappé et est affiché dans le logs.txt