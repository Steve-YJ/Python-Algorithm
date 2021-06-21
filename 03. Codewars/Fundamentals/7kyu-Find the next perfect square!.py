import math  # why don't we use isqrt?

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    int_sqrt = math.isqrt(sq)
    if int_sqrt ** 2 == sq:  # if in_sqrt is root_square of sq
        return (int_sqrt+1)**2  # rerutn square value of (int_sqrt+1)
    return -1
