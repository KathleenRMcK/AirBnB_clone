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
# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Entry point class begins here
    """
    prompt = "(hbnb) "
#    item = [BaseModel, User, State, City, Amenity, Place, Review]

    def do_quit(self, line):
        """ Allows use of quit command to exit program """
        return True

    def do_EOF(self, line):
        """ Allows use of EOF command to exit program """
        return True

    def emptyline(self):
        """ Allows empty line + ENTER to provide blank space """
        pass

    """
    ***Help support documentation for all commands***
    """
    def help_create(self):
        """ Documentation for the create command """
        print 'Use of the create command creates a new instance of BaseModel, saves it to JSON file and prints the id with: create <class name>'
    def help_show(self):
        """ Documentation for the show command """
        print 'Use of the show command retrieves an instance based on its ID with: <class name>.show(<id>)'
    def help_count(self):
        """ Documentation for the count command """
        print 'Use of the count command retrieves the number of instances of a class with: <class name>.count()'
    def help_destroy(self):
        """ Documentation for the destroy command """
        print 'Use of the destroy command destroys an instance based on its ID with: <class name>.destroy(<id>)'
    def help_all(self):
        """ Documentation for the all command """
        print 'Use of the all command retrieves all instances of a class with: <class name>.all()'
    def help_update(self):
        """ Documentation for the update command """
        print 'Use of the update command updates an instance based on its ID with: <class name>.update(<id>, <attribute name>, <attribute value>) and with a dictionary using: <class name>.update(<id>, <dictionary representation>)'

if __name__ == '__main__':
    HBNBCommand().cmdloop()
