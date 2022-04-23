# 10 4790
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000

"""
Greedy
"""

n, remain = map(int, input().split())
coin = []
count = 0

for _ in range(n):
    coin.append(int(input()))

# sort coin in reverse
coin.sort(reverse = True)  # e.g. 50000, 10000, 5000, ...


while True:
    # 나머지가 0이라면 값을 출력하고 무한 루프를 종료한다
    if remain == 0:
        print(count)
        break
    # 가장 큰 지폐부터 거슬러준다
    for c in coin:
        if remain // c > 0:  # 지폐로 거슬러줄 수 있다면 거슬러주자
            count += (remain // c)  # 거슬러준 지폐 숫자만큼 수를 더해준다
            remain -= (remain // c) * c  # 나머지 금액을 구해준다
    