#!/usr/bin/python3

for a in range(0, 10):
    for b in range(a+1, 10):
        if (a != 8):
            print("{:d}{:d}".format(a, b), end=', ')
        else:
            print("{:d}{:d}".format(a, b), end=' ' "\n")
