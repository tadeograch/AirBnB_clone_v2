#!/usr/bin/python3
""" Test file for Amenity"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Testing amenity """

    def __init__(self, *args, **kwargs):
        """ Instantation """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Testing name """
        new = self.value()
        self.assertEqual(type(new.name), str)
