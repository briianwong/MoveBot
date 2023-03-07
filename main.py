import discord
from discord.ext import commands
import tokenKey

TOKEN = tokenKey.token

intents = discord.Intents.all()

#discord.Member = discord.utils.get(bot.member, id = member)

# @bot.command(pass_context=True)
# async def move(ctx, member: discord.Member, channel: discord.Channel):
#     await bot.move_member(member, channel)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def move (ctx, initialChannel, moveToChannel):
   # Get the channels
   # initial_channel = discord.utils.get(bot.channels, id=initial_channel_id)
   # move_to_channel = discord.utils.get(bot.channels, did=initial_channel_id)


   initialChannel = discord.utils.get(ctx.guild.voice_channels, name = "office")
   #initial_channel_id = discord.VoiceChannel.id
   moveToChannel = discord.utils.get(ctx.guild.voice_channels, name = "voice1")   
   #move_to_channel_id = discord.VoiceChannel.id
    


   # Check if the channel types are valid
   if not isinstance(initialChannel, (discord.VoiceChannel)):
      await ctx.send('Invalid ID for `initial_channel_id`')
      return
   if not isinstance(moveToChannel, (discord.VoiceChannel)):
      await ctx.send('Invalid ID for `move_to_channel_id`')
      return

   # Move all the members:
   for member in initialChannel.members:
      try:
         await member.move_to(moveToChannel)
      except discord.Forbidden:
         await ctx.send(f'Trying to move {member} failed')
      else:
         await ctx.send(f'Successfully moved {member}')

   await ctx.send(f'Moved all members from {initialChannel.mention} to {moveToChannel.mention}')

@bot.event
async def on_ready():
   print ("hello world")
   print("ready")

bot.run(TOKEN)
