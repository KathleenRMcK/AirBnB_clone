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
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class that inherits from cmd.Cmd
    """
    prompt = '(hbnb) '
    all_classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def do_quit(self, line):
        """ Allows use of quit command to exit program """
        return True

    def do_EOF(self, line):
        """ Allows use of EOF command to exit program """
        return True

    def emptyline(self):
        """ Allows empty line + ENTER to provide blank space """
        pass

    def do_help(self, args):
        """
        list all commands
        """
        cmd.Cmd.do_help(self, args)

    """
    ***Help support documentation for all commands***
    """
    def help_create(self):
        """ Documentation for the create command """
        print('Use of the create command creates a new instance of BaseModel, saves it to JSON file and prints the id with: create <class name>')
    def help_show(self):
        """ Documentation for the show command """
        print('Use of the show command retrieves an instance based on its ID with: <class name>.show(<id>)')
    def help_count(self):
        """ Documentation for the count command """
        print('Use of the count command retrieves the number of instances of a class with: <class name>.count()')
    def help_destroy(self):
        """ Documentation for the destroy command """
        print('Use of the destroy command destroys an instance based on its ID with: <class name>.destroy(<id>)')
    def help_all(self):
        """ Documentation for the all command """
        print('Use of the all command retrieves all instances of a class with: <class name>.all()')
    def help_update(self):
        """ Documentation for the update command """
        print('Use of the update command updates an instance based on its ID with: <class name>.update(<id>, <attribute name>, <attribute value>) and with a dictionary using: <class name>.update(<id>, <dictionary representation>)')


    def do_destroy(self, args):
        """
        Deletes an instance of the class name and id
        saves the changes inside JSON file
        """
        tokens = args.split()
        stored_keys = storage.all()
        if tokens[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        if len(tokens) < 1:
            print("** class name missing **")
            return
        key = tokens[0] + "." + tokens[1]
        if key in stored_keys.keys():
            stored_keys.pop(key)
            storage.save()
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
        if tokens[0] in HBNBCommand.all_classes:
            new_model = HBNBCommand.all_classes[tokens[0]]()
            storage.new(new_model)
            storage.save()
            print(new_model.id)

    def do_all(self, args):
        """
        Prints all string representation of all instances
        """
        token = args.split()
        all_instances = []
        if len(token) < 1:
            for x in storage.all().values():
                all_instances.append(str(x))
            print(all_instances)
        else:
            classes = HBNBCommand.classes
            if token[0] not in classes:
                print("** class doesn't exist **")
                return
            for x in storage.all().keys():
                if x[0:len(token[0])] == token[0]:
                    all_instances.append(str(storage.all()[x]))
            print(all_instances)

    def do_count(self, args):
        """ Counts number of instances of a class """
        count_help = 0
        try:
            class_list = split(line, " ")
            if class_list[0] not in self.all_classes:
                print("** class doesn't exist **")
            obj = storage.all()
            for key in obj:
                key_help = key.split('.')
                if key_help[0] == class_list[0]:
                    count_help += 1
            print(count_help)

    def do_update(self, args):
        """ Update an instance based on the class name and id by adding
        or updating object """
        class_list = split(line, " ")
        obj = storage.all()
        key =
        val = obj[key]


    def do_show(self, args):
        """ show string representation of an instance"""
        tokens = args.split()
        stored_keys = storage.all()
        if len(tokens) < 1:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(tokens) > 1:
            key = tokens[0] + "." + tokens[1]
            if key in stored_keys:
                show_output = stored_keys[key]
            print(show_output)
            if key not in stored_keys:
                print("** instance id missing **")
        else:
            print("** no instance found **")


    def default(self, args):
        """
        default method to use with commands
        """


if __name__ == "__main__":
    HBNBCommand().cmdloop()
