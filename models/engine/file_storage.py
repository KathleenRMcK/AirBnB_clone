#!/usr/bin/python3
"""
Defination of class FileStorage to convert dictionary representations
to a JSON string and use the de/serialization process
"""
import json
import models
import os


class FileStorage():
    """ Class that serializes instances to JSON file
    and deserializes JSON to instance """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary: __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ serializes objects
        """
        object_dicts = []
        for key, value in self.__objects.items():
            object_dicts.append(value.to_dict())
        with open(self.__file_path, "w+") as file:
            file.write(json.dumps(object_dicts))

    def reload(self):
        """ Deserializes the JSON file
        """
        try:
            with open(self.__file_path, "r") as file:
                list_of_dicts = json.loads(file.read())
        except:
            pass
