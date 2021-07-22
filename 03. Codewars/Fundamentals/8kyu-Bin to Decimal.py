def bin_to_decimal(inp):    
    if int(inp)<=1:
        return int(inp)
    else:
        decimal = 0
        for idx, elem in enumerate(inp):
            decimal+= int(elem)*(2**(len(inp)-idx-1))
        return decimal

# I need to refactoring it!