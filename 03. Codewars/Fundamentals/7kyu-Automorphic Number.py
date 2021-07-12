def automorphic(n):
    #your code here
    length= len(str(n))
    square = n*n
    return "Automorphic" if int(str(square)[-length:])==n else "Not!!"