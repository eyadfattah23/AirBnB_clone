#!/usr/bin/python3

"""Define a class BaseModel:
defines all common attributes/methods for other classes"""
import uuid
import datetime


class BaseModel():
    '''defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        """initializes a new BaseModel object"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'updated_at' or k == 'created_at':
                    setattr(self, k, datetime.datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            from models import storage
            storage.new(self)

    def __str__(self):
        """string representation of BaseModel
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''updates the public instance attribute
        updated_at with the current datetime'''
        from models import storage

        self.updated_at = datetime.datetime.utcnow()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': self.__class__.__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
