import discord
from discord.ext import commands


class unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name='unban', description='unbans a banned user', with_app_command=True)
    async def unban(self, ctx: commands.Context, userid: str = None):
        
        if ctx.author.guild_permissions.administrator:


            if userid==None:
                await ctx.send('Please specify a userid to be unbanned')

            else:
                user = ctx.guild.get_member(int(userid))
                await ctx.guild.unban(user)
                await ctx.send(f"`{user}` has been unbanned!")

        else:
            await ctx.send("You don't have valid permissions")

async def setup(client):
    await client.add_cog(unban(client))