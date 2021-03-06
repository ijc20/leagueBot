from discord.ext.commands import Bot
import discord
import sys, traceback
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config.get('BOT', 'BotToken')

bot = Bot(command_prefix='/')

initial_extenstions = ['cogs.basic', 'cogs.lol']

for extension in initial_extenstions:
    try:
        bot.load_extension(extension)
        print(f'Loaded {extension}')
    except Exception as e:
        print("Failed to load extension {extension}.", file=sys.stderr)
        traceback.print_exc()

@bot.event
async def on_ready():

    print(f'Logged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    await bot.change_presence(game=discord.Game(name='/help'))
    print(f'Logged in and booted...\n\nHistory:\n\n')


bot.run(TOKEN, bot=True, reconnect=True)
