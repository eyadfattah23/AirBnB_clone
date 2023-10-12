from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


import unittest


"""define test class to test the json file storage,
FileStorage class and
storage instance"""


class FileStorageTestCase(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        # Remove the file.json after each test
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_all(self):
        # Assert that the initial all() method returns an empty dictionary
        self.assertEqual(self.storage.all(), {})

        # Add an object to the storage and assert that all() returns the object
        self.storage.new(self.base_model)
        self.assertEqual(self.storage.all(), {
            'BaseModel.{}'.format(self.base_model.id): self.base_model
        })

    def test_new(self):
        # Assert that new() adds the object to the __objects dictionary
        self.storage.new(self.base_model)
        self.assertEqual(self.storage.all(), {
            'BaseModel.{}'.format(self.base_model.id): self.base_model
        })

    def test_save_reload(self):
        # Save the object to the file
        self.storage.new(self.base_model)
        self.storage.save()

        # Reload the objects from the file and assert that they match the original object
        self.storage.reload()
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects['BaseModel.{}'.format(
            self.base_model.id)].to_dict(), self.base_model.to_dict())
