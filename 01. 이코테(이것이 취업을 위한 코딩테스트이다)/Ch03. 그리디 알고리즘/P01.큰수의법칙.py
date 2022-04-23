"""
My Solution 1. 가장 큰 수를 K번 더하고 두번째로 큰 수를 한 번 더해준다
"""

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
# sort data
data.sort()

# set the biggest value and second biggest value
first = data[-1]
second = data[-2]

result = 0

# using loop
for i in range(1, m + 1):
    if i % (k + 1) == 0:  # 최대 반복횟수를 넘으면 두번째로 큰 수를 더해준다
        result += second
    else:
        result += first
print(result)


"""
Idea. 반복되는 수열을 사용해 문제를 해결해보자
"""

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
# sort data
data.sort()

first = data[-1]
second = data[-2]

num_first = (m // (k + 1)) * k + (m % (k + 1))
# num_second = m // (k + 1)
num_second = m - num_first

result = (first * num_first) + (second * num_second)
print(result)