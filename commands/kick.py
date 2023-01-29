import discord
from discord.ext import commands

class kick(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name='kick', description='kicks the mentioned member', with_app_command=True)
    async def kick(self, ctx: commands.Context, user: discord.Member=None):

        if ctx.author.guild_permissions.kick_members:

            try:
                await ctx.guild.kick(user)
                await ctx.send(f"{user} has been kicked!")
            
            except discord.NotFound:
                await ctx.send("The user was not found")
            
            except discord.Forbidden:
                await ctx.send("I do not have permissions to kick members")

        else:
            await ctx.send("You do not have the permissions required to kick members!")
            
async def setup(client):
    await client.add_cog(kick(client))