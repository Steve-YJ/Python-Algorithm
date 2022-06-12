n = int(input("input n: "))
# makes maps
maps = [[(i + 1, j + 1) for j in range(n)] for i in range(n)]

# get the move
move = list(map(str, input().split()))

# print(f"n: {n}")
# print(f"maps: {maps}")
# print(f"move: {move}")

# set the current location
cur = maps[0][0]
# print(f"cur: {cur}")

# set the x, y 
x, y = cur[0], cur[1]

# let's move!
for m in move:
    if m == "R" and y < n:
        y += 1
    elif m == "L" and y > 1:
        y -= 1
    elif m == "U" and x > 1 :
        x -= 1
    elif m == "D" and x < n:
        x += 1

# print results
print(x, y)