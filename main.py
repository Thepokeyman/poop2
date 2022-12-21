import discord
from discord.ext import commands
import os

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents, help_command=None)

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot


@bot.event
async def on_ready():
    await bot.add_cog(music_cog(bot))
    await bot.add_cog(help_cog(bot))


#bot.add_cog(help_cog(bot))
#bot.add_cog(music_cog(bot))

#start the bot with our token
bot.run("MTA1NDYwODk3MTkyODk2MTExNQ.GxFiOw.eCbaB8D2VCq5Ihbd1dSleEhG3Bed80-A7cxGzQ")
