#!/usr/bin/python3
"""Base model"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all models
    """
    def __init__(self, *args, **kwargs):
        """Initialize Basemodel instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        """updates updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary repr. of a BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict.update({"__class__": self.__class__.__name__})
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
