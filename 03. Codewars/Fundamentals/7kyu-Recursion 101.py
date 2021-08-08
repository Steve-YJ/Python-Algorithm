"""
# RecursionError: maximum recursion depth exceeded in comparison

def step1(a,b):
    if a==0 or b==0:
        return [a,b]
    else:
        return step2(a,b)

def step2(a,b):
    if a>=2*b:
        a=a-2*b
        return step1(a,b)
    else:
        return step3(a,b)

def step3(a,b):
    if b>=2*a:
        b=b-2*a
        return step1(a,b)
    else:
        return [a,b]

def solve(a,b):
    return step1(a,b)

"""

def solve(a,b):
"""
This is way you can avoid recursion error!
"""
    while a>=2*b or b>=2*a:
        if a==0 or b==0:
            return [a,b]
        elif a>=2*b:
            a=a-2*b
        elif b>=2*a:
            b=b-2*a
            
    return [a,b]