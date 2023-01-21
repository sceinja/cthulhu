import discord
from discord.ext import commands


class ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name='ban', description='bans the user mentioned', with_app_command=True)
    async def ban(self, ctx: commands.Context, user: discord.Member=None):
        
        if user==None:
            await ctx.send('Please specify a user to be banned')

        else:

            await ctx.guild.ban(user)
            await ctx.send(f"{user.mention} has been banned!")

async def setup(client):
    await client.add_cog(ban(client))
