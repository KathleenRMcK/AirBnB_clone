#!/usr/bin/python3
""" Init module """

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


storage = FileStorage()
storage.reload()
