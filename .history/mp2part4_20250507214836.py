from random import random
from mp2function import *

def menu():
    pass

def play():
    answer = random.randint(1,100)
    try:
        choice = None
        attempt = None
        while answer != choice:
            choice = dataTypeInput("Guess the number", "int")
            if answer > choice:
                print("Too high!")
            if answer < choice:
                print("Too low!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
    except:
        print("Wrong data type input, try again!")
        
