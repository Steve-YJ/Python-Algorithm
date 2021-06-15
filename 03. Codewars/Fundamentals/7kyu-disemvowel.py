def disemvowel(string_):
    pre_string = ""
    for s in string_:
        if s in "aeiouAEIOU":
            continue
        else:
            pre_string += s
            
    return pre_string