def balanced_num(number):
    print(number)
    mid = len(str(number)) // 2

    if len(str(number)) % 2 == 0:
        if sum([int(n) for n in str(number)[:mid-1]]) == sum([int(n) for n in str(number)[mid+1:]]):
            return "Balanced"
        else:
            return "Not Balanced"
    else:
        if sum([int(n) for n in str(number)[:mid]]) == sum([int(n) for n in str(number)[mid+1:]]):
            return "Balanced"
        else:
            return "Not Balanced"
        
        