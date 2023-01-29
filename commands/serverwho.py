import discord
from discord.ext import commands

class serverwho(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name='serverwho', description="Fetches server information", with_app_command=True)
    async def getserverid(self, ctx: commands.Context):
            
        guild = ctx.guild

        embedServerId = discord.Embed(
            title='Server Information:',
            colour=0x228B22
        )   

        embedServerId.add_field(
            name=':mailbox:  ID:', 
            value=(f'`{guild.id}`'), 
            inline=False
        )
        
        embedServerId.add_field(
            name=':identification_card: Owner:', 
            value=(f'{guild.owner.mention} [`{guild.owner_id}`]'), 
            inline=False
        )
        
        date_string = guild.created_at.strftime("%Y-%m-%d")
        time_string = guild.created_at.strftime("%H:%M:%S")
        
        embedServerId.add_field(
                name=':date: Date created:', 
                value=(f'{date_string} {time_string}'), 
                inline=False    
            )
        
        embedServerId.add_field(
            name=':people_hugging: Members:', 
            value=(f'`{guild.member_count}`'), 
            inline=False
        )

        await ctx.send(embed=embedServerId)


async def setup(client):
   await client.add_cog(serverwho(client))



            


