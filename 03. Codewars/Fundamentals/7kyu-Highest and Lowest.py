# 7Kyu-Highest and Lowest
# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

def high_and_low(numbers):
    # ...
    nums=[]
    numbers = numbers.split()
    for n in numbers:
        nums.append(int(n))
    return "{} {}".format(str(max(nums)), str(min(nums)))