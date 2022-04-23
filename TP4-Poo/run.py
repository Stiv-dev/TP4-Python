import discord
from clients.custom_bot_client import CustomClient
from cogs.greetings import Greetings
from cogs.command_err_handler import CommandErrHandler
from cogs.loggings import logins

def main():
    token = "TOKEN"


    intents = discord.Intents.default()
    intents.members = True

    bot = CustomClient(
        command_prefix='$', 
        intents=intents
    )

    bot.add_cog(Greetings(bot))
    bot.add_cog(CommandErrHandler(bot))
    bot.add_cog(logins(bot))

    bot.run(token)


if __name__ == '__main__':
    main()