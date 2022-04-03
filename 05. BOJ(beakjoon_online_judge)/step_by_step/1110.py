n = int(input())  # 0 <= n <= 99
origin = n
temp = 100
count = 0

while True:
    if temp == origin:
        print(count)
        break

    else:
        # if count == 0 then temp = origin
        if count == 0:
            temp = origin
            
        # 주어진 자리수를 구해준다
        left, right = temp // 10, temp % 10
        # 주어진 자리수의 합을 구해준다
        sum_ = left + right
        # ㅈ두어진 수의 가장 오른쪽값과 합의 가장 오른쪽 자리수를 이어붙여 새 수를 만들어준다
        temp = str(right) + str(sum_ % 10)
        temp = int(temp)
        count += 1