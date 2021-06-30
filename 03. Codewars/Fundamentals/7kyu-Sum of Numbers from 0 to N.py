def show_sequence(n):
    if n < 0:
        return "{}<0".format(n)
    elif n == 0:
        return "0=0"
    else:
        return "".join(str(i)+"+" for i in range(n+1))[:-1] +" = " + str(sum(e for e in range(n+1))) + ""