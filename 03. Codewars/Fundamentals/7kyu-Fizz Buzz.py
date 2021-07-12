def fizzbuzz(n):
    # your code here
    lst = []
    for i in range(1, n+1):
        if i%3==0 and i%5== 0:
            lst.append("FizzBuzz")
        elif i%5==0:
            lst.append("Buzz")
        elif i%3==0:
            lst.append("Fizz")
        else:
            lst.append(i)
    return lst