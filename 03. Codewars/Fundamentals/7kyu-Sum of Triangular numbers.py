def sum_triangular_numbers(n):
    #your code here
    if n <0:  # if input value under 0, return 0 
        return 0
    
    start = 1  # this is start number
    tmp = 0    # set tmp for indexing
    answer = []  # append last number 
    
    for i in range(1, n+1):
        tmp_lst = []
        for j in range(start, start+i):
            tmp = j
            tmp_lst.append(j)
            
        start = tmp + 1  # after loop, update start number
        answer.append(tmp_lst[-1])
        
    return sum(answer)