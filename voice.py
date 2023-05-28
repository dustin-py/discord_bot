import discord
from discord.ext import commands
import time
import asyncio

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')


@bot.event
async def on_voice_state_update(member, before, after):

    before_channels = ["None","gumping it","the real goop","good morning kanye"]
    after_channels = ["None","goop chat","gumping it","the real goop"]
    
    if str(before.channel) in before_channels and str(after.channel) in after_channels:
        await asyncio.sleep(2)  # Delay for 5 seconds

        # Check if the member is still in the same voice channel after the delay
        if str(member.name) in ["dustin-py","Donald “Trenbolone” Trump"]:

            if member.voice and member.voice.channel == after.channel:
                target_channel_id = 953273790106861658 
                target_channel = bot.get_channel(target_channel_id)

                if target_channel:
                    await member.move_to(target_channel)
                    print(f"Moved {member.display_name} to {target_channel.name}.")

        else:
            print(f"{member.display_name} has joined voice chat.")


bot.run("MTExMDU1NjQyNTI0MDk4NTY1MA.GRhXf7.xcOQxRe9EsQWij8x5ct9-DvijLKXOfTS77rGZE")