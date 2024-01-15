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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """
        Return string representation of the Square instance.

        Returns:
            str: String representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
