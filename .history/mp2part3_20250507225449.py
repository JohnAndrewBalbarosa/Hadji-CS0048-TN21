from mp2function import *

listMenu = [
    "Add Task",
    "Remove Task",
    "View Tasks"
]


def menu():
    listTask = []
    
    

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
    pass
