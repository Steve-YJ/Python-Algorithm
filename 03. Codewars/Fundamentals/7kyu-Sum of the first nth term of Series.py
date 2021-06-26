"""
# Solved it. But... need to refactoring it! -21.06.26.Sat-
# Question. What is {:.2f} in python?
"""

def series_sum(n):
    # Happy Coding ^_^
    # Thank you! lol
    if n == 0 or n == 1:
        return str("{}.00".format(n))
    else:
        result = str(round(1/1 + sum(1/(1+3*i) for i in range(1, n)), 2))
        if len(result) == 3:
            return result+"0"
        else:
            return result