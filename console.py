#!/usr/bin/python3

"""
Command line interpreter for AirBnB
"""
from models.base_model import BaseModel
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand
    """
    prompt = "(hbnb) "

    """ dict containing all the possible classes to be created """
    __classes = {'BaseModel': BaseModel}

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
                print("{}".format(
                    self.__classes[arguments[0]](**objects_dict[search_key])
                    ))
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
        elif len(arguments) == 2:
            print("** attribute name missing **")
        elif len(arguments) == 3:
            print("** value missin **")
        else:
            objects_dict = storage.all()
            search_key = arguments[0] + "." + arguments[1]
            if search_key in objects_dict:
                objects_dict[search_key][arguments[2]] = eval(arguments[3])
                storage.save()
                print("update successful")
            else:
                print("** no instance found **")

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
        is_class_printed = False

        if not arguments:
            for idx, (key, value) in enumerate(objects_dict.items()):
                class_name = key.split(".")[0]
                instance = self.__classes[class_name](**value)
                print("{}".format(instance), end="")
                if idx != len(objects_dict) - 1:
                    print(", ", end="")
                else:
                    print()
        else:
            search_key = arguments[0]

            for idx, (key, value) in enumerate(objects_dict.items()):
                class_name = key.split(".")[0]

                if class_name == search_key:
                    is_class_printed = True
                    instance = self.__classes[class_name](**value)
                    print("{}".format(instance), end="")

                    if idx != len(objects_dict) - 1:
                        print(", ", end="")
                    else:
                        print()

            if not is_class_printed:
                print("** no instance found **")

    def help_all(line):
        """
        Prints the message for the "all" command
        """
        print("Usage <all> <class_name>")
        print("prints all the instances of class_names"
              " or all the instances stored if no argument"
              " is provided")

    def emptyline(self):
        """Does Nothing"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
