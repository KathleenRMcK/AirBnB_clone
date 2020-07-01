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
        """ Deserializes the JSON file
        """
        try:
            with open(self.__file_path, "r") as file:
                list_of_dicts = json.loads(file.read())

            for obj_dict in list_of_dicts:
                if obj_dict['__class__'] == "BaseModel":
                    from models.base_model import BaseModel
                    self.new(BaseModel(**obj_dict))
                if obj_dict['__class__'] == "User":
                    from models.user import User
                    self.new(User(**obj_dict))
        except:
            pass
    """ Deserializes JSON to __objects if file exists """
        #try:
            #with open(self.__file_path, encoding="UTF8") as x:
                #for key, val in (json.load(x)).__objects.items():
                    """ Retrieving JSON for serialization """
                    #name_of_class = val["__class__"]
                    #name_of_class = models.classes[name_of_class]
                    #self.__objects[key] = name_of_class(**val)
                    """ Class selection for serialization """
        #except FileNotFoundError:
            """ If no file exists """
            #pass
