import discord
import discord_bot.responses as responses
import time


intents = discord.Intents.default()
intents.message_content = True

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    
    except Exception as e:
        return 0 

async def send_mean_message(message, user, is_private):
    try:
        response = responses.mean_response(user)
        await message.author.send(response) if is_private else await message.channel.send(response)
    
    except Exception as e:
        return 0 


def run_discord_bot():
    TOKEN = 'MTExMDU1NjQyNTI0MDk4NTY1MA.GRhXf7.xcOQxRe9EsQWij8x5ct9-DvijLKXOfTS77rGZE'
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        poo_list = ["HyTec#0079","JOJO#1135","dustin-py#6813","Donald “Trenbolone” Trump#5607"]

        if str(message.author) in poo_list:
           #add if to check for nick name
           user = message.author.nick
           no_nick = message.author
           time.sleep(2)
           await message.delete()
           if user == None:
                await send_mean_message(message, no_nick, is_private=False)
           else:
                await send_mean_message(message, user, is_private=False)
             
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)