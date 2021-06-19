# My Solutions - First Trial
def get_sum(a,b):
    #good luck!
    result = 0
    
    if a < b:
        for e in range(a, b+1):
            result += e 
    else:  # a >= b
        for e in range(b, a+1):
            result +=e
            
    return result
        
        
# Simple, Best
def get_sum(a,b):
    #good luck!
    return sum(range(min(a, b), max(a, b)+1))