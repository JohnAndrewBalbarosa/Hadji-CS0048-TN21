from mp2function import *

listOfMenu = [
    "Convert Celsius to Fahrenheit",
    "Convert Fahrenheit to Celsius"
]

def menu():
    while True:
        result = 0
        displayMenu(listOfMenu)
        try:
            match(menuPrompt(listOfMenu)):
                case "Error":
                    continue
                case False:
                    return
                case 1:
                    result = cToF(dataTypeInput("Enter temperature in Celsius: ", "float"))
                case 2:
                    result = fToC(dataTypeInput("Enter temperature in Fahrenheit: ", "float"))
        except:
            print("Wrong data input, try again")
            continue
        print(f"Result: {result:.2f}")

def cToF(num):
    return (num * 9/5) + 32

def fToC(num):
    return (num - 32) * 5/9

menu()

