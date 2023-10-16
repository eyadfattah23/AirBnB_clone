#!/usr/bin/python3
"""define test class to test base model"""

from models.base_model import BaseModel
from models.amenity import Amenity

import unittest
import datetime


class TestState(unittest.TestCase):
    """test class for testing BaseModel"""

    def setUp(self):
        """set up module"""
        self.my_model = Amenity()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.my_model_json = self.my_model.to_dict()

        self.args_base = Amenity(89, 'my_model', 0)
        self.base_with_kwargs = Amenity(**self.my_model_json)
