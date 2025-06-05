# import random
# print('helloworld')
# print(len(input('what is your name: ')))

# # Band Generator
# print("Welcome to the Band Name Generator.")
# city = input("What's the name of the city you grew up in?\n")
# pet = input("What's your pet's name?\n")
# print("Your band name could be "+city+" "+pet)

# print(type(123))
# print(type("hello"))
# print(type(True))
# print(type(12.3))

# print("123"+"234")
# print(123+234)
# print(123_234)

# print(5**2)
# print(5/2)
# print(5//2)
# print(26%23)

# #PEMDAS (),**,* OR /,+ OR -

# print(int(3.5),int(3.7))
# print(round(3.5),round(3.7))
# score = 30
# print(f"Your score is = {score}")

# #Tip calculator
# print("Welcome to the tip calculator!")
# bill = float(input("What is your bill? $ "))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))

# #bill/people = bill to paid by each person
# #tip is in % so we will divide it 100 and then multiply by bill/people to find the tip for 1 person
# #then we add the tip to bill/people
# # (tip/100)*(bill/people) + bill/people = (tip/100+1)*(bill/people) is we take bill/people common

# total= round((bill/people) * (1+tip/100),2)
# print(f"Each person should pay: ${round(total,2)}")
# print("Each person should pay : $",total)

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm ? "))
# if height > 120:
#     print("You can ride the rollercoaster")
#     bill = 0
#     age = int(input("What is your age? "))
#     if age <12:
#         print("Child tickets are 5$")
#         bill = 5
#     elif age <=18:
#         print("Youth tickets are 7$")
#         bill = 7
#     elif age>=45 and age<=55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         print("Adult tickets are 12$")
#         bill = 12
    
#     wants_photo = input("Do you want to have a photo take? Write y for Yes and n for No: ")
#     if wants_photo == "y":
#         bill += 3
#     print("Total bill =",bill)
# else:
#     print("You cannot ride the rollercoaster")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill=0

# if size == 'S':
#     bill = 15
# elif size == 'M':
#     bill = 20
# else:
#     bill = 25

# if pepperoni == 'Y':
#     if size == 'S':
#         bill+=2
#     else:
#         bill +=3

# if extra_cheese == 'Y':
#     bill += 1

# print(f"Your final bill is: ${bill}")

# print(r'''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# print("\nYou're at a crossroad. Where do you wanna go?")
# choice = input("\tType 'left' or 'right'\n").lower()

# if(choice=="right"):
#     print("You fell over. Game over!")
# else:
#     print("You've have come to a lake. There is an island in the middle of the lake.")
#     swim = input("\tType 'wait' to wait for a boat . Type 'swim' t swim across.\n").lower()
#     if(swim=='swim'):
#         print("You get attacked by an angry trout. Game Over.")
#     else:
#         color = input("One red, one yellow and one blue. Which color do  you choose?\n")
#         if(color=="blue"):
#             print("You enter a room of beasts. Game Over.")
#         elif(color == "red"):
#             print("It's a room full of fire. Game Over.")
#         elif(color=='yellow'):
#             print("You found the treasure! You Win!")
#         else:
#             print("Wrong output")

# import my_module # my_module.py file
# print(my_module.my_fav_num)


# random_int = random.randint(1, 10)
# print(random_int)
# random_float = random.uniform(1,2)
# print(random_float)

# # head,tails
# print("Heads" if (random.randint(0,1) == 0) else "Tails")

# # lists
# ch = [1,2,3,4,5]
# print(ch[0])

# states_of_america = ['Delaware','Pennsylavnia','New Jersey','Georgia','Connecticut','Massachusetts','Maryland','South Carolina','New Hampshire','Virginia',
#                      'New York','North Carolina','Rhode Island','Vermont','Kentucky','Tennessee','Ohio','Louisiana','Indiana','Mississippi','Illinois','Alabama',
#                      'Maine','Missouri','Arkansas','Michigan','Florida','Texas','Iowa','Wisconsin','California','Minnesota','Oregon','Kansas','West Virginia']
# print(states_of_america)

# print(len(states_of_america), states_of_america[-25], states_of_america[10], states_of_america[-10], states_of_america[25])

# print(states_of_america[3])
# states_of_america[3] = 'jerry'
# print(states_of_america[3], states_of_america[-1])

# #append adds item to the list
# states_of_america.append('Hi')
# print(states_of_america[-1])

# #extend merges two lists one that is before dot and one which is given in function parameter
# states_of_america.extend(['AnantFerry', 'Akshaylund'])
# print(states_of_america[-1],states_of_america[-2])

# #insert - inserts an element at the given index
# print(states_of_america[1])
# states_of_america.insert(1,'Halaluia')
# print(states_of_america[1])


# friends = ['Alice', 'Bob', 'Charlie', 'David', 'Emanuel']
# print(friends[random.randint(0,(len(friends)-1))])
# print(random.choice(friends))

# dirty_dozen = ['Strawberries', 'Spinach', 'Kale', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes', 'Celery', 'Potatoes']
# fruits = ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
# vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']

# dirty_dozen = [fruits,vegetables]
# print(dirty_dozen)



# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# rps = [rock,paper,scissors]

# choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
# comp = random.randint(0,2)
# if choice !=1 or choice!=2 or choice!=0:
#     print("You typed an invalid number. You lose!")
# else:
#     print(rps[choice],'\nComputer chose:')
#     print(rps[comp])
#     if comp==choice:
#         print("It's a draw")
#     elif (comp==1 and choice==2) or (comp==2 and choice==0) or (comp==0 and choice==1):
#         print('You won')
#     else:
#         print('You lose')

# # Loops
# fruits = ['Apple', 'Peache', 'Pear']
# for fruit in fruits:
#     print(fruit)

# # sum function
# scores = [123,146,78,23,45,26,63]
# print(sum(scores))

# s=0
# for score in scores:
#     s+=score
# print(s)

# # max function
# print(max(scores))
# maximum=0
# for score in scores:
#     if(score > maximum):
#         maximum=score
# print(maximum)

# #range funciton and end value in print funciton
# for num in range(1,11,3):
#     print(num,"",end="")

# # Gauss Challenge
# print(sum(range(1,101))) 

# # Password Generator

# print("Welcome to the PyPassword Gnerator!")
# letter = int(input("How many letters would you like in your password?\n"))
# symbol = int(input("How many symbols would you like in your password?\n"))
# number = int(input("How many numbers would you like in your password?\n"))

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# password = [random.choice(letters)]
# for n in range(1,letter):
#     l = random.choice(letters)
#     while l==password[-1]:
#         l = random.choice(letters)
#     password.append(l)

# for n in range(0,symbol):
#     l = random.choice(symbols)
#     while l==password[-1]:
#         l = random.choice(symbols)
#     password.append(l)

# for n in range(0,number):
#     l = random.choice(numbers)
#     while l==password[-1]:
#         l = random.choice(numbers)
#     password.append(l)
# print(password)
# random.shuffle(password)
# print(password)
# print("Your password is: ",end="")
# for num in password:
#     print(num,end="")

# # Functions

# def my_func():
#     print("Helloworld")

# my_func()
# # rest was done at reeborg's world site

# # Hangman Project in different folder

# # function parameter

# def greet_with_name(name):
#     print(f"Hello {name}")

# greet_with_name("Anant")

# def greet_with(name, location):
#     print(f"Hello {name}!")
#     print(f"What is it like in {location}?")

# greet_with("Anant","Kanpur")
# greet_with(name="Manan",location="Prayagraj")

# def calculate_love_score(name1, name2):
#     n1=0
#     n2=0
#     for char in name1:
#         char = char.lower()
#         for c in 'true':
#             if c==char:
#                 n1+=1
#         for c in 'love':
#             if c==char:
#                 n2+=1
#     for char in name2:
#         char = char.lower()
#         for c in 'true':
#             if c==char:
#                 n1+=1
#         for c in 'love':
#             if c==char:
#                 n2+=1
#     love_score = str(n1)+str(n2)
#     print(int(love_score))

# # caesar cipher project in different file

# # dictionaries

# student_marks = {
#     "Anant": 56,
#     "Aditi": 49,
#     "Manan": 56,
#     "Akshay": 100
# }

# for key in student_marks:
#     print(f"{key} got {student_marks[key]} marks")

# # Auction Program
# import os
# bidders = {}
# logo = '''
#                          ___________
#                          \         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\\
#                        .-------------.
#                       /_______________\\
# '''
# print(logo)
# print("Welcome to the secret auction program.")
# while True:
#     bidder = input("What is your name?: ")
#     bid = int(input("What's your bid?: $"))
#     bidders.update({bidder:bid})
#     choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
#     os.system('cls')
#     if choice=='no':
#         break

# highest_bid=0
# highest_bidder=""
# for bidder in bidders:
#     bid = bidders[bidder]
#     if bid > highest_bid:
#         highest_bid=bid
#         highest_bidder=bidder
# print(f"The winner is {highest_bidder} with a bid of {highest_bid}.")

# # More on functions

# def format_name(f_name, l_name):
#     """Takes first and last name and returns full name in title case"""
#     # docstring
#     return f_name.title() + " " + l_name.title()


# print(format_name("anant", "agrawal"))

# # Calculator

# def calc(n1,n2,op):
#     if op=='*':
#         return n1*n2
#     elif op=='+':
#         return n1+n2
#     elif op=='-':
#         return n1-n2
#     elif op=='/':
#         return n1/n2
#     return False
    
    

# while True:
#     print("""
#     _____________________
#     |  _________________  |
#     | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
#     | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
#     |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
#     | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
#     | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
#     | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
#     | |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
#     | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
#     | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
#     | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
#     | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
#     |_____________________|
#     """)
#     n1 = float(input("What's the first number: "))
#     while True:
#         op = input("+\n-\n*\n/\nPick an operation: ")
#         n2 = float(input("What's the next number: "))
#         result = float(calc(n1,n2,op))
#         print(n1,op,n2,"=",result)
#         ch = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
#         if ch=='n':
#             break
#         else:
#             n1 = result

# # blackjack project in another folder

# # global scope

# enemies = 1

# def add_enemies():
#     # enemies+=1
#     global enemies
#     enemies+=1
#     print(enemies)

# add_enemies()
# # Number guessing game

# print(r"""  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
#  / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
# / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
# \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|""")
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# chances = 10 if difficulty=="easy" else 5
# number = random.randint(1,100)
# found = False
# for i in range(chances,0,-1):
#     print(f"You have {i} attempts remaining to guess the number.")
#     guess = int(input("Make a guess: "))
#     if guess == number:
#         print(f"You got it. The answer was {number}.")
#         found = True
#         break
#     elif guess > number:
#         print("Too high.\nGuess again!.")
#     else:
#         print("Too low.\nGuess again!.")
# if not found:
#     print("You've run out of guesses. Refresh the page to run again.")

# # Error And Exception

# try:
#     age = int(input("Enter a number in string: "))
# except ValueError:
#     print("give input in number format")
#     age = int(input("Enter a number in string: "))
# else:
#     print(age)

# # Higher Lower Project In Another Folder

# # Turtle

# from turtle import Turtle,Screen

# tim = Turtle()
# tim.shape('turtle')
# tim.color('PeachPuff1')
# tim.forward(100)
# print(tim)

# my_screen = Screen()
# my_screen.bgcolor('gray10')
# print(my_screen.canvheight)
# my_screen.exitonclick()

# # Packages

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column('Pokemon Name',['Pikachu','Squirtle','Charmander'])
# table.add_column('Type',['Electric','Water','Fire'])
# table.align = 'l'
# print(table)

# # OOP Coffee Machine project in different folder

# # Making Classes

# class User:
#     def __init__(self,userID, username): # contsructor method
#         self.id = userID
#         self.username = username
#         self.followers = 0
#         self.following = 0

#     def follow(self, user):
#         user.followers += 1
#         self.following += 1

# user1 = User(1234,'John Wick')
# user2 = User(1122, 'Reyna Martin')
# print(f"User1 Details:\nUser ID : {user1.id}\nUsername : {user1.username}")
# user1.follow(user2)
# print(f"User1 Followers: {user1.followers}\tUser1 Following: {user1.following}")
# print(f"User2 Followers: {user2.followers}\tUser2 Following: {user2.following}")
    
# # Quiz Project in another folder

# # importing modules 3 ways

# from turtle import *
# import turtle
# import turtle as t

# # higher order function

# def add(n1,n2):
#     return n1+n2

# def multiply(n1,n2):
#     return n1*n2

# def calculate(n1,n2,func):
#     return func(n1,n2)

# print(calculate(10,20,add))
# print(calculate(10,20,multiply))
