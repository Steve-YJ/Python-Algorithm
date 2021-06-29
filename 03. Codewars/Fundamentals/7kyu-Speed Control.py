def gps(s, x):
#     print("print s: {}".format(s))
#     print("print x: {}".format(x))
    
    # your code
    if len(x) <= 1:
        return 0
    else:
        lst = [x[i+1]-x[i] for i in range(len(x)-1)]
        avg_h = [3600 * e for e in lst]
#         print("print 3600 * lst: {}".format(3600 * lst))  # fixed bug
        avg_h = [e/s for e in avg_h]
        
        return round(max(avg_h), 2)
