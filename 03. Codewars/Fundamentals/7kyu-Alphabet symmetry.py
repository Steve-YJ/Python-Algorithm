ef solve(arr):
    arr = [a.lower() for a in arr]  # convert it to lower case
    
    return [sum(1 for i in range(len(a)) if i == ord(a[i])-97) for a in arr]