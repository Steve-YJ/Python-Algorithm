a, b, c = map(int, input().split())  # get 3 elements
lst = [a, b, c]
maximum = max(lst)

if len(set(lst)) == 1:  # case when all elements are same
  print(10000 + (a * 1000))
elif len(set(lst)) == 2:  # case when two elements are same
  first_elem = list(set(lst))[0]
  second_elem = list(set(lst))[1]
  cnt_first = lst.count(first_elem)
  cnt_second = lst.count(second_elem)
  if cnt_first > cnt_second:
    print(1000 + (100 * first_elem))
  else:
    print(1000 + (100 * second_elem))
else:  # all elements are different
  print(100 * maximum)