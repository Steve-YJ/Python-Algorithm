def to_jaden_case(string):
    answer = ""
    for s in string.split():
        s = s[0].upper() + s[1:]
        answer = answer + s + " "
    
    # ...
    return answer[:-1]