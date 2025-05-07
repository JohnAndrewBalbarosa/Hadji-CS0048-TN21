from random import random
from mp2function import *

listMenu = [
    "Play Number Guessing Game",
    "Exit"
    ]

def menu():
    while True:
        displayMenu(listMenu)
        try:
            match(menuPrompt(listMenu)):
                case 1:
                    play()
                case 2:
                    return
                case False:
                    return
                case "Error":
                    continue
        except:
            padding("Something happened so try again")
            continue

def play():
    answer = random.randint(1,100)
    try:
        choice = None
        attempt = None
        while answer != choice:
            choice = dataTypeInput("Guess the number", "int")
            attempt += attempt
            if answer > choice:
                print("Too high!")
            if answer < choice:
                print("Too low!")
            else:
                print(f"Congratulations! You guessed the number in {attempt} attempts.")
    except:
        print("Wrong data type input, try again!")
    
menu()
