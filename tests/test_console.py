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
        Prints all objects of a specified class
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

    def test_update(self):
        """
        Updates an object
        """
        all_objects = storage.all()
        key = "City.5739eadf-f300-4675-b13d-97c5fb3ebb63"
        val = all_objects[key].__dict__
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update City\
     5739eadf-f300-4675-b13d-97c5fb3ebb63 state 'Lagos'")
            self.assertIn('state', val)

    def test_default(self):
        """
        Tests for all commands
        """
        """
        all
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
            self.assertEqual(type(f.getvalue()), str)

        out = "** class doesn't exists **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("review.all()")
            self.assertEqual(f.getvalue(), out)

        """
        Test for count()
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual(type(f.getvalue()), str)

        out = "** class doesn't exists **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("review.count()")
            self.assertEqual(f.getvalue(), out)

        """
        show()
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "BaseModel.show('bb230126-8e70-47e6-8be8-16bfdb3ecd66')")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "User.show('2cf605e6-8082-41ff-b2cf-29632e0744cc')")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "State.show('1fc19385-b67d-430a-a696-a32fecdc5c51')")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "City.show('c60ee7b9-4c30-4aeb-afcf-96bda28e9d45')")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "Place.show('61881db5-c387-405b-940e-c5b41158eaa1')")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "Amenity.show('91371784-d2ed-44a1-aea1-743ab44b9c9f')")
            self.assertEqual(type(f.getvalue()), str)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "Review.show('28acf8ce-0142-4a8b-a7f1-64d84ba73ed2')")
            self.assertEqual(type(f.getvalue()), str)

        out1 = "** class doesn't exists **\n"
        out2 = "** instance id missing **\n"
        out3 = "** no instance found **\n"

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "review.show('28acf8ce-0142-4a8b-a7f1-64d84ba73ed2')")
            self.assertEqual(f.getvalue(), out1)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "Review.show()")
            self.assertEqual(f.getvalue(), out2)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "Review.show('1234')")
            self.assertEqual(f.getvalue(), out3)

        """
        destroy()
        """
        out1 = "** class doesn't exists **\n"
        out2 = "** instance id missing **\n"
        out3 = "** no instance found **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "BaseModel.destroy('bb230126-8e70-47e6-8be8-16bfdb3ecd66')"
                )
            self.assertEqual(f.getvalue(), out3)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "User.destroy('2cf605e6-8082-41ff-b2cf-29632e0744cc')"
                )
            self.assertEqual(f.getvalue(), out3)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "State.destroy('1fc19385-b67d-430a-a696-a32fecdc5c51')"
                )
            self.assertEqual(f.getvalue(), out3)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "City.destroy('c60ee7b9-4c30-4aeb-afcf-96bda28e9d45')"
                )
            self.assertEqual(f.getvalue(), out3)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "Place.destroy('61881db5-c387-405b-940e-c5b41158eaa1')"
                )
            self.assertEqual(f.getvalue(), out3)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "Amenity.destroy('91371784-d2ed-44a1-aea1-743ab44b9c9f')"
                )
            self.assertEqual(f.getvalue(), out3)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "Review.destroy('28acf8ce-0142-4a8b-a7f1-64d84ba73ed2')")
            self.assertEqual(f.getvalue(), out3)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "review.destroy('28acf8ce-0142-4a8b-a7f1-64d84ba73ed2')")
            self.assertEqual(f.getvalue(), out1)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "Review.destroy()")
            self.assertEqual(f.getvalue(), out2)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                "Review.destroy('1234')")
            self.assertEqual(f.getvalue(), out3)

        """
        update()
        """
        all_objects = storage.all()

        key = "Review.28acf8ce-0142-4a8b-a7f1-64d84ba73ed2"
        val = all_objects[key].__dict__
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                'Review.update("28acf8ce-0142-4a8b-a7f1-64d84ba73ed2",\
     "stars", "five")')
            self.assertIn('stars', val)

        key = "Place.61881db5-c387-405b-940e-c5b41158eaa1"
        val = all_objects[key].__dict__
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                'Place.update("61881db5-c387-405b-940e-c5b41158eaa1",\
     "loc", "kwara")')
            self.assertIn('loc', val)

        key = "City.5739eadf-f300-4675-b13d-97c5fb3ebb63"
        val = all_objects[key].__dict__
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                'City.update("5739eadf-f300-4675-b13d-97c5fb3ebb63",\
     "area", "LCDA")')
            self.assertIn('area', val)

        key = "State.1fc19385-b67d-430a-a696-a32fecdc5c51"
        val = all_objects[key].__dict__
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                'State.update("1fc19385-b67d-430a-a696-a32fecdc5c51",\
     "state", "Anambra")')
            self.assertIn("state", val)

        key = "Amenity.1da41a05-066f-48a8-8919-386d58dd87cc"
        val = all_objects[key].__dict__
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                'Amenity.update("1da41a05-066f-48a8-8919-386d58dd87cc",\
     "stars", "two")')
            self.assertIn('stars', val)

        key = "BaseModel.f745a0ff-4224-43e0-abbb-e58deded2f1a"
        val = all_objects[key].__dict__
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                'BaseModel.update("f745a0ff-4224-43e0-abbb-e58deded2f1a",\
     "level", "two")')
            self.assertIn('level', val)

        key = "User.64cb6f28-240a-4b86-96e4-d0231057bcbe"
        val = all_objects[key].__dict__
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(
                'User.update("64cb6f28-240a-4b86-96e4-d0231057bcbe",\
     "last_name", "Eva")')
            self.assertIn('last_name', val)

    def test_pep8_console(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
