def rps(p1, p2):
    #your code here
    winner = {'rock':'scissors', 
          'scissors':'paper',
          'paper':'rock'}
    if winner[p1] == p2:
        return "Player 1 won!"
    elif winner[p2] == p1:
        return "Player 2 won!"
    return "Draw!"