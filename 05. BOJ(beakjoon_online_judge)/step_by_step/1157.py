"""got runtime error!! -2022.04.12"""

from collections import Counter

# convert input to lower case
string = str(input()).lower()

# using Counter() class
counter = Counter(string)
# you can find most freqeunt words
most_common = counter.most_common()

if most_common[0][1] == most_common[1][1]:
    print("?")
else:
    print(most_common[0][0].upper())  # print output as upper case