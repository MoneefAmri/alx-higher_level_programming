#!/usr/bin/python3
"""
Module class Square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class inherits from the Rectangle class and
    sets up a square-shaped rectangle with sides of equal length.

    Attributes:
        size (int): The length of each side of the square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class.

        Args:
            size (int): Size of the square.
            Args:
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The ID of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: Size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): New size value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return string representation of the Square instance.

        Returns:
            str: String representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
        Assigns attributes to the instance based on positional
        and keyword arguments.
        Args:
            *args: List of arguments (no-keyworded arguments).
            **kwargs: Dictionary of keyworded arguments.
        """
        if args:
            i = 0
            listme = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, listme[i], arg)
                i += 1
            return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.
        Returns:
            dict: Dictionary representation of the Square.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
