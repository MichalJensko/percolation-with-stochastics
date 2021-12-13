import numpy as np
import random


def create2D(rowCount, colCount, value=None):

# Used for generating square matrices of given size of a side
    a = [None] * rowCount
    
    for row in range(rowCount):
        a[row] = [value] * colCount
    
    return a


"""
Generates a matrix  with a given side and then changes some of the zeros to open cells,
capable of participating in percolation.
    p - probability that the cell is open
    n - side length of the matrix
"""


def random2D(n, p):

    a = create2D(n, n, value=0)
              
    row_count = len(a)
    col_count = len(a[0])
    
    b = np.array(a)
    b_1d = b.flatten()  
    
    for element in range(0, len(b_1d)):

        if random.choices([1, 0], weights=(p, 1-p)) == [1]:
            b_1d[element] = 1
    
    b = np.resize(b_1d, (row_count, col_count))
    return b


