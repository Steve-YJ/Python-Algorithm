"""
# Time Complexity... 21.07.04.Sun. pm 6:35
"""

def divisor(x):
    return [i for i in range(1, x+1) if x%i ==0]


def mygcd(x, y):    
    div_x = divisor(x)
    div_y = divisor(y)
    
    return max(set(div_x) & set(div_y))