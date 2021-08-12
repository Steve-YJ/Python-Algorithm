def halving_sum(n): 
    # your code here
    i = 0
    result = 0
    while True:
        if int(n/(2**i))>1:
            result += int(n/(2**i))
            i += 1
        elif int(n/(2**i)) == 1:
            result += int(n/(2**i))
            return result