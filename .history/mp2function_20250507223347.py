def menuPrompt(menu, prompt = False):
    default =  f"Enter your choice (1 - {len(menu)}): "
    choice = input(prompt or default)
    try:
        idx = int(choice)
        size = len(menu)
        if 1 <= idx <= size:
            return idx
        if idx == size + 1:
            padding("Exiting this program. Returning to Main Menu")
            return False
        print("Invalid choice. Please try again.")
        return "Error"
    except ValueError:
        print("Not the correct data type. Try again.")
        return "Error"

#Funtion to enter choice for the menu
def dataTypeInput(prompt, type):
    choice = input(prompt)
    try:
        match(type):
            case "int":
                choice = int(choice)
            case "float":
                choice = float(choice)
            case "string":
                pass
            case _:
                print("Not an included data type")
                return False    
        return choice
    except ValueError:
        print("Not the correct data type. Try again.")
        return "Error"

# Function to display the menu
def displayMenu(menu):
    print("Menu:")
    for i in menu:
        print(f"    {i}")
    print(f"    Exit ")

# Padding for the output
def padding(title):
    print(f"---{title:^30}---")
