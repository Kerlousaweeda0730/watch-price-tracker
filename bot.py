import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='w/')

@bot.event
async def on_ready():
  try:
    print("Logged in as " + bot.user.name)
  except Exception:
    print(Exception)

bot.run(TOKEN)