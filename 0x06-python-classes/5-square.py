#!/usr/bin/python3
"""Square class."""


class Square:
    """Square class that defines a square."""

    def __init__(self, size=0):
        """
        Initializes a new instance of the square class.

        Args:
            size (int): The size of the square.

        """
        self.size = size

    @property
    def size(self):
        """ Gets the attribute to be used in class """
        return self.__size

    @size.setter
    def size(self, value):
        """
            Setter method for the size attribute.
            Args:
                value (int): The new value for the size attribute.
            Raises:
                TypeError: If the value is not an integer.
                ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Compute the area of a square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square to the standard output using "#" characters.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
