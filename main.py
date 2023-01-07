import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

#loads token from .env file
load_dotenv()
token = os.getenv('token_v')

bot = commands.Bot(command_prefix="$", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"{bot.user} is on")

@bot.command(name='verify', description='grants access to the server')
async def verify(ctx, user: discord.ext.commands.UserConverter):
    user_object = await user

    guild = ctx.guild

    add_role = discord.utils.get(guild.roles, name='fish')
    remove_role = discord.utils.get(guild.roles, name='washups')

    await user_object.add_roles(add_role)
    await user_object.remove_roles(remove_role)

    await ctx.send_response(f"{user_object} has been granted access")

bot.run(token)
