#!/usr/bin/python3
#"end=''" is not added in this code like in most codes bcos prints creates\
#          new line automatically. with end no new line is created.
#In Python, the prefix ‘0x’ is used to indicate that a number is in the hexadecimal system and not in the decimal system like normal integers. In your code, the format method is used to print the value of each figure in decimal and hexadecimal format. The {:d} is used to format the decimal value of each figure and {:x} is used to format the hexadecimal value of each figure. The 0 in 0x is just a prefix indicating that the number is in hexadecimal format
for figure in range(0, 99):
    print("{:d} = 0x{:x}".format(figure, figure))
