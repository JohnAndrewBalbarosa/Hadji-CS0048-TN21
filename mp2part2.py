from mp2function import *

listOfMenu = [
    "Convert Celsius to Fahrenheit",
    "Convert Fahrenheit to Celsius"
]

def menu():
    while True:
        result = 0
        displayMenu(listOfMenu)
        match(menuPrompt(listOfMenu)):
            case "Error":
                continue
            case False:
                return
            case 1:
                result = cToF(dataTypeInput("Enter temperature in Celsius: ", "float"))
            case 2:
                result = fToC(dataTypeInput("Enter temperature in Celsius:", "float"))
        if (not result):
            print("Error please try again")
            continue
        print(f"Result: {result:.2f}")

def cToF(num):
    if (num == "Error"):
        return False
    return (num * 9/5) + 32

def fToC(num):
    if (num == "Error"):
        return False
    return (num - 32) * 5/9

menu()

