#!/usr/bin/python3
"""
Module class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class inherits from the Base class and
    sets up private instance attributes with public getter and
    setter methods. It also provides a constructor
    for initializing instance values.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle's position.
        __y (int): The y-coordinate of the rectangle's position.
        id (int): The ID of an instance of this class.
    """
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
        Setter method for the width attribute.
        Args:
            value (int): The width value to set.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
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
        Setter method for the height attribute.
        Args:
            value (int): The height value to set.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
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
        Setter method for the x attribute.
        Args:
          value (int): The new value for the x attribute.
        Raises:
          TypeError: If the value is not an integer.
          ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
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
        Setter method for the y attribute.
        Args:
          value (int): The new value for the y attribute.
        Raises:
          TypeError: If the value is not an integer.
          ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.
        Returns:
            int: Area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Print the Rectangle instance with '#' character.
        Prints:
            str: Representation of the Rectangle instance.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.
        Returns:
            str: String representation of the Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle instance.
        Args:
            *args: Arguments in the order: id, width, height, x, y.
        """
        if args:
            listme = ['id', 'width', 'height', 'x', 'y']
            i = 0
            for arg in args:
                setattr(self, listme[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.
        Returns:
            dict: Dictionary representation of the Rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
