def get_count(input_str):
    num_vowels = 0
    
    # your code here
    vowels = ['a', 'e', 'i', 'o', 'u']  # list of vowels
    
    for s in input_str:
        if s in vowels:
            num_vowels +=1
    
    return num_vowels