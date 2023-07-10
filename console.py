#!/usr/bin/python3

"""
Command line interpreter for AirBnB
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand
    """
    prompt = "(hbnb) "

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

    def emptyline(self):
        """Does Nothing"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
