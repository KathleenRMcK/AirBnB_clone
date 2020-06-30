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
        if len(args) > 0:
            datetime_string = args[0]['created_at']
            args[0]['created_at'] = (datetime.strptime(
                datetime_string, "%Y-%m-%d %H:%M:%S.%f"))
            update_datetime_string = args[0]['updated_at']
            args[0]['updated_at'] = (datetime.strptime(
                update_datetime_string, "%Y-%m-%d %H:%M:%S.%f"))
            self.__dict__ = args[0]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = (datetime.now())
            storage.new(self)
    def save(self):
        """ Saves current datetime to updated_at """
        self.updated_at = datetime.now()
        storage.save()
    def __str__(self):
        """ String representation ofinstance """
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      self.__dict__))
