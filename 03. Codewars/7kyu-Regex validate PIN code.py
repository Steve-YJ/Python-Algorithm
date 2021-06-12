# 
# First Trial
def validate_pin(pin):
    #return true or false
    if len(pin) in [4, 6]:
        for p in pin:
            if p not in "0123456789":
                return False
        return True
    
    else:
        return False

# Using .isdigit()
# https://www.w3schools.com/python/ref_string_isdigit.asp
# python isdigit() method return True is all the characters in text are digits
def validate_pin(pin):
    #return true or false
    return len(pin) in [4, 6] and pin.isdigit()