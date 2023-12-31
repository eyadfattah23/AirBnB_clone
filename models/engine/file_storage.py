#!/usr/bin/python3


"""class FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances"""

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''serializes instances to a JSON file and
    deserializes JSON file to instances'''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
            obj (BaseModel): the value of the object to add to __objects
        """
        if obj:
            FileStorage.__objects.update(
                {f'{obj.__class__.__name__}.{obj.id}': obj})

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        import json

        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, 'w+') as f:
            json.dump(dictionary, f)

    def reload(self):
        '''deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)'''
        import json
        dictionary = {}
        try:
            with open(self.__file_path, 'r+') as f:
                dictionary = json.load(f)
            for key, value in dictionary.items():
                class_name = dictionary[key]['__class__']
                self.__objects.update(
                    {key: eval(class_name)(**value)})

        except Exception as e:
            pass
