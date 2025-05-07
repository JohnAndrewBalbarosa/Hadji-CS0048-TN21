from random import randint
from mp2function import *

listMenu = [
    "Play Number Guessing Game"
    ]

def menu():
    while True:
        displayMenu(listMenu)
        try:
            match(menuPrompt(listMenu)):
                case 1:
                    play()
                case False:
                    return
                case "Error":
                    continue
        except:
            padding("Something happened so try again")
            continue

def play():
    answer = randint(1,100)
    try:
        choice = None
        attempt = 0
        while answer != choice:
            choice = dataTypeInput("Guess the number: ", "int")
            attempt += 1
            if choice > answer:
                print("Too high!")
            if choice < answer:
                print("Too low!")
            else:
                print(f"Congratulations! You guessed the number in {attempt} attempts.")
    except:
        print("Wrong data type input, try again!")
    
menu()
