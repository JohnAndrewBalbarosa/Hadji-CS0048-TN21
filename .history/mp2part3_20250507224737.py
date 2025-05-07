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
        toRemove = dataTypeInput("Enter the task to remove, "   )

def viewTask(task):
    pass
