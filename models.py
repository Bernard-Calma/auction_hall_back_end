from peewee import *
import datetime
from flask_login import UserMixin

import os
from playhouse.db_url import connect
from playhouse.postgres_ext import *

if os.environ.get('FLASK_ENV') != 'production':
    DATABASE = PostgresqlDatabase("auctions", user="postgres", password="admin", host="localhost", port=5432)
    print("Connected to Local Database")
else:
    DATABASE = connect(os.environ.get('DATABASE_URL'))
    print("Connected to Cloud Database")
    

# print("ENVIRON : ", os.environ)
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
    photo = BlobField()
    participants = ArrayField(null = True)
    winner = ForeignKeyField(User, null = True, backref='auctions')
    logs = CharField(default = "")


    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    print("Connected to Database")
    DATABASE.create_tables([User, Auctions], safe = True)
    print("Create table check")
    DATABASE.close()
