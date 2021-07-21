def well(x):
    #your code here
    if x.count("good")>2:
        return "I smell a series!"
    if "good" in x:
        return "Publish!"
    else:
        return "Fail!"