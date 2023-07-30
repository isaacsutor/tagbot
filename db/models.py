from sqlalchemy import create_engine, Column, Integer, String, Unicode, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, backref

db_file = 'testing_database.db'
engine = create_engine(f'sqlite:///{db_file}', echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


picture_tag_association_table = Table(
    'picture_tag_association',
    Base.metadata,
    Column('picture_id', Integer, ForeignKey('pictures.picture_id')),
    Column('tag_id', Integer, ForeignKey('tags.tag_id'))
)


class User(Base):
    __tablename__ = 'users'

    user_id: int = Column(Integer, primary_key=True, autoincrement=False)
    name: str = Column(String, nullable=False)
    display_name: str = Column(String, nullable=True)
    # pictures = Column('picture_id', Integer, ForeignKey('pictures.picture_id'))
    pictures = relationship('Picture', backref=backref('users'))

class Picture(Base):
    __tablename__ = 'pictures'

    picture_id = Column(Integer, primary_key=True)
    picture_url = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    # user_id = relationship('User', backref=backref('pictures'))
    tags = relationship('Tag',
                        secondary=picture_tag_association_table,
                        back_populates='pictures'
                        )

class Tag(Base):
    __tablename__ = 'tags'

    tag_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    emoji = Column(Unicode, nullable=True)

    pictures = relationship('Picture',
                            secondary=picture_tag_association_table,
                            back_populates='tags')

'''
class Picture(Base):
    __tablename__ = 'pictures'

    id = Column(Integer, primary_key=True)
    original_message_id = Column(Integer, nullable=False)
    original_channel_id = Column(Integer, nullable=False)
    image_url = Column(String, nullable=False)
    # original_author_id = Column(Integer, nullable=False)

    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', back_populates='pictures')

    tags = relationship('Tag',
                        secondary=picture_tag_association_table,
                        back_populates='pictures'
                        )


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    emoji = Column(Unicode, nullable=True)

    pictures = relationship('Picture',
                            secondary=picture_tag_association_table,
                            back_populates='tags')
'''

Base.metadata.create_all(engine)
session.commit()
session.close()

def add_picture_to_db(message_id, attachment, user_id, Session):
    session = Session()
    picture = Picture(picture_id=message_id,
                      picture_url=attachment.url,
                      user_id=user_id)
    session.add(picture)
    session.commit()
    session.close()
