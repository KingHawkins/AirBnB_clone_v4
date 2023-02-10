#!/usr/bin/python3
from models.base_model import BaseModel

"""Inherits basemodel"""


class User(BaseModel):
    """Implementation"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
