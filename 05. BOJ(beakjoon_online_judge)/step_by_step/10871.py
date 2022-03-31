n, x = map(int, input().split())
lst = input().split()
lst = [elem for elem in lst if int(elem) < x]
result = " ".join(elem for elem in lst)
print(result)