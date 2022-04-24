# Solv.01
n, k = map(int, input().split())
count = 0

# 나누어 떨어지지 않으면 큰 수로 나눠준다
while True:
    # print(n)
    if n == 1:
        print(count)
        break
        
    if n % k == 0:
        n = n // k
        count += 1
    else:
        n -= 1
        count += 1