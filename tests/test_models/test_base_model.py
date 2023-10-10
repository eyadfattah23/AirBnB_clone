#!/usr/bin/python3
from models.base_model import BaseModel

import unittest

"""define test class to test base model"""


class TestModel(unittest.TestCase):
    """test class for testing BaseModel"""

    def setUpModule():
        """set up module"""
        print("setup module")

    def tearDownModule():
        """tear down module"""
        print("teardown module")
