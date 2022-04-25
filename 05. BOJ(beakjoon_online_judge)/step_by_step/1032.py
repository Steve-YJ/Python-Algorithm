# 3
# config.sys
# config.inf
# configures

n = int(input())
files = []

for i in range(n):
    files.append(str(input()))

data = [s for s in files[i]]
result = data

for i in range(1, n):
    file = files[i]
    for j in range(len(file)):
        if file[j] != data[j]:
            result[j] = ("?")

print("".join(s for s in result))          