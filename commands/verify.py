import discord
from discord.ext import commands
from discord.utils import get
from discord import app_commands

class verify(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name='verify', description='grants access to the server', with_app_command=True)
    @app_commands.guilds(discord.Object(id = 1034136477782777926))
    async def verify(self, ctx: commands.Context, user: discord.Member=None):

        #checks if author has manage roles permission
        if ctx.author.guild_permissions.manage_roles:

            if user==None:
                e_wrong_cmd = discord.Embed(
                    title='No user mentioned',
                    description='Correct usage: `$verify @mention`',
                    colour= 0x228B22
                )

                e_wrong_cmd.set_footer(text="Incorrect Command Usage")

                await ctx.send(embed=e_wrong_cmd)
            
            else:

                guild = ctx.guild
                member = user

                role = get(guild.roles, name='fish')

                #checks if the member being verified is already verified.
                if role in member.roles:

                    #message embed
                    e_alreadyVerified = discord.Embed(
                        description=(f"{member.mention} is already verified :anger:"),
                        colour=0x228B22
                    )

                    await ctx.send(embed=e_alreadyVerified)

                else:

                    add_role = discord.utils.get(guild.roles, name='fish')
                    remove_role = discord.utils.get(guild.roles, name='washups')

                    await member.add_roles(add_role)
                    await member.remove_roles(remove_role)

                    e_verified = discord.Embed(
                    description=(f"{member.mention} has been granted access to {guild.name}! :white_check_mark:"),
                    colour= 0x228B22
                )

                    await ctx.send(embed=e_verified)
        else:

            e_noPerms = discord.Embed(description='You are missing the `Manage Roles` permission :warning:', colour= 0x228B22)

            e_noPerms.set_footer(text="Insufficient Permissions")

            await ctx.send(embed=e_noPerms, ephemeral=True)

async def setup(client):
   await client.add_cog(verify(client))
