#!/usr/bin/python3
"""Square class."""


class Square:
    """Square class that defines a square."""

    def __init__(self, size=0):
        """
        Initializes a new instance of the square class.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Compute the area of a square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
