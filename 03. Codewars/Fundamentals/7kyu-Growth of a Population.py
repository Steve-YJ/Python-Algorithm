# Growth of a Population

def nb_year(p0, percent, aug, p):
    # your code
    y = 0
    
    while True:
        if p0 >= p:  # 인구가 목표치를 달성했다면 
            return y
        else:
            p0 = p0 + int((p0 * percent/100)) + aug
            y += 1