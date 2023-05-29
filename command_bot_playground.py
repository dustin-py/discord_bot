import discord
import random
import json
import asyncio
import openai
import requests
from os import getenv
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Declare intents with 
intents = discord.Intents.default()
intents.message_content = True # This allows the client/bot to read message content.


# Clreate a bot to handle command events:
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

# Token to log the bot into discord.
TOKEN = getenv("DISCORD_TOKEN")

openai.organization = "org-wVPDySoWpfji41ZecNs6aEyZ"
openai.api_key = getenv("OPENAPI_TOKEN")


# LOGING THE BOT INTO DISCORD:
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')


# HELP COMMAND
@bot.command()
async def help(ctx, *args):
    await ctx.send("""
    Hello here are the commands available right now for your punk ass:
    
    `!poop` - provide 2 arguments to do poop stuff.
    
    `!math` - command to do simple addition, division, multiplication, and subtraction.
            ex: (1 / 3  or 5 * 5)
    
    `!context` - this command will print the message contexts.
    
    `!upper_converter` - this command will send a message with your text in all caps.
    
    `!slap` - Use this command to slap a random guild member and provide a reason. ex: (!slap because i want to)""")


# HANDLING ARGUMENTS:
@bot.command(name="poop")
async def test(ctx, arg1, arg2):  # arg is like positional arguments so there can be multiple arg1 arg2 etc...
    await ctx.send(int(arg1) + int(arg2))

@bot.command(name="math")
async def math_function(ctx, *args):  # This example is a simple math bot using *args for an unknown amount of arguments.
    # can alse do: async def test(ctx, *, arg) this will treat all after first arg as one arg.

    arguments = ''.join(args)
    math_input = arguments.strip()
    
    if "*" in math_input:
        split_numbers = math_input.split("*")
        await ctx.send(f"{int(split_numbers[0]) * int(split_numbers[1])}")
    
    elif "/" in math_input:
        split_numbers = math_input.split("/")
        await ctx.send(f"{int(split_numbers[0]) / int(split_numbers[1])}")
    
    elif "+" in math_input:
        split_numbers = math_input.split("+")
        await ctx.send(f"{int(split_numbers[0]) + int(split_numbers[1])}")
    
    elif "-" in math_input:
        split_numbers = math_input.split("-")
        await ctx.send(f"{int(split_numbers[0]) - int(split_numbers[1])}")
    
    else:
        await ctx.send("Can not compute.")


# INVOCATION CONTEXT:
@bot.command(name="context")
async def context_checker(ctx, *args): # ctx is the context
    await ctx.send(f"Guild: {ctx.guild}")
    await ctx.send(f"Message: {ctx.message}")
    await ctx.send(f"Author: {ctx.author}")
    await ctx.send(args)


# BASIC CONVERTERS:
# - int conversion could also use str.
@bot.command(name="int_converter")
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

# - Apply a custom function to convert arguments:    
def to_upper(argument):
    return argument.upper()

@bot.command(name="upper_converter")
async def up(ctx, *, content: to_upper):
    await ctx.send(content)


# ADVANCED CONVERTERS:
class Slapper(commands.Converter): # Use a class for conversions
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return f"<@{ctx.message.author.id}> slapped <@{to_slap.id}> because *{argument}*" # the <@ user id > will mention someone in chat.

@bot.command()
async def slap(ctx, *,reason: Slapper):
    await ctx.message.delete()
    await ctx.send(reason)

# CHATGPT BOT
@bot.command(name="chat")
async def chat_gpt(ctx, *args):

    arguments = ' '.join(args)
    bearer = f"Bearer {openai.api_key}"

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type":"application/json",
        "Authorization":bearer
    }
    
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": arguments}],
        "temperature": 0.7
    }

    request = requests.post(url,headers=headers,json=payload)

    bot_response = request.json()["choices"][0]["message"]["content"]

    chunk_1 = bot_response[:1998]
    chunk_2 = bot_response[1999:3996]
    chunk_3 = bot_response[3996:5994]
    chunk_4 = bot_response[5994:7992]

    if chunk_1:
        await ctx.send(chunk_1)
        await asyncio.sleep(2)
    if chunk_2:
        await ctx.send(chunk_2)
        await asyncio.sleep(2)
    if chunk_3:
        await ctx.send(chunk_3)
        await asyncio.sleep(2)
    if chunk_4:
        await ctx.send(chunk_4)
    



bot.run(TOKEN)