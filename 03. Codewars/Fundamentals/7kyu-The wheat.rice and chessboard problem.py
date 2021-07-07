"""
Test case passed but not all the case

problem: The wheat/rice and chessboard problem
url: https://www.codewars.com/kata/5b0d67c1cb35dfa10b0022c7/train/python
"""

import math

def squares_needed(grains):
    print(grains)
    #your code here
    if grains == 0:
        return 0
    elif grains == 1:
        return 1
    
    else:
        return int(math.sqrt(grains)) + 1