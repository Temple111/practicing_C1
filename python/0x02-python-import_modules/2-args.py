#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    n_args = len(args)
    if n_args == 0:
        print("0 arguments.")
    elif n_args == 1:
        print("1 argument:")
        print("1: {}".format(args[1]))
    else:
        print("{} arguments:".format(n_args))
        for i, arg in enumerate(args):
            print("{}: {}".format(i+1, arg))
