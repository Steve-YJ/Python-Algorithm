# 2017 British Informatics Olympiad
"""
First trial. 
Passed, but... not satisfied... 21.07.08.Thur.
"""
def triangle(row):
    # Your code here:
    if len(row) == 1:
        return row[0]
    
    lst = []
    
    for i in range(len(row)-1):
        if row[i] == row[i+1]:
            lst.append(row[i])
        else:
            if row[i] == 'G' and row[i+1] == 'G':
                lst.append('G')
            elif (row[i] == 'B' and row[i+1] == 'G') or (row[i] == 'G' and row[i+1] == 'B'):
                lst.append('R')
            elif (row[i] == 'R' and row[i+1] == 'G') or (row[i] == 'G' and row[i+1] == 'R'):
                lst.append('B')
            elif (row[i] == 'B' and row[i+1] == 'R') or (row[i] == 'R' and row[i+1] == 'B'):
                lst.append('G')
                
    return triangle(lst)



"""
Second Trial.

"""
def triangle(row):
    print("row: {}".format(row))
    # Your code here:
    if len(row) == 1:
        return row[0]
    
    dic = {
          'GG': 'G',
          'BB': 'B',
          'RR': 'R',
          'BG': 'R',
          'GB': 'R',
          'RG': 'B',
          'GR': 'B',
          'BR': 'G',
          'RB': 'G'}
    
    lst = []  # make list to make new row
    
    for i in range(0, len(row)-1):
        tmp = "".join(row[i:i+2])
        lst.append(dic[tmp])
    
    return triangle(lst)


"""
Third, Interesting!


"""

def triangle(row):  
    # Your code here:
    if len(row) == 1:
        return row  # return result 

    row = "".join(row[i] if row[i] == row[i+1] else list(set("RGB")-set(row[i:i+2]))[0] for i in range(0, len(row)-1))  # if row[i] == row[i+1], join(row[i]) else, set("RGB")-set(row[i:i+2])

    return triangle(row)  # recursion