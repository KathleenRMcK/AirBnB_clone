# 0x00 - AirBnB Clone - The Console
##### Created for Holberton School - Foundations - Higher-level Programming

### Description

In this project, students create their first steps towards building the AirBnB clone. This is done by building a console to interpret desired commands and manage the objects of the AirBnB project. This console must be able to create new objects, retrieve objects, do operations on objects, update objects attributes and destroy objects.  
Below is a basic overview of the entire AirBnB project:

![Overview for AirBnB Project](/images/AirBnB_Overview.png)

### Installation
```
user$ git clone https://github.com/KathleenRMcK/AirBnB_clone.git
```

### Usage

Below is a list of the desired console commands and a simple overview on how to utilize the AirBnB console through examples with these commands. 

##### Console commands:
- quit - exits program
- EOF - exits program
- help - shows documented commands
- create - creates a new instance
- show - prints a string representation
- destroy - deletes an instance
- all - prints all string representation
- update - updates an instance 

This will launch the entry point of the command interpreter:
```
user$ ./console.py
(hbnb)
```

In this	example, the help command provides information on some commands:
```
(hbnb) help quit
Quit command to exit the program
```

In this example, the all command retrieves all instances of a class:  
(The same syntax can also be used with count, show and destroy.)
```
(hbnb) <class name>.all()
<class all>
```

In these examples, the update command is used to update based on the ID  
and then based on an ID with a dictionary:
```
(hbnb) <class name>.update(<id>, <attribute name>, <attribute value>)
```
```
(hbnb) <class name>.update(<id>, <dictionary representation>)
```

And finally, to close the interpreter, use the quit command below:
```
(hbnb) quit
user$
```

### Project Files

| Directory |  Project File   |         Description          |
|-----------|-----------------|------------------------------|
|   root    |  AUTHORS        | List of contributors |
|   root    |  console.py     | Entry point of the command interpreter |
|   models  | \_\_init\_\_.py | Initializes valid modules as packages |
|   models  |  amenity.py     | Amenity class that inherits from BaseModel |
|   models  | base_model.py   | BaseModel class to define all other classes |
|   models  |    city.py      | City class that inherits from BaseModel |
|   models  |    place.py     | Place class that inherits from BaseModel |
|   models  |   review.py     | Review class that inherits from BaseModel |
|   models  |    state.py     | State class that inherits from BaseModel |
|   models  |    user.py      | User class that inherits from BaseModel |
|   engine  | file_storage.py | Class that de/serializes from/to JSON file |
|   engine  | \_\_init\_\_.py | Initializes valid modules as packages |
|   tests   | test_console.py | Unittests for all console.py features |

### Authors
See [AUTHORS](https://github.com/KathleenRMcK/AirBnB_clone/blob/dev/AUTHORS) file for complete list of names and contact information for contributors