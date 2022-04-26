"""
8줄 밖에 안되는 체스판의 특징을 떠올리며 해결
"""

chase = []
count = 0

for i in range(8):
    chase.append([s for s in str(input())])

for i in range(8):
    # 짝수 번째 줄은 첫 칸이 흰색인 체스줄이다
    if i % 2 == 0:
        for j in range(8):
            if chase[i][j] == 'F' and j % 2 == 0:
                count += 1
    # 홀수 번째 줄은 첫 칸이 검정색인 체스줄이다
    elif i % 2 == 1:
        for j in range(8):
            if chase[i][j] == 'F' and j % 2 == 1:
                count += 1

print(count)