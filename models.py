from cgi import FieldStorage
from ctypes import Array
from enum import unique
from typing import Text
from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('auctions.sqlite')

class User(UserMixin, Model):
    username = CharField(unique = True)
    email = CharField(unique = True)
    password = CharField()
    # Model needs to be changed while in development. 
    # Add these fields when feature is implemented.
    # feedback
    # rating
    # auctions
    # messages

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    print("Connected to Database")
    DATABASE.create_tables([User], safe = True)
    print("Create table check")
    DATABASE.close()
