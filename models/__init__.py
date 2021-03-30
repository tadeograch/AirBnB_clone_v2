#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv


NEW_TYPE = getenv("HBNB_TYPE_STORAGE")
if NEW_TYPE == "db":
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
