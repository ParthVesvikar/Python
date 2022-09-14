import random

import random2

choices = ['rock', 'paper', 'scissor']
user_choice = int(input('Enter the option \n'))
print(choices[user_choice])
computer_choice = random.randint(0, 2)
print(choices[computer_choice])
if user_choice<0 and user_choice>=3:
    print("invalid.")
elif user_choice == 0 and computer_choice == 2:
    print("User won!!")
elif computer_choice == 0 and user_choice == 2:
    print("User lose!!")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You won")
elif user_choice == computer_choice:
    print("I's a draw")
