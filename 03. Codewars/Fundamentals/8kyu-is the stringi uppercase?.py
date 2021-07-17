# Second Trial, Refactoring
def is_uppercase(inp):    
    for e in "".join(inp.split()):
        if e == e.upper():  # if e in upper then continue
            continue
        elif e == e.lower():  # if e in lower then return False
            print(f"{e} is lower")
            return False
    
    return True