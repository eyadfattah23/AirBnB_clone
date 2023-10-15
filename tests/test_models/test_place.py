#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place

import unittest
import datetime
"""define test class to test base model"""


class TestPlace(unittest.TestCase):
    """test class for testing BaseModel"""

    def setUp(self):
        """set up module"""
        self.my_model = Place()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.my_model_json = self.my_model.to_dict()

        self.args_base = Place(89, 'my_model', 0)
        self.base_with_kwargs = Place(**self.my_model_json)

    def tearDown(self):
        """tear down module"""
        del self.my_model
        del self.args_base
        del self.base_with_kwargs
