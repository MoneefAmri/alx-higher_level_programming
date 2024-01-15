#!/usr/bin/python3
"""
Module class Base
"""
import json


class Base:
    """
    Base class
    Attributes:
        __nb_objects: number of objects created
        id: id of object
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for initializing the instance id values.
        Attributes:
            id (int): The id of the object.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.
        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
