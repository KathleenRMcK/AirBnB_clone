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
#import models
#from models.base_model import BaseModel
#from models.user import User
#from datetime import datetime
#from models.city import City
#from models.state import State
#from models.amenity import Amenity
#from models.place import Place
#from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class that inherits from cmd.Cmd
    """
    prompt = '(hbnb) '

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
        token = args.split()
        all_instances = []
        instances = storage.all()
        if len(token) > 1:
            if token[0] in self.classes:
                for x in instances:
                    if x[0:len(token[0])] == token[0]:
                        all_instances.append(instances[x])
                print(all_instances)
            else:
                print("** class doesn't exist **")
                return
        if len(token) > 1:
            for x in instances:
                all_instances.append(instances[x])
            print(all_instances)

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
