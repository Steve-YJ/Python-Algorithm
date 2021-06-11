# https://www.codewars.com/kata/56606694ec01347ce800001b/train/python

# the longest line should shorter than other lines

"""
def is_triangle(a, b, c):
    lst = sorted([a, b, c], reverse=True)
    max_len = lst[0]
    others = lst[1:]
#     print(max_len, others)
    if max_len < sum(others):
        return True
    return False
"""

# Update - more clever
def is_triangle(a, b, c):
  a, b, c = sorted([a, b, c], reverse=True)
  return b+c > a