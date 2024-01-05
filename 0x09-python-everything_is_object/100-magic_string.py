#!/usr/bin/python3
def magic_string(lst_of_str=[]):
    if lst_of_str is None:
        lst_of_str = []
    lst_of_str += ["BestSchool"]
    return ", ".join(lst_of_str)
