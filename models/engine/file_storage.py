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
        """ Serializes __objects to JSON file """
        obj_dict = {}
        for key, val in self.__objects.items():
            obj_dict[key] = val.to_dict()
        with open(self.__file_path, mode='w', encoding="UTF8") as x:
            """ Saves by writing """
            json.dump(obj_dict, x)
            """ Send dictionary to JSON """

    def reload(self):
        """ Reload """
        if (os.path.isfile(self.__file_path) is True):
            try:
                with open(self.__file_path, 'r') as file:
                    FileStorage.__objects = json.load(file)
            except:
                pass
