# Origin
def divisors(integer):
    lst= []

    for i in range(1, integer+1):
        if integer % i == 0:
            lst.append(i)
            lst.append(integer//i)

    sorted_ = sorted([e for e in set(lst)])[1:-1]
#     print("sorted_: {}".format(sorted_))
    
    if len(sorted_) == 0:
        return "{} is prime".format(integer)
    else:
        return sorted_