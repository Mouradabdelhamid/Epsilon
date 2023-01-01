# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 20:34:51 2023

@author: moura
"""
import random
mlist = [1,2,3]
random.choice(mlist)

choices = {
    1:'rock',
    2:'paper',
    3:'scissors'
}  
computer_choices = [1, 2, 3]

while True:
    invalid_input = True
    while invalid_input:
        print('Please chose one of the following choices: 1 = rock, 2 = paper, 3 = scissors.')
        choice_of_user = input('Your turn: ')
        if choice_of_user.isdigit():
            choice_of_user = int(choice_of_user)
            if choice_of_user in computer_choices:
                invalid_input = False
                print(choices[choice_of_user])
            else:
                print('Oops! Your number is not valid. Please enter a number from 1 to 3 : 1 = rock, 2 = paper, 3 = scissors.')
        else:
            print('Please enter numbers only!')

    choice_of_user_name = choices[choice_of_user]
    print(f'The user chose {choice_of_user_name}.')
    computer_choices.remove(choice_of_user)

    choice_of_computer = random.choice(computer_choices)
    choice_of_computer_name = choices[choice_of_computer]
    print(f'The computer chose {choice_of_computer_name}.')

    if (choice_of_user == 1 and choice_of_computer == 2) or (choice_of_user == 2 and choice_of_computer == 1 ):
        print('Paper wins')
        win_result = "paper"
    elif(choice_of_user == 1 and choice_of_computer == 3) or (choice_of_user == 3 and choice_of_computer ==1):
        print('Rock wins')
        win_result = "rock"
    else:
        print('Scissor wins')
        win_result = "scissors"

    if win_result == choice_of_user_name:
        print("Congrats, you win")
    else:
        print("The computer wins, try again")

    ans = input("Do you want to play again? ")
    if ans.lower() == "n":
        break
    