from db import engine
from sqlalchemy.orm import sessionmaker
from models import Picture, Tag, User
Session = sessionmaker(bind=engine)

session = Session()
tag1 = Tag(name='Chapter 30') # emoji=None
tag2 = Tag(name='Orc')
# {"original_message_id": 1135258921192403014,
# "original_channel_id": 1133362551657336963,
# "image_url": "https://cdn.discordapp.com/attachments/1133362551657336963/1135258920949137439/image.png",
# "original_author_id": 291730225157373953,
# "tags": []}
picture = Picture(picture_id=1135258921192403015,
                  picture_url='https://cdn.discordapp.com/attachments/1133362551657336963/1135258920949137439/image.png',
                  user_id=291730225157373953)
tag = session.query(Tag).filter(Tag.tag_id == 1).one_or_none()
print(tag)
picture.tags.append(tag)
session.add(picture)
session.commit()
session.close()
