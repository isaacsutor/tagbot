import discord
from discord.ext import commands

from old.domain import (Picture, emojis_tags, suggested_tags, tag_votes,
                    tagged_images, top_tags)

async def add_user(bot, user):
    return True


async def suggest_tags_for_image(bot, picture: Picture):
    description = 'React with emojis to tag the image:'
    for i, top_tag in enumerate(top_tags):
        description = description + '\n' + emojis_tags[i] + ' ' + top_tag

    embed = discord.Embed(title='Tag Suggestions', description=description)

    embed.set_image(url=picture.image_url)
    msg = await bot.get_channel(picture.original_channel_id).send(embed=embed)

    for i, top_tag in enumerate(top_tags):
        # emoji = f'\U0001F1E6'  # Use flags as emojis for simplicity
        await msg.add_reaction(emojis_tags[i])


async def detect_image(bot, message):
    for attachment in message.attachments:
        picture = Picture(original_message_id=message.id,
                            original_channel_id=message.channel.id,
                            original_author_id=message.author.id,
                            image_url=attachment.url,
                            tags=[])
        # pictures.append(picture) # add to db
        print(picture.to_json())
        
        # await suggest_tags_for_image(bot, picture)

def has_image(message):
    # Check if the message has any attachments
    if message.attachments:
        # Check if the first attachment is an image (you can add more sophisticated checks here)
        return True  # message.attachments[0].url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    else:
        return False
