def validate_pin(pin):
    #return true or false
    
    if len(pin) == 4 or len(pin) == 6:
        for p in pin:
            if p in '0123456789':
                continue
            else:
                return False
            
        return True
    
    else:
        return False
    
    
# upgrade - much simple!
def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()