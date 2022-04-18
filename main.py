string = str(input()).lower()
dic = {}
value_key = {}

for char in string:
    if char not in dic:
        dic[char] = 1
    else:
        dic[char] += 1

# most frequent words
most = 0

for key in dic.keys():
    if dic[key] == most:
        print("?")
    elif dic[key] > most:
        most = dic[key]
        value_key[dic[key]] = key

# print most frequent word
print(value_key[most])