from typing import Literal, Optional
import discord
from discord.ext import commands
from discord.ui import TextInput
from keep_alive import keep_alive
import os
i  = discord.Intents.all()
owner_id =1200490105371099327
class Adminappliction(discord.ui.Modal,title = "LastBullet Roster Appliction"):
     q1 = TextInput(label="Name?")
     q2 =  TextInput(label = "Age?")  
     q3 = TextInput(label=" how many hours active a day")
     q4 = TextInput(label = "discord experience rate 1-10 ")
     q5 = TextInput(label=" what things you can do as an admin") 
     async def on_submit(self, interaction: discord.Interaction):
         channel = client.get_channel(1150843378217525299)
         embed = discord.Embed(title=f"User : {interaction.user.name}")
         embed.add_field(name="Name:", value=f"```{self.children[0].value}```")
         embed.add_field(name="Age:", value=f"```{self.children[1].value}```")
         embed.add_field(name="Hour active a day:", value=f"```{self.children[2].value}```")
         embed.add_field(name="discord experince:", value=f"```{self.children[3].value}```")
         embed.add_field(name="things you can do as an admin:", value=f"```{self.children[4].value}```") 
         await channel.send(embed=embed)
         await interaction.response.send_message("Application sent to staff and Bot will reply the answer to you , please enable direct messages from everyone in settings to receive bot message", ephemeral=True)
class Rosterappliction(discord.ui.Modal,title = "LastBullet Roster Appliction"):
     q1 = TextInput(label="Current Rank")
     q2 =  TextInput(label="Main Role")  
     q3 = TextInput(label="Peak Rank")
     q4 = TextInput(label = "How many hours active?")
     async def on_submit(self, interaction: discord.Interaction):
         channel = client.get_channel(1150456281958715392)
         embed = discord.Embed(title=f"User : {interaction.user.name}")
         embed.add_field(name="Current Rank:", value=f"```{self.children[0].value}```")
         embed.add_field(name="Main Role:", value=f"```{self.children[1].value}```")
         embed.add_field(name="Peak Rank:", value=f"```{self.children[2].value}```")
         embed.add_field(name="Active Hours:", value=f"```{self.children[3].value}```") 
         await channel.send(embed=embed)
         await interaction.response.send_message("Application sent to staff and Bot will reply the answer to you , please enable direct messages from everyone in settings to receive bot message", ephemeral=True)
class Admibutton(discord.ui.View):
     def __init__(self):
         super().__init__(timeout = None)
         self.value = None
     @discord.ui.button(label="apply", style=discord.ButtonStyle.red,custom_id='persistent_view:green')
     async def Command_Button(self, interaction: discord.Interaction, button: discord.ui.Button):
               await interaction.response.send_modal(Adminappliction())     
##############################################################################################################
class Rosterbutton(discord.ui.View):
     def __init__(self):
         super().__init__(timeout = None)
         self.value = None
     @discord.ui.button(label="apply", style=discord.ButtonStyle.red,custom_id='persistent_view:blue')
     async def Command_Button(self, interaction: discord.Interaction, button: discord.ui.Button):
               await interaction.response.send_modal(Rosterappliction())      
###############################################################################################################
class lbappliction(discord.ui.Modal,title = "LastBullet Clan Appliction"):
    q1 = TextInput(label="What is your name?") 
    q2 = TextInput(label="What is your nickname? (ex:- ChainsawMan)")
    q3 = TextInput(label="What is your age?")
    q4 = TextInput(label="Where are you from?",placeholder="France, Turkey, Egypt..etc")
    q5 = TextInput(label="What is the most online game you play   ?",placeholder="Rocket league")
    async def on_submit(self, interaction: discord.Interaction):
        channel = client.get_channel(1233459742408441856)
        embed = discord.Embed(title=f"User : {interaction.user.name}")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1111699459194241155/1119993114552180858/5ra.jpg")
        #embed.add_field(name="User:", value=f"```{interaction.user}```")
        embed.add_field(name="Name:", value=f"```{self.children[0].value}```")
        embed.add_field(name="Nickname:", value=f"```{self.children[1].value}```")       
        embed.add_field(name="Age:", value=f"```{self.children[2].value}```")
        embed.add_field(name="Country:", value=f"```{self.children[3].value}```")  
        embed.add_field(name="What is the most online game you play?:", value=f"```{self.children[4].value}```")
        # embed.add_field(name="User:", value=f"```{interaction.user}```")     
        await channel.send(embed=embed)
        await interaction.response.send_message("Application sent to staff and Bot will reply the answer to you , please enable direct messages from everyone in settings to receive bot message", ephemeral=True)
class appbutton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        self.value = None
    @discord.ui.button(label="Join", style=discord.ButtonStyle.red,custom_id='persistent_view:red')
    async def Command_Button(self, interaction: discord.Interaction, button: discord.ui.Button):
            role1 =1116580355529510973
            role2 =1116580753900327083      
            role3= 1119041126175866900        
            if role1 not in  [role.id for role in interaction.user.roles] or role3 not in  [role.id for role in interaction.user.roles]  or role2 not in  [role.id for role in interaction.user.roles] or str(interaction.user.name) not in db["pending"][0:]  :   
              await interaction.response.send_modal(lbappliction())      
              db["pending"][0:].append(str(interaction.user.name))
            elif str(interaction.user.name) in db["pending"][0:] :
                      interaction.response.send_message("You applied once, you cannot apply again. Wait for confirmation from admins.")
            else : 
              await interaction.response.send_message("You have been suspended from applying to be member, you can reapply once you dont have suspension.",ephemeral=True)

class PersistentViewBot(commands.Bot):
    def __init__(self):
        i.message_content = True
        super().__init__(command_prefix=commands.when_mentioned_or('!'), intents=i)

    async def setup_hook(self) -> None:
        # Register the persistent view for listening here.
        # Note that this does not send the view to any message.
        # In order to do this you need to first send a message with the View, which is shown below.
        # If you have the message_id you can also pass it as a keyword argument, but for this example
        # we don't have one.
        self.add_view(appbutton())
        self.add_view(Rosterbutton())
        self.add_view(Admibutton())
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

client = PersistentViewBot()
@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def lbmodal(ctx):
    # Get the channel where you want to send the message 
    channel = client.get_channel(1233191527585419284)
    # Create the button
    # 398633398899310605.gif
    with open("398633398899310605.gif", "rb") as gif:
        file = discord.File(gif, filename="file.gif")
    await channel.send(file=file)
    await channel.send('***Want to join LastBullet clan? Do not hesitate to apply by pressing the button below!***.', view=appbutton())        

@client.tree.command(name = "refuse")
async def refuse(interaction,reason:str,member:discord.Member):
  if 1116575896288104530 in [role.id for role in interaction.user.roles] or owner_id in [role.id for role in interaction.user.roles]:
    await member.send(f"You have been declined due to not meeting the conditions to be a member (because of {reason}). You can reapply later. (LastBullet application team™)")
    db["pending"][0:].remove((str(interaction.user.name)))
  else:
    interaction.response.send_message("You do not have permission to do that command", ephemeral=True)         
@client.tree.command()
async def accept(interaction, member: discord.Member):
 if 1116575896288104530 in [role.id for role in interaction.user.roles] or owner_id in [role.id for role in  interaction.user.roles]:  
     role = discord.utils.get(interaction.guild.roles, id= 1006853269462728765)
     guild = client.get_guild(662064075626250310) 
     member = guild.get_member(member.id)
     await member.edit(nick=f'{member.display_name}')
     channel = client.get_channel(1151179158555217960)
     await member.add_roles(role) 
     await member.remove_roles(discord.utils.get(interaction.guild.roles, id=662097656306466826))
     await member.send("You have been approved to be member, welcome to LastBullet clan :heart: (Lastbullet application team™)")   
     await channel.send(f"{member.mention} has joined our family, please welcome our new mate ")   
     await interaction.response.send_message("done")
 else:
      await interaction.response.send_message("you do not have the permission to do this command",ephemeral = True) 
@client.tree.command(name = "priv")
async def priv(interaction:discord.Interaction,msg:str,mention:discord.Member =None,role : discord.Role = None):
    if 1116573645062553662 in [role.id for role in interaction.user.roles] or owner_id in [role.id for role in interaction.user.roles] :
      if mention == None and role == None or  mention != None and role != None:
       await interaction.response.send_message("choose one only role or mention",ephemeral=True) 
      elif  mention == None : 
       await interaction.response.send_message("sent succfully",ephemeral=True) 
       for i in role.members:
        try:       
          await i.send(f'{interaction.user.name} want to tell you : {msg}')
        except:
          print(f"{i.name}")
      elif role == None:
       await interaction.response.send_message("sent succfully",ephemeral=True) 
       await mention.send(f'{interaction.user.name} want to tell you: {msg}')
    else:
        await interaction.response.send_message("you do not have the permission to this action",ephemeral=True)
@client.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1
    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")
# Roster applcation commands
@client.tree.command(name="roster_accept")
async def acccept(interaction, member: discord.Member):
  if 1116573645062553662 in [role.id for role in interaction.user.roles]:  
      role = discord.utils.get(interaction.guild.roles, id= 1085640428881190962)
      guild = client.get_guild(662064075626250310) 
      member = guild.get_member(member.id)
      role2 = discord.utils.get(interaction.guild.roles, id= 1006853269462728765) 
      if role2 in  member.roles:
           await member.add_roles(role2) 
      await member.edit(nick=f'LB {member.display_name} (M)')
      await member.add_roles(role) 
      await member.send("You have been approved to be from last bullet's clan roster clan :heart: ")   
      await interaction.response.send_message("succfully been added")
  else:
       await interaction.response.send_message("you do not have the permission to do this command",ephemeral = True)
@client.tree.command(name = "roster_refuse")
async def reffuse(interaction,reason:str,member:discord.Member):
   if   1116573645062553662 in [role.id for role in interaction.user.roles] :
     await member.send(f"You have been declined due to not meeting the conditions to be a member (because of {reason}). You can reapply later. (LastBullet application team™)")
   else:
     interaction.response.send_message("You do not have permission to do that command", ephemeral=True)  
@client.command()
async def rostermodal(ctx):
    # Get the channel where you want to send the message 
    channel = client.get_channel(1150456236014305381)
    # Create the button
    # 398633398899310605.gif
    #with open("398633398899310605.gif", "rb") as gif:
    #file = discord.File(gif, filename="file.gif")
    # await channel.send(file=file)
    await channel.send('***Click the button to apply for the roster***.', view=Rosterbutton())        
##############################################################################################################
@client.tree.command(name="admin_accept")
async def aacccept(interaction, member: discord.Member,reason:str):
  if 1116573645062553662 in [role.id for role in interaction.user.roles]:  
      guild = client.get_guild(662064075626250310) 
      member = guild.get_member(member.id)
      await member.send(f"You have been approved to be from last bullet's Admins  because of your {reason} :heart: ")   
  else:
       await interaction.response.send_message("you do not have the permission to do this command",ephemeral = True)
@client.tree.command(name = "admin_refuse")
async def refffuse(interaction,reason:str,member:discord.Member):
   if   1116573645062553662 in [role.id for role in interaction.user.roles] :
     await member.send(f"You have been declined due to not meeting the conditions to be a member (because of {reason}). You can reapply later. (LastBullet application team™)")
   else:
     interaction.response.send_message("You do not have permission to do that command", ephemeral=True)       
@client.command()
async def adminmodal(ctx):
    # Get the channel where you want to send the message 
    channel = client.get_channel(1150843037291909231)
    # Create the button
    # 398633398899310605.gif
    #with open("398633398899310605.gif", "rb") as gif:
    #file = discord.File(gif, filename="file.gif")
    # await channel.send(file=file)
    await channel.send('***Click the button to apply to be an admin.***.', view=Admibutton())
keep_alive()     
discordD = os.environ["discord"]     
try:
  client.run(discordD)
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  os.system('kill 1')
  os.system("python restarter.py")
print("velo")     
