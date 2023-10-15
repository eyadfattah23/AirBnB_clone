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

    def test_str(self):
        """test string representation"""
        self.assertEqual(self.my_model.name, "My First Model")
        self.assertEqual(self.my_model.my_number, 89)
        self.assertEqual(str(self.my_model), "[Place] ({}) {}".format(
            self.my_model.id, self.my_model.__dict__))

    def test_types(self):
        """test everything's type"""
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(self.my_model, Place)
        self.assertTrue(issubclass(Place, BaseModel))

        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

        self.assertIsInstance(self.my_model.amenity_ids, list)

        self.assertIsInstance(self.my_model_json, dict)
        self.assertIsInstance(self.my_model_json['created_at'], str)
        self.assertIsInstance(self.my_model_json['updated_at'], str)
        self.assertIsInstance(self.my_model_json['__class__'], str)

        self.assertTrue(hasattr(self.my_model, "city_id"))
        self.assertTrue(self.my_model.city_id == "")

        self.assertTrue(hasattr(self.my_model, "user_id"))
        self.assertTrue(self.my_model.user_id == "")

        self.assertTrue(hasattr(self.my_model, "description"))
        self.assertTrue(self.my_model.description == "")

        self.assertTrue(hasattr(self.my_model, "number_rooms"))
        self.assertTrue(self.my_model.number_rooms == 0)

        self.assertTrue(hasattr(self.my_model, "number_bathrooms"))
        self.assertTrue(self.my_model.number_bathrooms == 0)

        self.assertTrue(hasattr(self.my_model, "max_guest"))
        self.assertTrue(self.my_model.max_guest == 0)

        self.assertTrue(hasattr(self.my_model, "price_by_night"))
        self.assertTrue(self.my_model.price_by_night == 0)

        self.assertTrue(hasattr(self.my_model, "latitude"))
        self.assertTrue(self.my_model.latitude == 0.0)

        self.assertTrue(hasattr(self.my_model, "longitude"))
        self.assertTrue(self.my_model.longitude == 0.0)

        self.assertTrue(hasattr(self.my_model, "amenity_ids"))
        self.assertTrue(self.my_model.amenity_ids == [])

        self.assertIsInstance(self.my_model.id, str)

    def test_dictRepresentation(self):
        """test the to dict method"""
        self.my_model.id = 'fa5f7cec-e7e1-436f-ba49-35241277adac'
        self.my_model.city_id = 'last_name'
        self.my_model.user_id = 'first_name'
        self.my_model.number_rooms = 0
        self.my_model.latitude = 0.0
        self.my_model_json = self.my_model.to_dict()
        self.assertDictEqual(self.my_model_json, {
            'my_number': 89,
            'name': 'My First Model',
            '__class__': 'Place',
            'updated_at': self.my_model.updated_at.isoformat(),
            'created_at': self.my_model.created_at.isoformat(),
            'id': self.my_model.id,
            'city_id': 'last_name',
            'user_id': 'first_name',
            'number_rooms': 0,
            'latitude': 0.0
        })
