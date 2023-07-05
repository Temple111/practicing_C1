#!/usr/bin/python3

import sys

if __name__=="__main__":
    args = sys.argv[1:]
    n_arg = len(args)
    if n_arg == 0:
        print("0 arguments.")
    elif n_arg == 1:
        print("1 argument:")
        print("1: {}".format(args[0]))
    else:
        print("{} arguments:".format(n_arg))
        for i, arg in enumerate(args):
            print("{}: {}".format(i+1, arg))
