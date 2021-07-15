result = [arr[idx+1] for idx, a in enumerate(arr[:-1]) if arr[idx]+1 != arr[idx+1]]
if  len(result) == 0:
    return None
else:
    return result[0]