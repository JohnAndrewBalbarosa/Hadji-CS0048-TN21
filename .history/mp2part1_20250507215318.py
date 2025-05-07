from mp2function import *

listOfMenu = [
    "Add",
    "Subtract",
    "Multiply",
    "Divide"
]

def menu():
    while True:
        result = 0
        displayMenu(listOfMenu)
        try:
            match(menuPrompt(listOfMenu)):
                case "Error":
                    
                case False:
                    return
                case 1:
                    result = add(twoInputs())
                case 2:
                    result = subtract(twoInputs())
                case 3:
                    result = multiply(twoInputs())
                case 4:
                    result = divide(twoInputs())
        except:
            continue
        print(f"Result: {result}")

def twoInputs():
    try:
        a = dataTypeInput("Enter first number: ", "int")
        b = dataTypeInput("Enter second number: ", "int")
        return a,b
    except :
        print("Not the correct data type. Try again.")

def add(num):

    total = 0
    for i in num:
        total += i
    return total 

def subtract(num):
    total = num[0]
    num = num[1:]
    for i in num:
        total -= i
    return total 

def multiply(num):
    total = num[0]
    num = num[1:]
    for i in num:
        total *= i
    return total 

def divide(num):
    total = num[0]
    num = num[1:]
    for i in num:
        total /= i
    return total


menu()