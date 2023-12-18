#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elems_count = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            elems_count += 1
        except (IndexError, TypeError):
            break
    print()
    return elems_count
