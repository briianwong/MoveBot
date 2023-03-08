import discord
from discord.ext import commands
import tokenKey

TOKEN = tokenKey.token

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

# This command moves the entire channel
@bot.command()
async def movec (ctx, initialChannel, moveToChannel):
   # Get the channels
   initialChannel = discord.utils.get(ctx.guild.voice_channels, name = str(initialChannel))
   moveToChannel = discord.utils.get(ctx.guild.voice_channels, name = str(moveToChannel))   
   
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


# This command moves the specified users
@bot.command()
async def moveu (ctx, *args):
   users = []
   for i in args:
      moveToChannel = None
      if not i.startswith('<@'):
         moveToChannel = discord.utils.get(ctx.guild.voice_channels, name = str(i))
         print (moveToChannel)

      if i.startswith('<@'):
         #print(i) #this will print the id
         usersMentioned = discord.utils.get(ctx.guild.members, id = int(i[2:-1]))
         print(usersMentioned) #this prints the username
         users.append(usersMentioned)
         # await usersMentioned.move_to(moveToChannel)


   if not moveToChannel:
      await ctx.send(f'dumbass there is no destination channel cane!')
      return
    
   for user in users:
      await user.move_to(moveToChannel)
   
   await ctx.send(f'Moved all members to {moveToChannel.mention}')

      
@bot.event
async def on_ready():
   print("ready")

bot.run(TOKEN)
