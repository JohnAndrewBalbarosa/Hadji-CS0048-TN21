from random import random
from mp2function import *

def menu():
    pass

def play():
    answer = random.randint(1,100)
    try:
        dataTypeInput("Guess the number", "int")
    except:
        
