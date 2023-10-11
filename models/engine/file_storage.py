#!/usr/bin/python3

"""class FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances"""


class FileStorage:
    '''serializes instances to a JSON file and
    deserializes JSON file to instances'''

    __file_path = 'file.json'  # path to the JSON file
    __objects = {}  # store all objects

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

    # they are just like the ones in 0x0C-python-almost_a_circle/models/base.py
