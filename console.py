#!/usr/bin/python3
"""
This module contains the command interpeter
for managing Airbnb files
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class that inherits from cmd.Cmd
    """
    prompt = '(airbnb) '

    def do_EOF(self, args):
        """
        EOF command exits out of the console
        """
        quit()
    def do_help(self, args):
        """
        list all commands
        """
        cmd.Cmd.do_help(self, args)


    def do_destroy(self, args):
        """
        Deletes an instance of the class name and id
        saves the changes inside JSON file
        """

    def do_all(self, args):
        """
        Prints all string representation of all instances
        """
    def do_count(self, args):
        """
        Counts number of instances
        """

    def do_create(self, args):
        """
        Creates a new instance of BaseModel and saves it inside JSON file

        """

    def do_update(self, args):
        """
        Update an instance based on the class name and id by adding
        or updating object
        """


    def do_show(self, args):
        """ show string representation of an instance"""


    def default(self, args):
        """
        default method to use with commands
        """


    def do_quit(self, args):
        """
        exits out of the console
        """
        quit()


    def emptyline(self):
        """
        Returns back to the prompt
        """
        return

if __name__ == "__main__":
    HBNBCommand().cmdloop()
