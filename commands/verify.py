import discord
from discord.ext import commands
from discord.utils import get

class verify(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(description='grants access to the server')
    async def verify(self, ctx, user: discord.Member):

        #checks if author has manage roles permission
        if ctx.author.guild_permissions.manage_roles:

            guild = ctx.guild
            member = user

            role = get(guild.roles, name='fish')

            #checks if the member being verified is already verified.
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

async def setup(client):
   await client.add_cog(verify(client))
