def distances_from_average(test_list):
    #your code here
    avg = sum(test_list)/len(test_list)
    return [round(avg-test, 2) for test in test_list]
    