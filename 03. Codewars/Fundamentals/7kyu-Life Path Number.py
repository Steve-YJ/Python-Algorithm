def recursion(string):
    while True:
        if int(string)>=10:
            string = str(sum([int(s) for s in string]))
        elif int(string)<10:
            return string

def life_path_number(birthdate):
    # print(birthdate.split("-"))
    result = sum([int(recursion(b)) for b in birthdate.split("-")])
    
    return int(recursion(str(result)))