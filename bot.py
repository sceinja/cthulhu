import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

#loads token from .env file
load_dotenv()
token = os.getenv('TOKEN')

#sets up bot intents
intents=discord.Intents.default()
intents = intents.all()

#sets up bot object
client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is on")

@client.command(name='verify', description='grants access to the server')
async def verify(ctx, user: discord.User):

    if ctx.author.guild_permissions.manage_roles:

        user_object = user
        guild = ctx.guild
        member = ctx.guild.get_member(user_object.id)

        add_role = discord.utils.get(guild.roles, name='fish')
        remove_role = discord.utils.get(guild.roles, name='washups')

        await member.add_roles(add_role)
        await member.remove_roles(remove_role)

        await ctx.send(f"{user_object} has been granted access to {guild.name}")
    
    else:
        
        await ctx.send("You don't have the 'manage roles' permission")

client.run(token)
