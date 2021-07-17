def is_uppercase(inp):
    print(f"inp: {inp}")
    print(f"inp.upper(): {inp.upper()}")
    print(f"inp==inp.upper(): {inp==inp.upper()}")  # if inp chars and inp.upper() chars are same, it will return True
                                                    # because return True as the Unicode of all the characters are equal - from Geeks for Geeks
    
    return inp==inp.upper()