#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        ser_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(ser_obj, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    module = __import__('models.' + class_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass
