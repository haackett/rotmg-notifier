import discord
from discord.ext import commands
import asyncio
from scraper import Scraper
import display
import logging
from dotenv import load_dotenv
import os


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

#### CONFIG ####
private_token = os.environ.get("privateToken")
event_channel_id = int(os.environ.get("eventChannelId"))
bot = commands.Bot(command_prefix='$')
################

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

###################

scraper = Scraper()

################


@bot.event
async def on_ready():
    print('logged on as {0.user}!'.format(bot))

    print('scraper:', Scraper())

async def clear():
    channel = bot.get_channel(event_channel_id)
    print('clearing channel')
    await channel.purge(limit=100)


async def post_events():
    await bot.wait_until_ready()
    while not bot.is_closed():
        try:
            events = scraper.get_servers()
            messages = display.display_events(events)
            channel = bot.get_channel(event_channel_id)
            await clear()
            await channel.send(messages)
            await asyncio.sleep(delay=60)
        except Exception as e:
            print(e)
    if bot.is_closed():
        scraper.close()

task = bot.loop.create_task(post_events())
bot.run(private_token)
