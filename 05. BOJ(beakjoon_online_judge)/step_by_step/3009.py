# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

x_data = []
y_data = []

# 세 점의 좌표를 입력받아 x_data, y_data에 쌓는다
for _ in range(3):
    x, y = map(int, input().split())
    x_data.append(x)
    y_data.append(y)

# 세 점의 x, y 좌표에서 중복되지 않는 값을 찾는다
set_x_data = list(set(x_data))
set_y_data = list(set(y_data))

result = []
# set_x_data, set_y_data에서 중복되지 않는 값을 돌며 값이 하나만 있을 경우 결과 리스트에 더해준다
for d in set_x_data:
    if x_data.count(d) == 1:
        result.append(d)
        break
        
for d in set_y_data:
    if y_data.count(d) == 1:
        result.append(d)
        break

# 공백을 기준으로 값을 출력해준다
for d in result:
    print(d, end = ' ')