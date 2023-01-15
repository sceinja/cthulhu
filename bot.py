import discord
from discord.ext import commands
from discord import app_commands
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

@client.command(description='grants access to the server')
async def verify(ctx, user: discord.Member):

    if ctx.author.guild_permissions.manage_roles:
    
        guild = ctx.guild
        member = user
    
        role = get(guild.roles, name='fish')
    
        if role in member.roles:
    
            await ctx.send(f"{member.mention} is already verified")
    
        else:
    
            add_role = discord.utils.get(guild.roles, name='fish')
            remove_role = discord.utils.get(guild.roles, name='washups')
    
            await member.add_roles(add_role)
            await member.remove_roles(remove_role)
    
            await ctx.send(f"{user.mention} has been granted access to {guild.name}")
    else:
        
        await ctx.send("You don't have the 'manage roles' permission")


client.run(token)
