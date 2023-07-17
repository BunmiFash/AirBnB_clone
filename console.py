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
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """
        Cleanly exits from the interpreter
        """
        return (True)

    def help_EOF(line):
        """
        Help message for EOF()
        """
        print("Cleanly exits from the interpreter\n")

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
              " and save it to a json file\n")

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
        print("prints the string representation of the specified instance\n")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        and saves changes to storage
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
                del objects_dict[search_key]
                storage.save()
            else:
                print("** no instance found **")

    def help_destroy(line):
        """
        prints the help method for the "destroy" command
        """
        print("Usage: destroy <class_name> <id>")
        print("Removes the specified class\n")

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
                attr_name = arguments[2]
                val_type = type(arguments[3])
                attr_value = val_type(arguments[3])
                obj_dict = objects_dict[search_key].__dict__
                value = arguments[3].strip('"')
                obj_dict[attr_name] = attr_value
                storage.save()

    def help_update(line):
        """
        prints help method for the update command
        """
        print("Usage: update <class name> <id> <attribute name>"
              " \"<attribute value>\"")
        print("Updates an instance of class_name and id by adding"
              " or updating attribute\n")

    def do_all(self, line):
        arguments = line.split() if line else []
        objects_dict = storage.all()
        all = []
        if not arguments:
            for val in objects_dict.values():
                all.append(str(val))
            if len(all) >= 1:
                print(all)
        else:
            if arguments[0] not in self.__classes:
                print("** class doesn't exist **")
            for val in storage.all().values():
                if arguments[0] == val.to_dict()["__class__"]:
                    all.append(str(val))
            if len(all) >= 1:
                print(all)

    def help_all(line):
        """
        Prints the message for the "all" command
        """
        print("Usage <all> <class_name>")
        print("prints all the instances of class_names"
              " or all the instances stored if no argument"
              " is provided\n")

    def default(self, line):
        """
        Method called when a command is not
        used a s first argument
        """
        all = []
        args = line.split(".") if line else []
        objects_dict = storage.all()
        try:
            cls = args[0]
            if len(args) > 1:
                comd = args[1]
            if cls not in self.__classes:
                print("** class doesn't exists **")
            elif comd == "all()":
                self.do_all(cls)
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
                if comd == "show":
                    self.do_show("{} {}".format(cls, obj_id))
                elif comd == "destroy":
                    self.do_destroy("{} {}".format(cls, obj_id))

            elif comd.startswith("update"):
                args = comd.split("(")
                comd = args[0]
                update_args = args[1].split(")")[0].split(", ")
                obj_id = update_args[0].strip('"')
                if len(update_args) == 2 and update_args[1].startswith("{"):
                    attr_dict = eval(update_args[1])
                    for key, value in attr_dict:
                        self.do_update("{} {} {} {}".format(
                            cls, obj_id, key, value))
                else:
                    attr_name = update_args[1].strip('"')
                    attr_value = update_args[2].strip('"')
                    self.do_update("{} {} {} {}".format(
                        cls, obj_id, attr_name, attr_value))
        except IndexError:
            print("Invalid!")

    def emptyline(self):
        """Does Nothing"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
