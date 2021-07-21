def well(x):
    #your code here
    if "good" not in x:
        return "Fail!"
    elif x.count("good") in [1, 2]:
        return "Publish!"
    elif x.count("good")>2:
        return "I smell a series!"