"""
Max Buffer Size Reached (1.5 MiB) -21.07.16.Fri.am8:48-
"""

def subsequence_sums(arr, s):
    # TODO - your code here
    count = 0  # subsequence Sums
    
    for i in range(1, len(arr)+1):
        for j in range(0, len(arr)-(i-1), 1):
            if sum(arr[j:j+i]) == s:
                count += 1
                
    return count     