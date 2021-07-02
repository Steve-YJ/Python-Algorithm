def step_func(m):
    x = m//10
    y = m%10
    return x-(2*y)
def divisible(m, step):
    if len(str(m)) <=2 and step_func(m) % 7 == 0:
        return 1
    elif len(str(m)) >= 3 and step_func(m) % 7 == 0:
        return divisible(m, step)


def seven(m):
    step = 0
    print("print_m: {}".format(m))
    # your code
    if divisible(m, step) == 1:
        return (m, step)
    else:
        step +=1
        return divisible(m, step)
    

    
#     if len(str(m)) <= 2 and m%7==0:
#         return (m, step)
#     else:
#         step +=1
#         return seven(step_func(m))