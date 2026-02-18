"""
create a simple number guessing game
the user gets 10 chance to guess a number
if the user guess the number before 10 chances,stop asking the number and end the game with congrats message
if the user never gues the number then ask 10 times then end the game
"""

num = [12,10,3,4,8,9,70,11,5,6]
counter=1


while counter<=10:
    choice = int(input("Guess the number :"))
    if choice not in num:
        print("Oops You guessed Wrong ! Try again ")
        counter +=1
        continue
    else :
        print("congratulation ! the number is present in list")
        break
    

