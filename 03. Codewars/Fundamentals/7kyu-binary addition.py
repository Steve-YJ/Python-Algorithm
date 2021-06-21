# Origin: 21.06.21.mon
def add_binary(a,b):
    #your code here
    sum_ = a + b
    result = ""
    print("initial_sum: {}".format(sum_))
    
    if sum_ == 1:  # if sum_ == 1, then return 1
        return "1"
    else:
        while True:
            if sum_//2 != 1:
                result += str(sum_%2)
                sum_ = sum_//2
            elif sum_//2 == 1:
                result = result + str(sum_%2) + str(sum_//2)
                return result[::-1] 