# 7kyu-List-Filtering
# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python


def filter_list(l):
#   'return a new list with the strings filtered out'
    lst = [e for e in l if type(e) != str]
    print(lst)
    return lst