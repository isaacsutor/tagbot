from sqlalchemy import create_engine, Column, Integer, String, Unicode, Table, ForeignKey
from sqlalchemy.orm import sessionmaker
from db import engine
from models import Tag, Picture, User

Session = sessionmaker(bind=engine)
session = Session()

# original_message_id: int
# original_channel_id: int # discord.ChannelType.text
# image_url: str
# original_author_id: int

# Example: Inserting data with tags and establishing many-to-many relationship
# picture1 = Picture()
# picture2 = Picture()

tag1 = Tag(name='Chapter 30') # emoji=None
tag2 = Tag(name='Orc')
tag3 = Tag(name='Troll')
tag4 = Tag(name='MESBG Proxy')
tag5 = Tag(name='Spear')

session.add(tag1)
session.add(tag2)
session.add(tag3)
session.add(tag4)
session.add(tag5)

session.commit()

# Close the session
session.close()

# Associate tags with the respective pictures using the many-to-many relationship
# picture1.tags.extend([tag1, tag2])
# picture2.tags.extend([tag2, tag3])

# Add data to the session and commit changes
# session.add(picture1)
# session.add(picture2)
