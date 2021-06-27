# Need to fix it! -21.06.27.sun-

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    #Code here!
    print("entered_code: {}".format(entered_code))
    print("correct_code: {}".format(correct_code))
    print("current_date: {}".format(current_date))
    print("expiration_date: {}".format(expiration_date))
    
    
    month = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
        
    }
    
    cur_month = month[current_date.split()[0]]
    exp_month = month[expiration_date.split()[0]]
    
    cur_date = int(current_date.split()[1][:-1])
    exp_date = int(expiration_date.split()[1][:-1])
    
    cur_year = int(current_date.split()[2])
    exp_year = int(current_date.split()[2])
    
    print()
    print("cur_year: {}".format(int(current_date.split()[2])))
    print("exp_year: {}".format(int(expiration_date.split()[2])))
    print()
    print("cur_month: {}".format(month[current_date.split()[0]]))
    print("exp_month: {}".format(month[expiration_date.split()[0]]))
    print()
    print("cur_date: {}".format(int(current_date.split()[1][:-1])))
    print("exp_date: {}".format(int(expiration_date.split()[1][:-1])))
    
    
    if entered_code != correct_code:
        return False
    elif entered_code == correct_code:
        if cur_year < exp_year:
            return True
        if cur_year > exp_year:  # 1. year
            return False
        elif cur_year == exp_year:  # 2. if year are same
            if cur_month > exp_month:
                return False
            elif cur_month == exp_month and cur_date > exp_date:
                return False
            elif cur_month == exp_month and cur_date <= exp_date:
                return True
            
            
        
    
    return True