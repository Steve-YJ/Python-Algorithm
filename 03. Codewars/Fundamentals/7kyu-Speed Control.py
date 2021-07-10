def gps(s, x):
    # your code
    if len(x) <= 1:
        return 0
    else:
        lst = [x[i+1]-x[i] for i in range(len(x)-1)]
        avg_h = [(3600 * e)/s for e in lst]
        return int(max(avg_h))


