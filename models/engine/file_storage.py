#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
import importlib


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initializes the storage"""
        pass

    def all(self):
        """Returns a dictionary of models in JSON format"""
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        ser_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(ser_obj, file)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    module = importlib.import_module('models.' + class_name)
                    class_ = getattr(module, class_name)
                    self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass
