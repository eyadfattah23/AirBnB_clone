#!/usr/bin/python3
from models.base_model import BaseModel
from models.city import City

import unittest
import datetime
"""define test class to test base model"""


class TestCity(unittest.TestCase):
    """test class for testing BaseModel"""

    def setUp(self):
        """set up module"""
        self.my_model = City()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.my_model_json = self.my_model.to_dict()

        self.args_base = City(89, 'my_model', 0)
        self.base_with_kwargs = City(**self.my_model_json)

    def tearDown(self):
        """tear down module"""
        del self.my_model
        del self.args_base
        del self.base_with_kwargs

    def test_str(self):
        """test string representation"""
        self.assertEqual(self.my_model.name, "My First Model")
        self.assertEqual(self.my_model.my_number, 89)
        self.assertEqual(str(self.my_model), "[City] ({}) {}".format(
            self.my_model.id, self.my_model.__dict__))

    def test_types(self):
        """test everything's type"""
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(self.my_model, City)
        self.assertTrue(issubclass(City, BaseModel))

        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

        self.assertIsInstance(self.my_model_json, dict)
        self.assertIsInstance(self.my_model_json['created_at'], str)
        self.assertIsInstance(self.my_model_json['updated_at'], str)
        self.assertIsInstance(self.my_model_json['__class__'], str)

        self.assertTrue(hasattr(self.my_model, "name"))

        self.assertIsInstance(self.my_model.id, str)
