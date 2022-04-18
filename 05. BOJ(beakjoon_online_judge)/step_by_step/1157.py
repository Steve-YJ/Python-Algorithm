import sys

# e.g. Mississipi
# string = str(input()).lower()
string = str(sys.stdin.readline()).lower()

# make dictionary
dic = {}
value_key = {}

# fill the dictionary
for char in string:
    if char not in dic:
        dic[char] = 1
    else:
        dic[char] += 1

# set the most 
most = 0

# find most values in the dictionary
for key in dic.keys():
    if dic[key] == most:
        most = int(999999)
        break
    elif dic[key] > most:
        most = dic[key]
        value_key[most] = key

if most == int(999999):
    print("?")
else:
    print(value_key[most].upper())
