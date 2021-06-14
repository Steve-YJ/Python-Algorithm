# Mumbling
# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(s):
    # your code
    
    start = 1
    answer = ""
    
    # for loop
    for e in s:
        before = e.lower() * start
        before = before[0].capitalize() + before[1:]
        answer = answer + str(before+"-")
        start += 1
    
    print(answer[:-1])
    
    return answer[:-1]