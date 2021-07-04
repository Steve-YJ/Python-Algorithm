"""
# Solved it! -21.07.04.pm7:40-
"""

def divisor_(x, y):
    return x//y, x%y  # 몫과 나머지로 생각해보자

def mygcd(x, y):
    while True:
        prev_x, prev_y = x, y
        tmp_x, tmp_y = divisor_(x, y)
        x, y = prev_y, tmp_y
        if tmp_y == 0:
            return prev_y