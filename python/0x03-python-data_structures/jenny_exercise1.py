#!/usr/bin/python3

row0 = ['x', 'x', 'x']
row1 = ['x', 'x', 'x']
row2 = ['x', 'y', 'x']

matrix = [row0, row1, row2]
actual_row = matrix[len(row2) - 1]
row2_row =row2[len(row2) - 1]
row2_col =row2[len(row2) - 2]
row2[len(row2) - 2] = 'l'
print(f"{row0}\n{row1}\n{row2}")
