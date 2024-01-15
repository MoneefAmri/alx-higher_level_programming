#!/usr/bin/python3
"""
Module class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The ID of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get the value of the width object.
        Returns:
            int: The width of the object.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the object.
        Args:
            value: The width value to be set.
        """
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the object.
        Returns:
            int: The height of the object.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the object.
        Args:
            value (int): The new height value.
        """
        self.__height = value

    @property
    def x(self):
        """
        Get the value of x.
        Returns:
            The value of x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Getter method for the x attribute.
        Returns:
            The value of the x attribute.
        """
        self.__x = value

    @property
    def y(self):
        """
        Get the value of y.
        Returns:
            The value of y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Getter method for the y attribute.
        Returns:
            The value of the y attribute.
        """
        self.__y = value
