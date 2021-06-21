def printer_error(s):
    # your code
    ext = "nopqrstuvwxyz"
    return str(sum(1 for e in s.lower() if e in ext))+"/"+str(len(s))