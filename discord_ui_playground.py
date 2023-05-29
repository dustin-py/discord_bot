import discord
from discord.ext import commands
import requests
from requests_html import HTML
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv('DISCORD_TOKEN')

class SimpleView(discord.ui.View):
     
    @discord.ui.button(
            label="Guess What?!",
            style=discord.ButtonStyle.success)
    
    async def hello(
        self, 
        interaction: discord.Interaction, 
        button: discord.ui.Button):
        await interaction.response.send_message(f"{interaction.user.display_name} sucks fat cock!")
    
    @discord.ui.button(
            label="Click to hear a joke.", 
            style=discord.ButtonStyle.blurple)
    
    async def joke(
        self, 
        interaction: discord.Interaction, 
        button: discord.ui.Button):
        request = requests.get(
            "https://icanhazdadjoke.com/", 
            headers={"User-Agent":"https://github.com/dustin-py/discord_bot",
                     "Content-Type":"text/plain"})
        response = request.content
        html_doc = HTML(html=response)
        joke_text = html_doc.find('p', first=True).text
        await interaction.response.send_message(joke_text)
         


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