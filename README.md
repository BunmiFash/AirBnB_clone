# AIRBNB CONSOLE
![AirBnB clone](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230710%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230710T164550Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2ce453dbbe223961f1bc55d6e7c97b044d3f038b6866fd371b7e89b0aa99d06e)
This is the first part of the AirBnB project.
The following are the tasks carried out in the course of the project:
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances.
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
- create the first abstracted storage engine of the project: File storage. All objects are stored here.
- create all unittests to validate all our classes and storage engine.

## THE CONSOLE
A command interpreter is used to manipulate data without a visual ineterface.
Objects can be created, retreived, updated or deleted from the command line.

## USAGE
### To get started, execute the console.py file
```
$ ./console.py
(hbnb) 
```

### To view all available commands
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit create show destroy all update 

(hbnb) 
```

### To check out what each command does
```
$ ./console.py
(hbnb) help quit
Quit command to exit the program

(hbnb) 
```

## CONTRIBUTORS
[Fashina Blessing Oluwabunmi](https://https://github.com/BunmiFash)

[Daniel Komolafe](https://github.com/Daniel-418)