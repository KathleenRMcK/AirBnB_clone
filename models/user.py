#!/usr/bin/python3
"""
user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    user class
    Update FileStorage to manage correctly serialization and deserialization
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
