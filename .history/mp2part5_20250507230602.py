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
                    addScore(grades)
                case 2:
                    calculateAverage(grades)
    except:
        padding("Something Happened so please try again! ")

def addScore(grades):
    try:
        a = dataTypeInput("Enter the subject: ", "string")
        b = dataTypeInput("Enter the score:")

def calculateAverage(grades):
    pass