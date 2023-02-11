#!/usr/bin/env python3
import uuid
from models import storage
from datetime import datetime

"""Base model class"""


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initialize Base Model class
        Args:
            args(tuple): tuple argument. Won't be used here
            kwargs(dict): object dictionary passed
        Attributes:
            id: unique number for identification
            created_at: shows when the object was created
            updated_at: shows when the object was last updated
            storage.new(): engine for storage
        """
        if kwargs:
            for key in kwargs:
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        kwargs[key] = datetime.strptime(kwargs[key],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns string representation of an object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def __repr__(self):
        """returns official string representation"""
        return self.__str__()

    def save(self):
        """updates the object date"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values\
                of __dict__ instance"""
        objec = {}
        for key in self.__dict__:
            if key == 'created_at' or key == 'updated_at':
                objec[key] = self.__dict__[key].isoformat()
            else:
                objec[key] = self.__dict__[key]
        objec['__class__'] = self.__class__.__name__
        return objec
