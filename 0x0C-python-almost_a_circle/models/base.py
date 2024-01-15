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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): List of instances that inherit from Base.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by a JSON string.
        Args:
            json_string (str): representing a list of dictionaries.
        Returns:
            list: List represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
