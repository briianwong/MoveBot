import discord
from discord.ext import commands
import tokenKey

TOKEN = tokenKey.token

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

# This command moves the entire channel
@bot.command()
@commands.has_guild_permissions(move_members=True)
async def movec (ctx, initialChannel, moveToChannel):
   # Get the channels
   initialChannel = discord.utils.get(ctx.guild.voice_channels, name = str(initialChannel))
   moveToChannel = discord.utils.get(ctx.guild.voice_channels, name = str(moveToChannel))   
   print(initialChannel)
   print(moveToChannel)

   # Check if the channel types are valid
   if not isinstance(initialChannel, (discord.VoiceChannel)):
      await ctx.send('Invalid ID for `initialChannel`')
      return
   if not isinstance(moveToChannel, (discord.VoiceChannel)):
      await ctx.send('Invalid ID for `moveToChannel`')
      return

   # Move all the members:
   for member in initialChannel.members:
      try:
         await member.move_to(moveToChannel)
      except discord.Forbidden:
         await ctx.send(f'Trying to move {member} failed')
   
   await ctx.send(f'Moved all members from {initialChannel.mention} to {moveToChannel.mention}')



################ NEW COMMAND ##################



# This command moves the specified users
@bot.command()
@commands.has_guild_permissions(move_members=True)
async def moveu (ctx, *args):
   users = []
   for i in args:
      moveToChannel = None
      if not i.startswith('<@'):
         moveToChannel = discord.utils.get(ctx.guild.voice_channels, name = str(i))
         print (moveToChannel) #this prints the channel name

      if i.startswith('<@'):
         #print(i) #this will print the id
         usersMentioned = discord.utils.get(ctx.guild.members, id = int(i[2:-1]))
         print(usersMentioned) #this prints the username
         users.append(usersMentioned)

   # Check if the channel is valid
   if not moveToChannel:
      await ctx.send(f'dumbass there is no destination channel')
      return
    
   for user in users:
      await user.move_to(moveToChannel)
   
   await ctx.send(f'Moved members to {moveToChannel.mention}')



################ NEW COMMAND ##################



# This command splits 2 teams into 2 seperate voice channels
class Menu(discord.ui.View):
    def __init__(self, bot, open_channel1_name, open_channel2_name):
        super().__init__()
        self.bot = bot
        self.open_channel1_name = open_channel1_name
        self.open_channel2_name = open_channel2_name
        self.selected_members = []

    async def get_user_id(self, interaction: discord.Interaction):
        user = interaction.user
        user_id = user.id
        return user_id

    def get_selected_members_text(self):
      if not self.selected_members:
         return "No one has selected a team yet."
      else:
         team_names = {self.open_channel1_name: "Team 1", self.open_channel2_name: "Team 2"}
         text = "Select a team to join. Click Start when ready.\n"
         for member, channel_name in self.selected_members:
               team_name = team_names.get(channel_name, "Unknown Team")
               text += f"{member.mention} has selected {team_name}.\n"
         return text

    @discord.ui.button(label="Team 1", style=discord.ButtonStyle.blurple)
    async def team1(self, interaction: discord.Interaction, button: discord.ui.Button):
      user_id = await self.get_user_id(interaction) #this works
      #user_id = interaction.user.id #new test / way to get user id

      member = interaction.guild.get_member(user_id) #good

      self.selected_members.append((member, self.open_channel1_name)) #working channel list

      #working
      embed = interaction.message.embeds[0]
      embed.description = self.get_selected_members_text()
      await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="Team 2", style=discord.ButtonStyle.gray)
    async def team2(self, interaction: discord.Interaction, button: discord.ui.Button):
      user_id = await self.get_user_id(interaction)
      #user_id = interaction.user.id #new test / wayt to get user id
      
      member = interaction.guild.get_member(user_id) #good

      self.selected_members.append((member, self.open_channel2_name)) #working channel list
      
      #working
      embed = interaction.message.embeds[0]
      embed.description = self.get_selected_members_text()
      await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="Start", style=discord.ButtonStyle.green)
    async def ready(self, interaction: discord.Interaction, button: discord.ui.Button):
        message = interaction.message
        await message.delete()
        for member, channel_name in self.selected_members:
            voice_state = member.voice
            if voice_state:
                channel = discord.utils.get(interaction.guild.voice_channels, name=channel_name)
                await member.move_to(channel)
        
        await interaction.response.send_message("Moved users to their respective team channels.")
        self.selected_members.clear() #clears message
    

@bot.command()
@commands.has_guild_permissions(move_members=True)
async def ten (ctx, open_channel1, open_channel2):
    view = Menu(bot, open_channel1, open_channel2)
    embed = discord.Embed(
        title="10 Mans",
        description="Select a team to join. Click Start when ready.",
        color=0x00FF00
    )
    await ctx.send(embed=embed, view=view)


@bot.event
async def on_ready():
   print("Ready")

bot.run(TOKEN)
