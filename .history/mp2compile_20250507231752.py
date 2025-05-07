from mp2part1 import menu
from mp2part2 import menu
from mp2part3 import menu
from mp2part4 import menu
from mp2part5 import menu
from mp2function import *

listMenu = [
    "Simple Calculator",
    "Temperature Converter",
    "To-Do List",
    "Number Guessing Game",
    "Student Grade Calculator"
]

def main():
    try:
        while True:
            match(menuPrompt):
                case "Error":
                    return
                case False:
                    continue
                case 1:
                    mp2part1.menu()
                case 2:
                    mp2part2.menu()
                case 3:
                    mp2part3.menu()
                case 4:
                    mp2part4.menu()
                case 5:
                    mp2part5.menu()    
    except:
        padding("Something is wrong with the main menu. Shutting down!")
        return main