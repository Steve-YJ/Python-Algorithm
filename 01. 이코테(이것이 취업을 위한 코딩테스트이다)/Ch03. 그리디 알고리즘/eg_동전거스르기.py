"""
다시시작하는 이코테
Greedy Algorithm
"""

n = int(input())

coin = [500, 100, 50, 10]
count = 0
remain = n

for c in coin:
    if remain // c > 0:  # 가장 큰 화폐로 거슬러 줄 수 있다면 거슬러주자
        num = remain // c
        count += num  # 거슬러준 화폐수를 더해준다
        remain -= (c * num)  # 화폐를 거슬러주고 남은 돈을 계산한다

print(count)