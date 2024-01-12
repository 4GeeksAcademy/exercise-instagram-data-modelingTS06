import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False)
    firstName = Column(String(250),nullable=False)
    lastName = Column(String(250),nullable=False)
    Email = Column(String(250),nullable=False)

    def serialize (self):
        return{
            "userName":self.userName,
            "firstName":self.userName,
            "lastName":self.lastName,
            "Email":self.Email,
        }

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    followingUserID = Column(Integer,ForeignKey("user.id"))
    followedUserID = Column(Integer,ForeignKey("user.id"))

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userID=relationship(User)
    caption = Column(String)
    postDate = Column(Integer)
    postTime = Column(Integer)

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    postID = Column(Integer,ForeignKey("post.id"))
    type = Column(String)
    url = Column(String)

    def serialize(self):
        return {
            "type":self.type,
            "url":self.url,
        }

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    commentText = Column(String,nullable=True)
    authorID = Column(Integer,ForeignKey("user.id"))
    postID = Column(Integer,ForeignKey("post.id"))

    def serialize(self):
        return {
            "commentText":self.commentText,
            "authorID":self.authorID,
            "postID":self.postID,
        }


 
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
