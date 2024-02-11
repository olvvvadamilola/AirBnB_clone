#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

from models.engine.file_storage import FileStorage

"""base class for all models"""
storage = FileStorage()
storage.reload()
