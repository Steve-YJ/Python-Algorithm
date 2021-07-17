def adjacent_element_product(array):
    result = []
    if len(array) == 2:
        return array[0] * array[1]
    
    for i in range(0, len(array)-1):
        result.append(array[i]*array[i+1])
    return max(result)