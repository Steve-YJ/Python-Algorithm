def xo(s):
    s = s.lower()
    cnt_x , cnt_o = s.count('x'), s.count('o')
    
    return cnt_x == cnt_o