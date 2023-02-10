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
