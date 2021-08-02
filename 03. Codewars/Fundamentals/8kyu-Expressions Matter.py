def expression_matter(a, b, c):
    case = []
    case.append(a*b*c)
    case.append(a+b+c)
    case.append(a*(b+c))
#     case.append(a+(b*c))  # because a*(b+c) >= a+(b*c)
    case.append((a+b)*c)
#     case.append((a*b)+c)  # because (a+b)*c >= (a*b)+c
    return max(case)  # So, this is highest achievable result! :)