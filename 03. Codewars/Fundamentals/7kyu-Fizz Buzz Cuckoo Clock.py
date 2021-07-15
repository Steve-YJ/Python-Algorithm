def fizz_buzz_cuckoo_clock(time):
    # your code here
    
    hour = int(time[:2])%12  # make AM/PM to same hour
    min = int(time[3:])
    
    if hour == 0 and min == 0:  # exception. 00:00, 12:00
        hour = 12
        min = 0
    
    # alram cuckoo
    if min == 30:
        return "Cuckoo"
    elif min == 60 or min == 0:
        return " ".join("Cuckoo" for h in range(hour))
    
    # alram Fizz Buzz
    if min%3 ==0 and min%5 == 0:
        return "Fizz Buzz"
    elif min%3 == 0:
        return "Fizz"
    elif min%5 == 0:
        return "Buzz"
    else:
        return "tick"