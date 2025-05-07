from mp2part1 import menu
from mp2part2 import menu
from mp2part3 import menu
from mp2part4 import menu
from mp2part5 import menu
from mp2function import *

listMenu = [
    "",
    "To-Do List",
    "Number Guessing Game",
    "Student Grade Calculator"
]

def main():
    try:
        while True:
            match(menuPrompt)
    except:
        padding("Something is wrong with the main menu. Shutting down!")
        return main