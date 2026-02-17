"""
a die has 6 faces with number 1 to 6 written on them
program should randomly written numbers between 1 to 6
"""

import random
print("Welcome to the game !!\nPlease follow instructions")

while True:
    user_input = input("Press Enter to roll a die or q to exit : ")
    user_input = user_input.strip()
    if user_input == "q":
      print("Thank you participating! Bye !")
      break
    elif user_input == '':
      number = random.randint(1,6)
      print(f"Your number is {number}")
    else:
      print("Invalid Input")

print("Thank you for participating !! GAME OVER !!")