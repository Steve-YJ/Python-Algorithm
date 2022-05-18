"""
그리디로 풀이 가능 -2022.05.18-
"""

n = int(input())

count = 0

while True:
    if n % 5 != 0:  # 5로 나누어 떨어지지 않는 경우
        n -= 3
        count += 1

    elif n % 5 == 0:
        count += (n // 5)  # 5로 나누어 떨어지면 몫만큼 더해준다
        print(count)
        break

    if n < 0:
        print(-1)  # 이도 저도 아니라면 -1을 리턴한다
        break
        
        