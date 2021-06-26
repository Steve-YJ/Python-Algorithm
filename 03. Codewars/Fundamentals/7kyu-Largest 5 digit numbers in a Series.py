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



# refactoring it! -21.06.27.sum. am 8:52-
# simple & bueauty

  def solution(digits):
        return max(int(digits[i: i+5]) for i in range(0, len(digits)-4))