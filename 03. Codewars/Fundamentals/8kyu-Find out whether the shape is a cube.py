import math

def cube_checker(volume, side):
    if volume<=0 or side<=0:  # if volume<0 or side<0: return False
        return False
    else:  # check if cube has same length or not
        return True if volume//side == math.sqrt(volume/side)**2 else False