n = int(input())

# power()
def power(a, n):
    """ Return power of a and b
    """
    if n == 0:
        return 1

    if n == 1:
        return a

    x = power(a, (n // 2))
    
    if n % 2 == 0:
        return x * x
    
    elif n % 2 == 1:
        return x * x * a
        
for i in range(n):
    a, b = map(int, input().split())
    data = power(a, b)
    print(data % 10)