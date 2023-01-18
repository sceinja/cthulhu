import discord
from discord.ext import commands
from discord import app_commands

class pfp(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name='pfp', description="displays a user's profile picture", with_app_command=True)
    async def pfp(self, ctx: commands.Context, user: discord.Member=None):

        if user==None:
            user = ctx.author
            await ctx.send(user.avatar)
        else:
            await ctx.send(user.avatar)

async def setup(client):
   await client.add_cog(pfp(client))

            
        