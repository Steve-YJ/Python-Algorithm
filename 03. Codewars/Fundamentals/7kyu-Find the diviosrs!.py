"""
Not Solved -21.06.22.Tue-
"""
def divisors(integer):
    lst= []
    print("integer: {}".format(integer))
    for i in range(1, integer+1):
        if integer % i == 0:
            lst.append(i)
            lst.append(integer)
            
    if len(lst) == 0:
        return [1, integer]
    else:
        return sorted(set(lst))[1:-1]