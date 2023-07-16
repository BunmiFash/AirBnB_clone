#!/usr/bin/python3

"""
Command line interpreter for AirBnB
"""
from models.base_model import BaseModel
from models.place import Place
import cmd
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand
    """
    prompt = "(hbnb) "

    """ dict containing all the possible classes to be created """
    __classes = {'BaseModel': BaseModel, 'Place': Place,
                 'User': User, 'State': State,
                 'City': City, 'Amenity': Amenity,
                 'Review': Review}

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return (True)

    def help_quit(line):
        """
        Help message for quit()
        """
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """
        Cleanly exits from the interpreter
        """
        return (True)

    def help_EOF(line):
        """
        Help message for EOF()
        """
        print("Cleanly exits from the interpreter")

    def do_create(self, line):
        """
        Creates a new instance of BaseModel and saves it
        to a JSON file
        """
        if line:
            if line in self.__classes:
                new_object = self.__classes[line]()
                new_object.save()
                print("{}".format(new_object.id))
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(line):
        """
        Help message for the "create" command
        """
        print("Usage: create <class_name>")
        print("creates an object specified by class_name"
              " and save it to a json file")

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        arguments = line.split() if line else []
        if not arguments:
            print("** class name missing **")
        elif arguments[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arguments) != 2:
            print("** instance id missing **")
        else:
            objects_dict = storage.all()
            search_key = arguments[0] + "." + arguments[1]
            if (search_key in objects_dict):
                print(objects_dict[search_key])
            else:
                print("** no instance found **")

    def help_show(line):
        """
        Prints the help message for the "show" command
        """
        print("Usage: show <class_name> <id>")
        print("prints the string representation of the specified instance")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        and saves changes to storage
        """
        arguments = line.split() if line else []
        if not arguments:
            print("** class name missing **")
        elif arguments[0] not in self.__classes:
            print("** class doen't exist")
        elif len(arguments) != 2:
            print("** instance id missing **")
        else:
            objects_dict = storage.all()
            search_key = arguments[0] + "." + arguments[1]
            if (search_key in objects_dict):
                del objects_dict[search_key]
                storage.save()
            else:
                print("** no instance found **")

    def help_destroy(line):
        """
        prints the help method for the "destroy" command
        """
        print("Usage: destroy <class_name> <id>")
        print("Removes the specified class")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        arguments = line.split() if line else []
        if not arguments:
            print("** class name missing **")
        elif arguments[0] not in self.__classes:
            print("** class doesn't exist")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            objects_dict = storage.all()
            search_key = arguments[0] + "." + arguments[1]
            if search_key not in objects_dict:
                print("** no instance found **")
            elif len(arguments) == 2:
                print("** attribute name missing **")
            elif len(arguments) == 3:
                print("** value missing **")
            else:
                valType = type(arguments[3])
                obj_dict = objects_dict[search_key].__dict__
                value = arguments[3].strip('"')
                obj_dict[arguments[2]] = valType(value)
                storage.save()

    def help_update(line):
        """
        prints help method for the update command
        """
        print("Usage: update <class name> <id> <attribute name>"
              " \"<attribute value>\"")
        print("Updates an instance of class_name and id by adding"
              " or updating attribute")

    def do_all(self, line):
        arguments = line.split() if line else []
        objects_dict = storage.all()
        all = []
        if not arguments:
            for val in objects_dict.values():
                all.append(str(val))
            print(all)
        else:
            if arguments[0] not in self.__classes:
                print("** class doesn't exist **")
            for val in storage.all().values():
                if arguments[0] == val.to_dict()["__class__"]:
                    all.append(str(val))
        print(all)

    def help_all(line):
        """
        Prints the message for the "all" command
        """
        print("Usage <all> <class_name>")
        print("prints all the instances of class_names"
              " or all the instances stored if no argument"
              " is provided")

    def default(self, line):
        """
        Method called when a command is not
        used a s first argument
        """
        all = []
        args = line.split(".") if line else []
        objects_dict = storage.all()
        cls = args[0]
        comd = args[1]
        if cls not in self.__classes:
            print("** class doesn't exists **")
        elif comd == "all":
            for value in objects_dict.values():
                val = value.to_dict()
                if cls == val["__class__"]:
                    all.append(value)
            if len(all) >= 1:
                print("[", end="")
                for idx in range(len(all)):
                    print(all[idx], end="")
                    if idx != len(all) - 1:
                        print(", ", end="")
                    else:
                        print("]")
        elif comd == "count()":
            count = 0
            for value in objects_dict.values():
                val = value.to_dict()
                if cls == val["__class__"]:
                    count += 1
            print(count)
        elif comd.startswith("show") or comd.startswith("destroy"):
            args = comd.split("(")
            comd = args[0]
            args = args[1].split(")")
            obj_id = args[0].strip('"').strip(")").strip('"')
            search_key = "{}.{}".format(cls, obj_id)
            if search_key not in objects_dict:
                print("** no instance found **")
            else:
                if comd == "show":
                    print(objects_dict[search_key])
                elif comd == "destroy":
                    del objects_dict[search_key]
                    storage.save()

    def emptyline(self):
        """Does Nothing"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
