def seven(m):
    # your code
    step = 0
        
    while True:
        print(m)
        if len(str(m)) <= 2 and m % 7 == 0:
            return (m, step)
        else:
            x, y = m//10, m%10
            if (x-(2*y)) % 7 == 0:
                m = x-(2*y)
                step += 1
            else:
                return

        