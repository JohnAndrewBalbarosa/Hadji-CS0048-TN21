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
            match(menuPrompt(listMenu))

def addScore(grades):
    pass

def calculateAverage(grades):
    pass