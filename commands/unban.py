import discord
from discord.ext import commands

class unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name='unban', description='unbans a banned user', with_app_command=True)
    async def unban(self, ctx: commands.Context, user_id: int):
        
        if ctx.author.guild_permissions.administrator:
            
            if user_id==None:
                await ctx.send("No user ID mentioned")

            try:
                await ctx.guild.unban(discord.Object(id=user_id))
                await ctx.send(f'{user_id} has been unbanned.')

            except discord.NotFound:
                await ctx.send(f'No user found with ID {user_id}.')
            
            except discord.Forbidden:
                await ctx.send('I do not have the permission to unban that user.')
        else:
            await ctx.send("You don't have permission to use this command.")

async def setup(client):
    await client.add_cog(unban(client))