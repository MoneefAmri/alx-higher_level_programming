#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elems_count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            elems_count += 1
        except (ValueError, TypeError):
            pass
    print()
    return elems_count
