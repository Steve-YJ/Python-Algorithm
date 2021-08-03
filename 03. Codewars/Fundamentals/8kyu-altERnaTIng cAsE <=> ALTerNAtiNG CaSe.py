def to_alternating_case(string):
    #your code here
    return "".join(s.lower() if s.isupper() else s.upper() for s in string)