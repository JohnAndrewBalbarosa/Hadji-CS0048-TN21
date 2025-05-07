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
        b = dataTypeInput("Enter the score:", "float")
        grades[a] = b
    except:
        print("Wrong data type input")
        return

def calculateAverage(grades):
    try:
        total = sum(grades.values())
        print(f"{total/len(grades)}")
    except:
        print("Wrong data type input")
        return