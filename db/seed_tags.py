from db import engine
from sqlalchemy.orm import sessionmaker
from models import Picture, Tag
Session = sessionmaker(bind=engine)

session = Session()
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

session.close()
