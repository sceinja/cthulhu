from discord.ext import commands

class get_server_ID(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name='getserverid', description="gets server ID", with_app_command=True)
    async def getserverid(self, ctx: commands.Context):
            
        guild = ctx.guild

        await ctx.send(f"Server ID: {guild.id}")


async def setup(client):
   await client.add_cog(get_server_ID(client))



            


