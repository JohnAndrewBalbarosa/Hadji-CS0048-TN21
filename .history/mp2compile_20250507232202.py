from mp2part1 import menu as menu1
from mp2part2 import menu as menu2
from mp2part3 import menu as menu3
from mp2part4 import menu as menu4 
from mp2part5 import menu as menu5
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
            displayMenu(listMenu)
            match(menuPrompt(listMenu)):
                case "Error":
                    return
                case False:
                    continue
                case 1:
                    menu1()
                case 2:
                    men2()
                case 3:
                    menu3()
                case 4:
                    menu4()
                case 5:
                    menu5()    
    except:
        padding("Something is wrong with the main menu. Shutting down!")
        return
main()