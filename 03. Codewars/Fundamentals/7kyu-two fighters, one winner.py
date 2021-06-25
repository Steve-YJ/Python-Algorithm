# Interesting
# Python Class

def declare_winner(fighter1, fighter2, first_attacker):
    # Code your solution here
    
    f1_name = fighter1.name
    f1_health = fighter1.health
    f1_attack = fighter1.damage_per_attack
    
    f2_name = fighter2.name
    f2_health = fighter2.health
    f2_attack = fighter2.damage_per_attack
    
    while True:
        if first_attacker == f1_name:
            f2_health = f2_health - f1_attack
            if f2_health <= 0:
                return f1_name
            first_attacker = f2_name  # change the turn
        else:  # fighter 2
            f1_health = f1_health - f2_attack
            if f1_health <= 0:
                return f2_name
            first_attacker = f1_name  # # change the turn