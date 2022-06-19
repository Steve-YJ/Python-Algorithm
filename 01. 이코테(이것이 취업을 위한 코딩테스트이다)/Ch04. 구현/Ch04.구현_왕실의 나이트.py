"""
Brute Forcing -2022.06.19.sun-
"""
# 왕실의 나이트
n = 8
maps = [[(i, j) for j in range(n)] for i in range(n)]
cnt = 0  # 결과값을 저장할 변수

# print(maps)
# print("#" * 20)
# print(f"maps[0][0]: {maps[0][0]}")

# 8 x 8 좌표평면 상에서 나이트의 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오

y_dic = {'a' : 0,
        'b' : 1,
        'c' : 2,
        'd' : 3,
        'e' : 4,
        'f' : 5,
        'g' : 6,
        'h' : 7}

# 1. Encoding: 입력 문자 좌표를 좌표평명상 좌표로 변환
point = input(str())
x = int(point[1]) - 1
y = point[0]
y = int(y_dic[y])
print(f"point[x][y]: {x}, {y}")


# 2. 이동할 수 있는 경우의 수 계산
# 상.하.좌.우 컨셉으로 이동시켜보자
# 모두 이동할 수 있다면 8가지 경우의 수가 존재함
# 상
if (x - 2) >= 0:
    print("top")
    if y + 1 <= n:
        cnt +=1
    if y - 1 >= 0:
        cnt += 1
        
# 하
if (x + 2) <= n:
    print("down")
    if y + 1 <= n:
        # print("down 1")
        print(x + 2, y + 1)
        cnt += 1
    if y - 1 >= 0:
        # print("down 2")
        print(x + 2, y - 1)
        cnt += 1
        
# 좌
if (y - 2) >= 0:
    print("left")
    if x -1 >= 0:
        cnt += 1
        print(x - 1, y - 2)
    if x + 1 <= n:
        cnt += 1
        print(x + 1, y - 2)

# 우
if (y + 2 ) <= n:
    print("right")
    if x - 1 >= 0:
        print(x - 1, y + 2)
        # print("right 1")
        cnt += 1
    if x + 1 <= n:
        print(x + 1, y + 2)
        # print("right 2")
        cnt += 1


# 결과 출력
print(cnt)