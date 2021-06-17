# Get the Middle Character

def get_middle(s):
    #your code here
    half = int(len(s)/2)
    
    if len(s) %2 == 0:
        return s[half-1:half+1]
    else:
        return s[half]