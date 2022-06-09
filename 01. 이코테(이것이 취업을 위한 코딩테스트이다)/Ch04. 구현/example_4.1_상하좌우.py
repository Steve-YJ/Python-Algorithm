n = int(input("input number: "))
move = list(map(str, input().split()))
map = [(i + 1, j + 1) for j in range(n) for i in range(n)]

cur = [1, 1]
print(f"starting_point: {cur}")


for m in move:
    if m == 'R':
    # pass
    # To-do
    if cur[1] < n:
        cur[1] += 1
  
    elif m == 'L':
    # pass
    if cur[1] > 1:
        cur[1] -= 1
  
    elif m == 'D':
    # pass
        if cur[0] < n:
        cur[0] += 1
    
    elif m == 'U':
    # pass
    if cur[0] > 1:
        cur[0] -= 1

print(cur[0], cur[1])
