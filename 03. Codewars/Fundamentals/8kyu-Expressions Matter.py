"""Question.
    is this really good?
"""

def expression_matter(a, b, c):
    cases = []
    cases.append(a+b+c)
    cases.append(a*b*c)
    cases.append((a+b)*c)
    cases.append(a+(b*c))
    cases.append(a*(b+c))
    return max(cases)# highest achievable result