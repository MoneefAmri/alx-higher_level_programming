#!/usr/bin/python3
"""Rectangle module.

This module contains a class that defines a rectangle.

"""


class Rectangle:
    """
        Defines a rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
           Initializes an instance of the class with the given width and height.

           Args:
               width (int): The width of the rectangle.
               height (int): The height of the rectangle.
       """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            Getter method for width of the rectangle.
            Returns:
                int: The width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter method for the width of the rectangle.
            Args:
                value (int): The new value for the width of the rectangle.
            Raises:
                ValueError: If the value is less than 0.
                TypeError: If the value is not an integer.
            """

        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
            Get the height of the rectangle.

            Returns:
                int: The height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter method for the height attribute.

            Args:
                value (int): The new value for the height attribute.

            Raises:
                ValueError: If the value is less than 0.
                TypeError: If the value is not an integer.
        """
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """
            Calculate and return the area of the rectangle.

            Returns:
                float: The area of the rectangle.
        """

        return self.__width * self.__height

    def perimeter(self):
        """
            Returns the current rectangle perimeter.

            Returns:
                int: The perimeter of the rectangle.
        """

        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """
            Returns a string representation of the Rectangle.

            Returns:
                str: A string representing the Rectangle.
        """

        rec_str = ""

        # Check if the width and height are greater than 0
        if self.__width > 0 and self.__height > 0:
            # Create a string with '#' repeated for the width of the rectangle
            # and add a newline character for each row
            rec_str = '#' * self.__width + '\n' * self.__height

        # Remove the extra newline character at the end of the string
        return rec_str[:-1]

    def __repr__(self):
        """
            Return a string representation of the Rectangle object.

            Returns:
                str: A string representation of the Rectangle object.
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self) -> None:
        """
            This method is called when the Rectangle is about to be destroyed.
            It prints a farewell message to the console.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...", flush=True)
