from mp2function import *

listMenu = [
    "Add Task",
    "Remove Task",
    "View Tasks"
]


def menu():
    listTask = []
    
    

def addTask(task):
    added = dataTypeInput("Enter the task to add", "string")
    if added == "Error":
        return
    task.append(added)

def removeTask(task):
    pass

def viewTask(task):
    pass
