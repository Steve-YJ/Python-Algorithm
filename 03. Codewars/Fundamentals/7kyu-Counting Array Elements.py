def count(array):
    #your code here
    set_elem = set(array)
    result={}
    for elem in set_elem:
        result[elem]=array.count(elem)
    return result