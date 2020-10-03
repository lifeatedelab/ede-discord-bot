import os
from discord.ext import commands
from dotenv import load_dotenv

from query import participants, total_participant

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot('!ede ')

@bot.command(name='openmind')
async def openmind(ctx):
    header = '''Total pendaftar: {} mahasiswa
NO\t|   NAMA LENGKAP    |    NIM     | ANGKATAN |               EMAIL                |
    '''.format(total_participant)
    await ctx.send(header)

    for data in participants:
        await ctx.send(''' 
        {}\t\t|        {}        |     {}      |   {}  |               {}              |
        '''.format(data[0], data[1], data[2], data[4], data[3]))

bot.run(TOKEN)