#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    str = "{} argument"
    args = len(sys.argv) - 1
    if args == 0:
        str += "s."
    elif args == 1:
        str += ':'
    else:
        str += "s:"
    print(str.format(args))

    i = 0
    for arg in sys.argv:
        if i != 0:
            print("{}: {}".format(i, arg))
        i += 1
