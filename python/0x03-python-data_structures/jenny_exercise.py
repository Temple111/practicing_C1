#!/usr/bin/python3

row0 = ['x', 'x', 'x']
row1 = ['x', 'x', 'x']
row2 = ['x', 'x', 'x']

matrix=[row0, row1, row2]

position=input("enter the position u want: ")
#32
row_pos=int(position[0])
col_pos=int(position[1])

actual_row_pos = matrix[row_pos - 1]
actual_row_pos[col_pos - 1] = '2'

print(f"{row0}\n{row1}\n{row1}")
