import discord
from clients.custom_bot_client import CustomClient
from cogs.greetings import Greetings

def main():
    token = "OTU5MzQ4MTE2OTA4Mjc3ODIw.Ykakjg.bdojbiTrPRxO22Vvazbkp1xqpi4"


    intents = discord.Intents.default()
    intents.members = True

    bot = CustomClient(
        command_prefix='$', 
        intents=intents
    )

    bot.add_cog(Greetings(bot))

    bot.run(token)


if __name__ == '__main__':
    main()