#!/usr/bin/python3
"""
Module class Base
"""


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
