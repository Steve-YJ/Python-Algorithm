"""
Need to refactoring the code
https://www.acmicpc.net/problem/1439
"""

s = str(input())

count = 0
prev = s[0]  # initialization

if s == '0' or s == '1' or '0' not in s or '1' not in s:
    print(0)

else:
    for e in s[1:]:
        temp = e
        if temp == prev:
            pass
        else:
            count += 1
            prev = temp # 이전값과 다르면 1을 증가시키고 현재값을 이전값으로 설정한다

    # print the result
    if count % 2 == 1:
        print((count // 2) + 1)
    else:
        print(count // 2)

