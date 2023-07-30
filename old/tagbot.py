'''tagbot.py'''
import random
from typing import List
import logging
import discord
from discord.ext import commands

# from actions import add_image_to_db, has_image, on_message_actions
# from domain import (Picture, emojis_tags, suggested_tags, tag_votes,
#                     tagged_images, top_tags)
# from db import SQLiteManager

# 

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] [%(asctime)s] %(message)s', filename='bot.log')

BOT_TOKEN = 'xxx'
intents = discord.Intents.all()  # (messages=True)
bot = commands.Bot(command_prefix='!', intents=intents)
CHANNEL_ID = '1133362551657336963'
'''
pictures: List[Picture] = []
db_manager = SQLiteManager('testing_database.db')
'''
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    logging.info(f'Logged in as {bot.user.name}')


@bot.event
async def on_message(message: discord.Message):
    # create
    if message.channel.id == 1133362551657336963:
        # if(has_image):
        # add_image_to_db(message)
        # detect_image(bot, message)
        print(message.author.id)
        print(message.author.name)
        print(message.author.display_name)
    await bot.process_commands(message)

cogslist = ['cog.cog1']

async def setup_hook():
    for ext in cogslist:
        await bot.load_extension(ext)

'''
@bot.event
async def on_reaction_add(reaction: discord.Reaction, user):
    # print(reaction)
    if user != bot.user:
        message = await bot.get_channel(reaction.message.channel.id
                                       ).fetch_message(reaction.message.id)
        for picture in pictures:
            if picture.image_url == message.embeds[0].image.url:
                print(reaction.emoji)
                picture.tags.append(suggested_tags.get(reaction.emoji))
                print('match in database')
                print('new status', picture)

    if user != bot.user and reaction.message.id in tag_votes:
        emoji = reaction.emoji
        # if emoji in tag_votes[reaction.message.id]:
        tag = tag_votes[reaction.message.id][emoji]
        tagged_images[reaction.message.embeds[0].image.url].append(tag)
        await reaction.message.channel.send(
            f"{user.mention} tagged the image with '{tag}'")

'''
# Run the bot
bot.run(BOT_TOKEN)
