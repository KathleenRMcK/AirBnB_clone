#!/usr/bin/python3
# console.py - Entry point of the command interpreter
# Requirements:
# Must use cmd module
# Class definition must be: class HBNBCommand(cmd.Cmd):
# Command interpreter must implement:
#     - quit and EOF to exit program
#     - help (provided by cmd by default, but should be updated)
#     - custom prompt: (hbnb)
#     - an empty line + ENTER shouldn't execute
# Code should not be executed when imported

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
    prompt = '(hbnb) '

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
        tokens = args.split()
        if tokens[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        if len(tokens) < 1:
            print("** class name missing **")
            return
        key = tokens[0] + "." + tokens[1]
        if key in BaseModelStorage:
            BaseModelStorage.all().pop(key)
            """ use .save """
            return
        else:
            print("** no instance found **")

    def do_create(self, args):
        """
        Creates a new instance of BaseModel and saves it inside JSON flie
        """
        tokens = args.split()
        if len(tokens) < 1:
            print("** class name missing **")
            return
        if tokens[0] in HBNBCommand.classes:
            if tokens[0] in HBNBCommand.classes:
                if tokens[0] == "BaseModel":
                    create_model = BaseModel()
                if tokens[0] == "User":
                    create__model = User()
                if tokens[0] == "State":
                    create__model = State()
                if tokens[0] == "Amenity":
                    create_model = Amenity()
                if tokens[0] == "Review":
                    create_model = Review()
                if tokens[0] == "Place":
                    create_model = Place()
                if tokens[0] == "City":
                    create_model = City()
                model.save()
                print(create_model.id)

        else:
            print("** class doesn't exist **")



    def do_all(self, args):
        """
        Prints all string representation of all instances
        """
    def do_count(self, args):
        """
        Counts number of instances
        """


    def do_update(self, args):
        """
        Update an instance based on the class name and id by adding
        or updating object
        """


    def do_show(self, args):
        """ show string representation of an instance"""
        tokens = args.split()
        if tokens[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            if len(args[0]) != 36:
                print("** instance id missing **")
            return
        if len(tokens) < 1:
            print("** class name missing **")
            return
        key = tokens[0] + "." + tokens[1]
        if key in BaseModelStorage:
            print()
            return
        else:
            print("** no instance found **")


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
        prints prompt
        """
        return

if __name__ == "__main__":
    HBNBCommand().cmdloop()
