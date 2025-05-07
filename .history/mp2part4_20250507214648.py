from random import random
from mp2function import *

def menu():
    pass

def play():
    answer = random.randint(1,100)
    try:
        choice = dataTypeInput("Guess the number", "int")
        while answer != choice:
            if answer > choice:
                print("Too high")
    except:
        print("Wrong data type input, try again!")
        
