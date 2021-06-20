# Origin
def longest(a1, a2):
    # your code
    return "".join(s for s in sorted(set(a1).union(set(a2))))


# refactoring
def longest(a1, a2):
    # your code
    return "".join(sorted(set(a1+a2))) # simple is the best 