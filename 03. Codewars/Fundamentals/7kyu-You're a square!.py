from math import *

def is_square(n):
    if n >= 0:
        square = int(sqrt(n))
        
        if n == (n*n) or (square * square) == n:
            return True
        else:
            return False
    
    # minus values
    else:  
        return False # fix me