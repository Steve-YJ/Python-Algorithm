# First trial
def is_uppercase(inp):
    letters = "abcdefghijklmnopqrstuvwxyz"  # to check if element in inp is letter or not
    lowers = "".join(e for e in inp.lower().split())  # to remove space
    
    for e in inp:
        if e not in letters:  # if e is not in letter then continue
            continue
        elif e in lowers:  # if e in lower then return False
            print(f"{e} is lower")
            return False
    
    return True