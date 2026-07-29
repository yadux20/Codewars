def declare_winner(fighter1, fighter2, first_attacker):
    if first_attacker == fighter1.name:
        attacker = fighter1
        defender = fighter2
    else:
        attacker = fighter2
        defender = fighter1
​
    while fighter1.health > 0 and fighter2.health > 0:
        defender.health -= attacker.damage_per_attack
        
        if defender.health <= 0:
            return attacker.name
            
        attacker, defender = defender, attacker