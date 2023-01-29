import discord
from discord.ext import commands
import asyncio

class timeout(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name='timeout', description='times out / mutes a member', with_app_command=True)
    async def timeout(self, ctx: commands.Context, user: discord.Member, duration: int):
        pass
        #not ready

def setup(client):
    client.add_cog(timeout(client))
