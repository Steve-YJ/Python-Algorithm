"""
#. Need to refactoring it
"""
def solution(digits):
#     print("print: {}".format(digits))
    if len(digits) == 5:
        return int(digits)
    
    lst = []
    for i in range(0, len(digits)-4):
#         print(i)
        lst.append(int(digits[i:i+5]))
    
    return max(lst)