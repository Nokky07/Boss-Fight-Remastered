
import random

player_health = 100
boss_health = 200

def attack(player_damage):
    global boss_health
    damage = random.randint(5, 20) + player_damage
    boss_health -= damage
    print("You dealt", damage, "damage to the boss.")
    
def defend(boss_damage):
    global player_health
    
    damage = random.randint(10, 25) - boss_damage
    
    if damage < 0:
        damage = 0
    
    player_health -= damage
    
    print("You took", damage, "damage from the boss.")

def boss_attack():
    damage = random.randint(10, 30)
    defend(damage)

def player_turn():
    print("Your turn:")
    print("  1. Attack")
    print("  2. Defend")
    choice = input("Enter your choice: ")
    if choice == "1":
        attack(10)
    elif choice == "2":
        defend(0)
    else:
        print("Invalid choice!")
        player_turn()

def boss_turn():
    print("Boss's turn:")
    boss_attack()

while player_health > 0 and boss_health > 0:
    print("Your health:", player_health)
    print("Boss's health:", boss_health)
    player_turn()
    if boss_health > 0:
        boss_turn()

if player_health > 0:
    print("Congratulations! You defeated the boss!")
else:
    print("Game over. The boss defeated you.")
