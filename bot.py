import os

import discord
from redisdb import get
from random import choice

BOT_TOKEN = os.getenv('TOKEN', "Token Doesn't Exist!")
POSITIONS = ['top', 'jungle', 'mid', 'adc', 'support']
bot = discord.Bot()

# we need to limit the guilds for testing purposes
# so other users wouldn't see the command that we're testing

@bot.command(description="Generate a random league team composition") # this decorator makes a slash command
async def randomcomp(ctx): # a slash command will be created with the name "ping"
    champions = dict()
    while not champions or len(set([values[0] for _, values in champions.items()])) != 5:
        for pos in POSITIONS:
            champions[pos] = choice(get(pos))
    
    res = ""
    res += f"Top: {champions['top'][0]} {champions['top'][1]}\n"
    res += f"Jungle: {champions['jungle'][0]} {champions['jungle'][1]}\n"
    res += f"Mid: {champions['mid'][0]} {champions['mid'][1]}\n"
    res += f"Bot: {champions['adc'][0]} {champions['adc'][1]}\n"
    res += f"Support: {champions['support'][0]} {champions['support'][1]}\n"

    await ctx.respond(res)

bot.run(BOT_TOKEN)