# Ones and Zeros
# https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python

def binary_array_to_number(arr):
  # your code
    result = 0
    length = len(arr)
    
    for a in arr:
        if a != 0:
            result += 2 ** (length-1)
            length -=1
        elif a == 0:
            length -= 1
    
    return result