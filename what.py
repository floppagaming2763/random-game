# a remake of a (bad) random number game
import random

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

number = random.randrange(1,10)
while True:
    answer = input("guess the number ")
    if has_numbers(answer) == False:
        print("thats not a number")
    elif int(answer) < number:
        print("too low, try again")
    elif int(answer) > number:
        print("too high, try again")
    elif int(answer) == number:
        print("correct")
        break

