from peewee import *
import datetime
from flask_login import UserMixin

import os
from playhouse.db_url import connect


if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get('postgres://qtszgjogdmqwqd:f9a820fee4065ba9322f70d25636dbd31fa04261631f5e79e1c2ef04744c8eb1@ec2-18-215-41-121.compute-1.amazonaws.com:5432/de32a3255v80st'))
else:
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


class Auctions(Model):
    user = ForeignKeyField(User, backref='auctions')
    created_date = DateTimeField(default = datetime.datetime.now)
    auction_date = DateTimeField()
    title = CharField(255)
    description = CharField(255)
    price = DoubleField()
    price_increment = DoubleField()
    # Need to add photo and participant list on this model
    # photo = BlobField()
    # participants = [ForeignKeyField(User, backref='auctions')]

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    print("Connected to Database")
    DATABASE.create_tables([User, Auctions], safe = True)
    print("Create table check")
    DATABASE.close()
