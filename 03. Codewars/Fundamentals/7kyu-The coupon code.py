"""
Hard Coded: 21.06.27.Sun. pm11:21
"""

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    #Code here!
    print("entered_code/correct_code: {}/{}".format(entered_code, correct_code))
    print("cur_date: {}".format(current_date))
    print("exp_date: {}".format(expiration_date))

    
    # cur, exp_year
    cur_year = int(current_date.split()[2])
    exp_year = int(expiration_date.split()[2])
    
    # cur, exp_month
    dic_month = {'January': 1,
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
                'December': 12}
    
    cur_month = dic_month[current_date.split()[0]]  # dic_month's value
    exp_month = dic_month[expiration_date.split()[0]]
    
    # cur, exp_date
    cur_date = int(current_date.split()[1][:-1])
    exp_date = int(expiration_date.split()[1][:-1])
    
    # LEGO~!
"""
The Rule is Simple.
Check Year first, and then check month and then date
"""

    if entered_code != correct_code or type(entered_code) != type(correct_code):
        return False
    elif entered_code == correct_code:
        if cur_year > exp_year:  # first, check year are same or not
            return False
        elif cur_year == exp_year:
            if cur_month > exp_month:  # if year are same, then compare month
                return False
            elif cur_month == exp_month:  # if year and month are same, then check date
                if cur_date > exp_date:
                    return False
    
    return True