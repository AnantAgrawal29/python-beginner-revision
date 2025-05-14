from game_data import data
import random
import os
logo = r"""    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r""" _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

score = 0
a = 0
b = 0

def assign():
    n1 = random.choice(data)
    n2 = random.choice(data)
    if n1==n2:
        while n2==n1:
            n2 = random.choice(data) 
    return n1,n2

a,b = assign()
print(logo)
print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
print(vs)
print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

def print_score(correct):
    a,b = assign()
    print(logo)
    if correct:
        print(f"You're right! Current score: {score}.")
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    else:
        print(f"Sorry, that's wrong. Final score {score}")


while True:
    higher = 'A' if a['follower_count']>b['follower_count'] else 'B'
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice == higher:
        score+=1
        os.system('cls')
        print_score(True)
    else:
        os.system('cls')
        print_score(False)
        break
    
    
