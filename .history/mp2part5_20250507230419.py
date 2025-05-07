from mp2function import *

listMenu = [
    "Add Score",
    "Calculate Average"
]

def menu():
    grades = {}
    try:
        while True:
            displayMenu(listMenu)
            match(menuPrompt(listMenu)):
                case "Error":
                    continue
                case False:
                    return
                case 1:
                    

def addScore(grades):
    pass

def calculateAverage(grades):
    pass