#!/usr/bin/python3
"""
This module contains all unittest cases for
Base class
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
import sys
from io import StringIO
import json
import os


class TestRectangle(unittest.TestCase):
    """
    Class containing functions to run
    multiple tests
    """
    def setUp(self):
        """
        function to redirect stdout to check
        outpute of functions relying on print
        """
        sys.stdout = StringIO()

    def tearDown(self):
        """
        cleans everything up after running
        setup
        """
        sys.stdout = sys.__stdout__

    def test_pep8_model(self):
        """
        Tests for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/rectangle.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """
        Tests for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_00_documentation(self):
        """
        Test to see if documentation is
        created and correct
        """
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(hasattr(Rectangle, "width"))
        self.assertTrue(Rectangle.width.__doc__)
        self.assertTrue(hasattr(Rectangle, "height"))
        self.assertTrue(Rectangle.height.__doc__)
        self.assertTrue(hasattr(Rectangle, "x"))
        self.assertTrue(Rectangle.x.__doc__)
        self.assertTrue(hasattr(Rectangle, "y"))
        self.assertTrue(Rectangle.y.__doc__)
        self.assertTrue(hasattr(Rectangle, "area"))
        self.assertTrue(Rectangle.area.__doc__)
        self.assertTrue(hasattr(Rectangle, "display"))
        self.assertTrue(Rectangle.display.__doc__)
        self.assertTrue(hasattr(Rectangle, "__str__"))
        self.assertTrue(Rectangle.__str__.__doc__)
        self.assertTrue(hasattr(Rectangle, "update"))
        self.assertTrue(Rectangle.update.__doc__)
        self.assertTrue(hasattr(Rectangle, "to_dictionary"))
        self.assertTrue(Rectangle.to_dictionary.__doc__)

    def test_0_id(self):
        """
        Tests for id
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(10, 11)
        R2 = Rectangle(11, 12, 13)
        R3 = Rectangle(12, 13, 14, 15)
        R6 = Rectangle(13, 14, 15, 16, 5)
        R4 = Rectangle(2, 4, 5, 6, 7)
        R5 = Rectangle(3, 45, 4, 2, id="10")
        self.assertEqual(R1.id, 1)
        self.assertEqual(R2.id, 2)
        self.assertEqual(R3.id, 3)
        self.assertEqual(R6.id, 5)
        self.assertEqual(R4.id, 7)
        self.assertEqual(R5.id, "10")

    def test_1_arg(self):
        """
        Test for checking numbers of
        objects
        """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Rectangle(10)
            Rectangle()
            Rectangle(x=10, y=20)
