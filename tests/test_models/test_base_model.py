#!/usr/bin/python3
""" Test file for Base Model"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from os import getenv


class test_basemodel(unittest.TestCase):
    """ Testing BaseModel """

    def __init__(self, *args, **kwargs):
        """ Instantation """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ Empty method """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ Testing default """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Testing kwargs """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ Testing kwargs int """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ Testing str """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.to_dict()))

    def test_todict(self):
        """ Testing to_dict """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ Testing kwargs none """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ Testing kwargs """
        n = {'Name': 'test'}
        new = BaseModel(**n)
        self.assertEqual(type(new), BaseModel)

    def test_id(self):
        """ Testing id """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ Testing created_at """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ Testing updated_at """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
