from peewee import *
from david.config import config
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteDatabase(config.get_database(), pragmas={'foreign_keys': 1})

class People(Model):
    pass