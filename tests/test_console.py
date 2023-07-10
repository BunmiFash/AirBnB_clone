#!.usr/bin/python3

"""
Unittest cases for all methods in console.py
"""

import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


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
        output = "Quit command to exit the program\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue(), output)

    def test_help_EOF(self):
        """
        EOF documentation
        """
        output = "Cleanly exits from the interpreter\n"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue(), output)

    """
    TESTS FOR METHODS FUNCTIONALITY
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
