#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User

import unittest
import datetime
"""define test class to test base model"""


class TestUser(unittest.TestCase):
    """test class for testing BaseModel"""

    def setUp(self):
        """set up module"""
        self.my_model = User()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.my_model_json = self.my_model.to_dict()

        self.args_base = User(89, 'my_model', 0)
        self.base_with_kwargs = User(**self.my_model_json)

    def tearDown(self):
        """tear down module"""
        del self.my_model
        del self.args_base
        del self.base_with_kwargs

    def test_str(self):
        """test string representation"""
        self.assertEqual(self.my_model.name, "My First Model")
        self.assertEqual(self.my_model.my_number, 89)
        self.assertEqual(str(self.my_model), "[User] ({}) {}".format(
            self.my_model.id, self.my_model.__dict__))

    def test_types(self):
        """test everything's type"""
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(self.my_model, User)
        self.assertTrue(issubclass(User, BaseModel))

        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

        self.assertIsInstance(self.my_model_json, dict)
        self.assertIsInstance(self.my_model_json['created_at'], str)
        self.assertIsInstance(self.my_model_json['updated_at'], str)
        self.assertIsInstance(self.my_model_json['__class__'], str)

        self.assertTrue(hasattr(self.my_model, "email"))
        self.assertTrue(self.my_model.email == "")

        self.assertTrue(hasattr(self.my_model, "password"))
        self.assertTrue(self.my_model.password == "")

        self.assertTrue(hasattr(self.my_model, "first_name"))
        self.assertTrue(self.my_model.first_name == "")

        self.assertTrue(hasattr(self.my_model, "last_name"))
        self.assertTrue(self.my_model.last_name == "")

        self.assertIsInstance(self.my_model.id, str)

    def test_dictRepresentation(self):
        """test the to dict method"""
        self.my_model.id = 'fa5f7cec-e7e1-436f-ba49-35241277adac'
        self.my_model.first_name = 'last_name'
        self.my_model.last_name = 'first_name'
        self.my_model_json = self.my_model.to_dict()
        self.assertDictEqual(self.my_model_json, {
            'my_number': 89,
            'name': 'My First Model',
            '__class__': 'User',
            'updated_at': self.my_model.updated_at.isoformat(),
            'created_at': self.my_model.created_at.isoformat(),
            'id': self.my_model.id,
            'first_name': 'last_name',
            'last_name': 'first_name'
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

        self.assertTrue(89 not in self.args_base.to_dict())
        self.assertTrue("my_model" not in self.args_base.to_dict())
        self.assertTrue(0 not in self.args_base.to_dict())

        self.assertIsInstance(self.args_base, BaseModel)
        self.assertIsInstance(self.args_base, User)
        self.assertIsNotNone(self.args_base.id)
        self.assertIsNotNone(self.args_base.created_at)
        self.assertIsNotNone(self.args_base.updated_at)

    def test_kwargs(self):
        """test initialization of a base model instance with kwargs"""

        self.assertEqual(self.base_with_kwargs.id, self.my_model.id)
        self.assertEqual(self.base_with_kwargs.created_at,
                         self.my_model.created_at)
        self.assertEqual(self.base_with_kwargs.updated_at,
                         self.my_model.updated_at)
        self.assertEqual(self.base_with_kwargs.name, self.my_model.name)
        self.assertEqual(self.base_with_kwargs.my_number,
                         self.my_model.my_number)

        self.assertEqual(str(self.base_with_kwargs), str(self.my_model))

        self.assertDictEqual(self.base_with_kwargs.to_dict(),
                             self.my_model.to_dict())

        self.base_with_kwargs.save()
        self.assertNotEqual(self.base_with_kwargs.updated_at,
                            self.my_model.updated_at)

    def test_none_kwargs(self):
        """test initialization of a base model instance with no kwargs"""
        my_user2 = User()
        my_user2.first_name = "John"
        my_user2.email = "airbnb2@mail.com"
        my_user2.password = "root"
        self.assertIsInstance(my_user2.created_at, datetime.datetime)
        self.assertIsInstance(my_user2.updated_at, datetime.datetime)

        self.assertIsInstance(my_user2.to_dict(), dict)
        self.assertIsInstance(my_user2.to_dict()['created_at'], str)
        self.assertIsInstance(my_user2.to_dict()['updated_at'], str)
        self.assertIsInstance(my_user2.to_dict()['first_name'], str)
        self.assertIsInstance(my_user2.to_dict()['email'], str)
        self.assertIsInstance(my_user2.to_dict()['password'], str)

        self.assertEqual(my_user2.first_name, 'John')
        self.assertEqual(my_user2.email, 'airbnb2@mail.com')
        self.assertEqual(my_user2.password, 'root')
        self.assertIsInstance(my_user2.id, str)

    def test_args_and_kwargs(self):
        """test initialization of a base model instance with args
                and no kwargs"""
        base3 = User(1, 2, name='best_school', num=89)
        base4 = User(name='bestest_school', num=8989)
        self.assertIsInstance(base3, User)
        self.assertIsInstance(base3, BaseModel)
        self.assertEqual(base3.name, 'best_school')
        self.assertEqual(base3.num, 89)
        self.assertIsInstance(base4, BaseModel)
        self.assertIsInstance(base4, User)
        self.assertEqual(base4.name, 'bestest_school')
        self.assertEqual(base4.num, 8989)