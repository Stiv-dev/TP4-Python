import discord
import sys
import traceback
#from discord.ext import commands


class CommandErrHandler(discord.ext.commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """
        if isinstance(error, discord.ext.commands.CommandNotFound):
            await ctx.send('Je ne connais pas la commande?!')
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

# la classe qui affiche quand la commande n'existe pas