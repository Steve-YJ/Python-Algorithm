# answer = 24
a, b, c, m = map(int, input().split())

if a > m:
    print(0)
    
else:
    tire = 0
    work = 0

    for i in range(24):
    # print(i)
        if tire < m:  # 일 할 수 있으면 일해라
            work += b
            tire += a
        # print(work, tire)

        else:
            tire -= c  # 피곤하면 쉬자
            if tire <= 0:
                tire = 0
        
        # print(work, tire)



    print(work)
