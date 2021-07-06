def cube_odd(arr):
    #your code here - return None if at least a value is not an integer
    for a in arr:
        if type(a) != int:
            return None
        
    return sum([elem**3 for elem in arr if elem%2==1 and type(elem)==int])