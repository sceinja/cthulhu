import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import os

#loads token from .env file
load_dotenv()
token = os.getenv('TOKEN')

#bot status
activity = discord.Activity(type=discord.ActivityType.listening, name="Jamal")

#sets up bot object with intents && adds bot 'status' 
client = commands.Bot(command_prefix='$', intents= discord.Intents.all(), activity=activity)
    
#loads each commands from commands folder
async def load_extensions():
    for filename in os.listdir(r"C:\Users\adilr\Desktop\cthulhu\commands"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"commands.{filename[:-3]}")

@client.event
async def on_ready():
    print(f'\n\nLogged in as: {client.user.name} - {client.user.id}\nVersion: {discord.__version__}\n')
    print(f"{client.user} is on")

#starts bot 
async def main():
    async with client:
        await load_extensions()
        await client.start(token, reconnect=True)

asyncio.run(main())
