def row_sum_odd_numbers(n):
    #your code here
    s = 1        # initiate first number of row
    sum_odd = 0  # initiate sum_odd as 0
    
    if n == 1:
        return 1
    else:
        for n in range(1, n+1):  # first. calc first value of n_th row
            s = s + 2*(n-1)    
        
        for i in range(n):  # iterate and sum all the elements
            sum_odd += s  # add_odd
            s += 2        # update_odd
    return sum_odd
            