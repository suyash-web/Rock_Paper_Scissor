print("*********************************************HELLO THERE***************************************************")
print("**********************************WELCOME TO STONE-PAPER-SCISSOR GAME*********************************")

import random

user_score = 0
computer_score = 0

li = ["rock", "paper", "scissor"]

while True:
    user_choice = input("Type Rock/Paper/Scissor or Q to quit:- ").lower()
    if user_choice == "q":
        quit()
    if user_choice not in li:
        continue

    ran_num = random.randint(0,2)

    computer_choice = li[ran_num]
    print("Computer's choice is", computer_choice + ".")

    if user_choice == "rock" and computer_choice == "scissor":
        print("You won!")
        user_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
        user_score += 1
    elif user_choice == "scissor" and computer_choice == "paper":
        print("You won!")
        user_score += 1
    else:
        print("You lost!")
        computer_score += 1

print("You won", user_score, "times.")
print("Computer won", computer_score, "times.")
print("Thanks for playing! GOODBYE!")