from dataclasses import dataclass
from typing import List
import discord
from dataclasses_json import dataclass_json



@dataclass
class HelloWorld():
    hello: str
    world: str


# A dictionary to store tagged images and their tags
tagged_images = {}

# A dictionary to store tag votes for each image
tag_votes = {}

top_tags = ['DnL', 'DnL2', 'DnL3', 'Encounters'] # , 'Miniature']
# A list of the top 6 most common tags or categories (you can fetch this from your database)
emojis_tags = [f'\U0001F1E6', f'\U0001F1E7', f'\U0001F1E8', f'\U0001F1E9'] # , ':moyai:']

suggested_tags = {f'\U0001F1E6': 'DnL',
                  f'\U0001F1E7': 'DnL2',
                  f'\U0001F1E8': 'DnL3',
                  f'\U0001F1E9': 'Encounters'}
#                   ':moyai:': 'Miniature'}

@dataclass_json
@dataclass
class Picture:
    original_message_id: int
    original_channel_id: int # discord.ChannelType.text
    image_url: str
    original_author_id: int
    tags: List[str]
