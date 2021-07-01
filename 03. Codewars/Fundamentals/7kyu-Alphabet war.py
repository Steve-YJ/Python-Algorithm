def alphabet_war(fight):
    #your code here
    dic = {}
    for i, e in enumerate("zdqm"):
        dic[e] = -1 * (i+1)
    for j, e in enumerate("sbpw"):
        dic[e] = (j+1)
                
    alpha_war = sum(dic[f] if f in dic else 0 for f in fight)
    
    if alpha_war > 0:
        return "Left side wins!"
    elif alpha_war < 0:
        return "Right side wins!"
    else:
        return "Let's fight again!"
    