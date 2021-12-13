import perkolacja_funkcje


"""
A set of functions used to test whether percolation occurs in the tested matrix

"""


def _flow(isOpen, isFull, i, j):

    n = len(isFull)
    if (i < 0) or (i >= n):
        return
    if (j < 0) or (j >= n):
        return
    if not isOpen[i][j]:
        return
    if isFull[i][j]:
        return
    isFull[i][j] = True
    _flow(isOpen, isFull, i+1, j)  # Down.
    _flow(isOpen, isFull, i, j+1)  # Right.
    _flow(isOpen, isFull, i, j-1)  # Left.
    _flow(isOpen, isFull, i-1, j)  # Up.
    
def flow(isOpen):
    n = len(isOpen)
    isFull = perkolacja_funkcje.create2D(n, n, value = False )
    for j in range(n):
        _flow(isOpen, isFull, 0, j)
    return isFull

def percolates(isOpen):
    
    isFull = flow(isOpen)
    
    n = len(isFull)
    for j in range(n):
        if isFull[n-1][j]:
            return True
    return False
