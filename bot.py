import os

import discord
from redisdb import get
from random import choice

BOT_TOKEN = os.getenv('TOKEN', "Token Doesn't Exist!")
POSITIONS = ['top', 'jungle', 'mid', 'adc', 'support']
bot = discord.Bot()

# reroll button view
class RerollButtonView(discord.ui.View):
    @discord.ui.button(label="Reroll", style=discord.ButtonStyle.secondary, emoji="🔄") # Create a button with the label "reroll"
    async def button_callback(self, button, interaction):
        await interaction.response.edit_message(content=rollComp()) # Send a message when the button is clicked

def rollComp():
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

    return res

@bot.command(description="Generate a random league team composition") # this decorator makes a slash command
async def randomcomp(ctx): # a slash command will be created with the name "randomcomp"
    await ctx.respond(rollComp(), view=RerollButtonView())

bot.run(BOT_TOKEN)