def recursion(string):
    string = sum([int(s) for s in str(string)])
    if string>=10:
        return recursion(string)
    else:
        return string

def life_path_number(birthdate):
    return recursion(sum([recursion(b) for b in birthdate.split("-")]))