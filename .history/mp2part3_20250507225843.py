from mp2function import *

listMenu = [
    "Add Task",
    "Remove Task",
    "View Tasks"
]


def menu():
    listTask = []
    try:
        while True:
            match(menuPrompt(listMenu)):
                case 1:
                    addTask(listTask)
                case 2:
                    removeTask(listTask)
                case 3:
                    viewTask(listTask)
                case False:
                    return
                case "Error":
                    continue
    except:
        padding("Something happened. Please try again!")
    

def addTask(task):
    try:
        added = dataTypeInput("Enter the task to add", "string")
        task.append(added)
    except:
        padding("Something just happened. Try again!")

def removeTask(task):
    try:
        toRemove = dataTypeInput("Enter the task to remove:" ,"string")
        index = task.index("toRemove")
        for i in task:
            if i == toRemove:
                task.pop(index)
                return
        else:
            print("Task not found")
    except:
        padding("Something just happened. Try again!")

def viewTask(task):
    padding("Veiwing all taks")
    for i in task:
        print(i)
