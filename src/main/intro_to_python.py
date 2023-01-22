# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:14:55 2023

Intro to Python

@author: Jacob Romero
course: Numerical Calculus
date: 1/22/2023
"""

import numpy as np

# 1. Print a specific 3x3 matrix where a cell is 1 if i == j, else 0

matrix = np.identity(3)
print(matrix)

# 2. Print the 3x3 matrix from #1 and then add 3 to every cell where i≠j

matrix2 = np.where(matrix !=0, matrix, matrix+3)
print(matrix2)

# 3. Print the 3x3 matrix from #2 as a 3x2 by deleting the last column from the matrix created
matrix3 = np.delete(matrix2, 2, 1)
print(matrix3)