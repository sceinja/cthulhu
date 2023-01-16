import discord
import importlib
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import os


#loads token from .env file
load_dotenv()
token = os.getenv('TOKEN')

#sets up bot object
client = commands.Bot(command_prefix='$', intents= discord.Intents.all())

@client.event
async def on_ready():
    print(f"{client.user} is on")

#imports commands from command folder 
for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        setup = importlib.import_module(f'commands.{filename[:-3]}.setup')
        setup(client)


client.run(token)
