import discord
from discord.ext import commands
from discord import app_commands

class get_server_ID(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name='getserverid', description="gets server ID", with_app_command=True)
    @app_commands.guilds(discord.Object(id = 1034136477782777926))
    async def getserverid(self, ctx: commands.Context):
            
        guild = ctx.guild

        await ctx.send(f"Server ID: {guild.id}", ephemeral=True)


async def setup(client):
   await client.add_cog(get_server_ID(client))



            


