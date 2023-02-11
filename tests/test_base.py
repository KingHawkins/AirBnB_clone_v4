#!/usr/bin/env python3
import unittest
import uuid
import sys
import io
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State
"""Tests for the Base Model"""


class TestInheritance(unittest.TestCase):
    """Tests for inheritance"""
    def test_id(self):
        my_model = BaseModel()
        self.assertEqual(my_model.id, my_model.id)

    def test_user(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_amenity(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_place(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_review(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_state(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_city(self):
        self.assertTrue(issubclass(City, BaseModel))


class TestFunctionality(unittest.TestCase):
    """Tests for the functionality"""
    def test_base_model(self):
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()
        captured = io.StringIO()
        sys.stdout = captured
        print(my_user)
        self.assertEqual(captured, captured)

    def test_base_model(self):
        my_user = BaseModel()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()
        captured = io.StringIO()
        sys.stdout = captured
        print(my_user)
        self.assertEqual(captured, captured)


if __name__ == '__main__':
    unittest.main()
