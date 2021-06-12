# 7kyu-Categorize-New Member
# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

def open_or_senior(data):    
    return ["Senior" if m[0] >= 55 and m[1] > 7 else "Open" for m in data]