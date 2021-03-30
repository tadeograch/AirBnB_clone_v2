#!/usr/bin/python3
""" Test file for User """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Testing user """

    def __init__(self, *args, **kwargs):
        """ Instantation """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Testing first name """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Testing last name """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Testing e-mail """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Testing password """
        new = self.value()
        self.assertEqual(type(new.password), str)
