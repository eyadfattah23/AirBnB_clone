#!/usr/bin/python3
from models.base_model import BaseModel

import unittest
import datetime
"""define test class to test base model"""


class TestBaseModel(unittest.TestCase):
    """test class for testing BaseModel"""

    def setUp(self):
        """set up module"""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.my_model_json = self.my_model.to_dict()

        self.args_base = BaseModel(89, 'my_model', 0)

    def tearDown(self):
        """tear down module"""
        del self.my_model
        del self.args_base

    def test_str(self):
        """test string representation"""
        self.assertEqual(self.my_model.name, "My First Model")
        self.assertEqual(self.my_model.my_number, 89)
        self.assertEqual(str(self.my_model), "[BaseModel] ({}) {}".format(
            self.my_model.id, self.my_model.__dict__))

    def test_types(self):
        """test everything's type"""
        self.assertIsInstance(self.my_model, BaseModel)

        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

        self.assertIsInstance(self.my_model_json, dict)
        self.assertIsInstance(self.my_model_json['created_at'], str)
        self.assertIsInstance(self.my_model_json['updated_at'], str)
        self.assertIsInstance(self.my_model_json['__class__'], str)

        self.assertIsInstance(self.my_model.id, str)

    def test_dictRepresentation(self):
        """test the to dict method"""
        self.my_model.id = 'fa5f7cec-e7e1-436f-ba49-35241277adac'
        self.my_model_json = self.my_model.to_dict()
        self.assertDictEqual(self.my_model_json, {
            'my_number': 89,
            'name': 'My First Model',
            '__class__': 'BaseModel',
            'updated_at': self.my_model.updated_at.isoformat(),
            'created_at': self.my_model.created_at.isoformat(),
            'id': self.my_model.id
        })

    def test_save(self):
        """test the save method if it changes the updated at"""
        up_at1 = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(up_at1, self.my_model.updated_at)

    def test_args(self):
        """test if the *args is read (it shouldn't be)"""
        with self.assertRaises(AttributeError) as e:
            self.assertIsNone(self.args_base.number)
            self.assertIsNone(self.args_base.number)
            self.assertIsNone(self.args_base.name)
            self.assertIsNone(self.args_base.updated_at)

    def test_kwargs(self):
        """test initalization of a base model instance with kwargs"""
        base_kwargs = BaseModel(**self.my_model_json)
        self.assertEqual(base_kwargs.id, self.my_model.id)
        self.assertEqual(str(base_kwargs), str(self.my_model))
        # NOT FINISHED YET
        # there's an error somewhere
