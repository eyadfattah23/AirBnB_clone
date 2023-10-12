#!/usr/bin/python3

"""class FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances"""

from models.base_model import BaseModel


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

    def reload(self):
        '''deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)'''
        import json
        dictionary = {}
        try:
            with open(self.__file_path, 'r+') as f:
                dictionary = json.load(f)  # 1
            for key, value in dictionary.items():   # 2
                self.__objects.update({key: BaseModel(**value)})    # 3

                '''
                1--> we got a dictionary like this from 'file.json':
                        {"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {
                            "my_number": 89,
                            "__class__": "BaseModel",
                            "updated_at": "2017-09-28T21:07:25.047381",
                            "created_at": "2017-09-28T21:07:25.047372",
                            "name": "My_First_Model",
                            "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
                2--> we go over the dictionary
                    with key ="BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d"
                    and value = {
                            "my_number": 89,
                            "__class__": "BaseModel",
                            "updated_at": "2017-09-28T21:07:25.047381",
                            "created_at": "2017-09-28T21:07:25.047372",
                            "name": "My_First_Model",
                            "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}

                3--> create instances using value as kwargs
                    and add those instances
                    using the right format to __objects
                '''
        except Exception as e:
            pass
    # they are just like the ones in 0x0C-python-almost_a_circle/models/base.py
