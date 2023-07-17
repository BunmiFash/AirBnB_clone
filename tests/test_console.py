#!.usr/bin/python3

"""
Unittest cases for all methods in console.py
"""

import unittest
from console import HBNBCommand
from io import StringIO
import pep8
from unittest.mock import patch
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """
    Test cases for console.py
    """
    """
    ALL METHOD DOCUMENTATION TESTS
    """
    def test_help_quit(self):
        """
        Quit documentation
        """
        output = "Quit command to exit the program\n\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue(), output)

    def test_help_EOF(self):
        """
        EOF documentation
        """
        output = "Cleanly exits from the interpreter\n\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue(), output)

    def test_help_create(self):
        """
        create command doc
        """
        out = "Usage: create <class_name>\n"
        out2 = "creates an object specified by class_name\
 and save it to a json file\n\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue(), out + out2)

    def test_help_show(self):
        """
        show command doc
        """
        out = "Usage: show <class_name> <id>\n"
        out2 = "prints the string representation of\
 the specified instance\n\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue(), out + out2)

    def test_help_destroy(self):
        """
        destroy command doc
        """
        out = "Usage: destroy <class_name> <id>\n"
        out2 = "Removes the specified class\n\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(f.getvalue(), out + out2)

    def test_help_update(self):
        """
        update command doc
        """
        out = 'Usage: update <class name> <id>\
 <attribute name> "<attribute value>"\n'
        out2 = "Updates an instance of class_name and id by\
 adding or updating attribute\n\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(f.getvalue(), out + out2)

    def test_help_all(self):
        """
        all command doc
        """
        out = 'Usage <all> <class_name>\n'
        out2 = "prints all the instances of class_names\
 or all the instances stored if no argument is provided\n\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(f.getvalue(), out + out2)

    """
    TESTS FOR COMMANDS FUNCTIONALITY
    """
    def test_emptyline(self):
        """
        Test for emptyline()
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_quit(self):
        """
        Test for quit()
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        """
        Test for EOF()
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        """
        Creates a new object
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertEqual(type(f.getvalue()), str)

        """
        Checks arguments passed
        """
        out = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), out)

        out = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create hello")
            self.assertEqual(f.getvalue(), out)

    def test_show(self):
        """
        Prints the string representation of an objects
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "show BaseModel 3ac2441a-7187-4321-8e95-d0f847414eec"
                )
            self.assertEqual(type(f.getvalue()), str)

        """
        Checks arguments passed
        """
        out = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), out)

        out = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show hello")
            self.assertEqual(f.getvalue(), out)

        out = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "show hello 2cf605e6-8082-41ff-b2cf-29632e0744cc"
                )
            self.assertEqual(f.getvalue(), out)

        out = "** instance id missing **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue(), out)

        out = "** no instance found **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show User 2345")
            self.assertEqual(f.getvalue(), out)

    def test_destroy(self):
        """
        Deletes an object
        """

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "destroy BaseModel d63d61ec-0e35-43df-8269-3d12861392c1"
                )
        """
        Checks arguments passed
        """
        out = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue(), out)

        out = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy hello")
            self.assertEqual(f.getvalue(), out)

        out = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "destroy hello 2cf605e6-8082-41ff-b2cf-29632e0744cc"
                )
            self.assertEqual(f.getvalue(), out)

        out = "** instance id missing **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual(f.getvalue(), out)

        out = "** no instance found **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 2345")
            self.assertEqual(f.getvalue(), out)

        """
        To check for an already deleted object
        """
        out = "** no instance found **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "destroy BaseModel d63d61ec-0e35-43df-8269-3d12861392c1"
                )
            self.assertEqual(f.getvalue(), out)

    def test_all(self):
        """
        Prints all objects orobjects of a specified class
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertEqual(type(f.getvalue()), str)

        """
        Checks arguments passed
        """
        out = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all hello")
            self.assertEqual(f.getvalue(), out)

        out = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all user")
            self.assertEqual(f.getvalue(), out)

    def test_pep8_console(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
