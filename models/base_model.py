#!/usr/bin/python3
"""
Base Model
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """ Base Model Class """
    def __init__(self, *args, **kwargs):
        """ intializes id, created_at, and updated_at instance vars """
        self.id = str(uuid.uuid4())
        self.updated_at = self.created_at = datetime.now()
        storage.new(self)

    def save(self):
        """ Saves current datetime to updated_at """
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """ String representation ofinstance """
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      self.__dict__))

    def to_dict(self):
        """
        function that return a dict containing key and value
        """
        dictionary = dict(**self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return (dictionary)
