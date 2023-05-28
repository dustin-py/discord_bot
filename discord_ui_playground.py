import discord
from discord.ext import commands
import requests

TOKEN = 'MTExMDU1NjQyNTI0MDk4NTY1MA.GRhXf7.xcOQxRe9EsQWij8x5ct9-DvijLKXOfTS77rGZE'


class SimpleView(discord.ui.View):
     
    @discord.ui.button(label="Guess What?!",style=discord.ButtonStyle.success)
    async def hello(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"{interaction.user.display_name} sucks fat cock!")
    
    @discord.ui.button(label="Click to hear a joke.", style=discord.ButtonStyle.blurple)
    async def joke(self, interaction: discord.Interaction, button: discord.ui.Button):
        r = requests.get("https://random-ize.com/bad-jokes/bad-jokes-f.php")
        
        await interaction.response.send_message(f"Testing joke generator: {r.content}")
         


def run ():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name} ({bot.user.id})')

    @bot.command(name="button")
    async def button(ctx):
        view = SimpleView()
        await ctx.send(view=view)

    bot.run(TOKEN)

if __name__ == "__main__":
    run()