def palindrome_chain_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    cnt = 0
    if str(n) == str(n)[::-1]:
        return 0
    else:
        while 1:
            n += int(str(n)[::-1])
            if str(n) == str(n)[::-1]:
                return cnt+1
            else:
                cnt+=1