"""
파일을 입력받고 파일명을 하나씩 비교하는 아이디어
- 파일명이 다를경우, ?로 일관한다!
"""
n = int(input())
files = []
# result = []

for i in range(n):
    files.append(str(input()))

# set the baseline to data
data = [s for s in files[0]]
result = data

for i in range(1, n):
    file = files[i]
    for j in range(len(file)):
        # print(f"file[j]: {file[j]}")
        # print(f"data[j]: {data[j]}")
        if file[j] != data[j]:
            # print(file[j])
            # print(data[j])
            result[j] = ("?")
# print(result)
print("".join(s for s in result))