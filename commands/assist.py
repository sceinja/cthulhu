import discord
from discord.ext import commands
from discord import app_commands

class assist(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name='assist', description="shows all available commands", with_app_command=True)
    async def getserverid(self, ctx: commands.Context):
            
        e_help = discord.Embed(
            title="Commands help: :book:",
            description='All the commands that are currently availble or will be added soon',
            colour= 0x228B22,
        )

        e_help.add_field(name='Moderation & Security:', value='`verify`, `ban`, `kick`, `timeout`, `untimeout`, `whois`, `getserverid`', inline=False)
        e_help.add_field(name='Music:', value='`play`, `next`, `previous`, `pause`, `queue`', inline=False)

        await ctx.send(embed=e_help)
    

async def setup(client):
   await client.add_cog(assist(client))