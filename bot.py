import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import app_commands
import asyncio
import os

#loads token from .env file
load_dotenv()
token = os.getenv('TOKEN')


class Client(commands.Bot):
    
    def __init__(self):
    
        intents=discord.Intents.all()
        activity = discord.Activity(type=discord.ActivityType.listening, name="God's word")
    
        super().__init__(command_prefix='$', intents=intents, activity=activity)

    async def setup_hook(self):
        await self.tree.sync(guild = discord.Object(id=1034136477782777926))
        print(f"All slash commands have synced with {self.user}")
    

client = Client()
    
#loads each commands from commands folder
async def load_extensions():
    for filename in os.listdir(r"C:\Users\adilr\Desktop\cthulhu\commands"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"commands.{filename[:-3]}")

@client.event
async def on_ready():
    print(f'\nLogged in as: {client.user.name} - {client.user.id}\nVersion: {discord.__version__}\n')
    print(f"{client.user} is on")

#starts bot 
async def main():
    async with client:
        await load_extensions()
        await client.start(token, reconnect=True)


asyncio.run(main())
