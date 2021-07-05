def close_compare(a, b, margin=0):
    if abs(a-b) <= margin:
        return 0
    elif abs(a-b) > margin and a > b:
        return 1
    elif abs(a-b) > margin and a < b:
        return -1