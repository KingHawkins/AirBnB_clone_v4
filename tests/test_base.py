#!/usr/bin/env python3
import unittest
import uuid
from models.base_model import BaseModel
"""Tests for the Base Model"""

class TestBase(unittest.TestCase):
    """Tests for functionality of the BaseModel class"""
    def test_id(self):
        my_model = BaseModel()
        self.assertEqual(my_model.id, my_model.id)

    def kwargs(self):
        """Tests the dictionary instantiation as a parameter"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        print(my_model.id)
        print(my_model)
        print(type(my_model.created_at))
        print("--")
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

        print("--")
        my_new_model = BaseModel(**my_model_json)
