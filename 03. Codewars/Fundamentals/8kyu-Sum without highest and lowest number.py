def sum_array(arr):
    #your code here
    if arr == None or len(arr) <= 1:
        return 0
    else:
        arr.pop(arr.index(max(arr)))
        arr.pop(arr.index(min(arr)))
        return sum(a for a in arr)