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
                print("Too high!")
            if answer < choice:
                print("Too low!")
            else:
                print("Corre")
    except:
        print("Wrong data type input, try again!")
        
