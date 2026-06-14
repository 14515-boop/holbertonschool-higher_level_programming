#!/usr/bin/python3
matrix = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]
new_matrix = []
for i in matrix:
    m = []
    for j in i:
        m.append(j**2)
    new_matrix.append(m)
print(new_matrix)