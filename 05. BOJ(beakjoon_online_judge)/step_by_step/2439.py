n = int(input())

num_star = 1
num_empty = n - num_star

for i in range(n):
    print((" " * num_empty) + ("*" * num_star))
    num_star += 1
    num_empty -= 1
