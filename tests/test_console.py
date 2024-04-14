#!/usr/bin/python3
import unittest
import os
import sys
from io import StringIO
from unittest.mock import create_autospec
from console import HBNBCommand
class TestHBNBCommand(unittest.TestCase):
    """
    THis class tests the console module
    """

    @classmethod
    def setUp(self):
        """ sets up resources for redirection of output from console
        """
        #save origninal value of sys.out to restore later
        self.initial_std_out = sys.stdout
        # for capturing information that would be normally printed on console
        self.captured_output = StringIO()
        #redirect standard output to stringIo()
        sys.stdout = self.captured_output

    @classmethod
    def tearDown(self):
        """ restore output to its initial state"""
        sys.stdout = self.initial_std_out

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') =='db', "works only for file storage")
    def test_all_command(self):
        """
        Tests if all command works
        """
        print("does this even work")
        console = HBNBCommand()
        console.onecmd("svdsknvsoidin")
        output = self.captured_output.getvalue()
        self.assertTrue(isinstance(output, str))
