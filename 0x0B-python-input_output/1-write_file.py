#!/usr/bin/python3
'''Module to writes a string to a text file'''


def write_file(filename="", text=""):
    """
    function that writes a string to text file (UTF8)
    Args:
        filename - name of the file to write to.
        text(str) - the string to write
    Return:
        Number of charter written.
        :param text:
        :param filename:
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
