origin = int(input())  # get nuber
temp = origin
sum_ = 0
new = 100
count = 0 # count from 0

while True:
    if count != 0 and temp == origin:  # if temp == origin then return count
        print(count)
        break
    else:
        if temp >= 10:
            temp = str(temp)
            first, second = temp[0], temp[1]
            sum_ = int(first) + int(second)
            new = second + str(sum_)[-1] # 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리수를 이어 붙여 새로운 수를 만들어 준다

            # change data type again
            # from string to int
            temp = int(temp)
            new = int(new)
            # add count
            count += 1
            # now new become temp
            temp = new
            
        else:  # if temp < 10
            new = str(temp) + str(temp)
            count += 1
             