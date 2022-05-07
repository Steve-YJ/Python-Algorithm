"""
Solution 1. Brute Force
"""
a, b = map(str, input().split())

max_a = ""
min_a = ""

max_b = ""
min_b = ""

for s in a:
    if int(s) == 6:
        print(s)
        min_a += "5"
        max_a += "6"
    elif int(s) == 5:
        min_a += "5"
        max_a += "6"
    else:
        min_a += s
        max_a += s
print(f"min_a: {min_a}, max_a: {max_a}")

for s in b:
    print(f"s: {s}")
    if int(s) == 6:
        min_b += "5"
        max_b += "6"
    elif int(s) == 5:
        min_b += "5"
        max_b += "6"
    else:
        min_b += s
        max_b += s
print(f"min_b: {min_b}, max_b:{max_b}")

print((int(min_a) + int(min_b)), (int(max_a) + int(max_b)))



"""
Solution 2.
"""