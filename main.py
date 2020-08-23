from os import system, name
from task import Task
import json

class Main:

    def __init__(self):
        self.exit = bool(False)
        self.tasksList = []
        with open('tasks.json', 'r') as tasksFile:
            tasksStr = json.loads(tasksFile.read())
            for str in tasksStr:
                self.createTask(str)
            del tasksStr
            tasksFile.close()
        while self.exit == bool(False):
            if self.exit == bool(True):
                break
            self.actionsList(input())

    def clearConsole(self): 
        if name == 'nt': 
            _ = system('cls')
        else: 
            _ = system('clear')

    def exitAction(self):
        self.exit = bool(True)

    def showHelp(self):
        print("""List of commands:
    add [task] - to add new task into your list
    remove|rm [task number] - to remove task from your list
    show - to see list of your tasks
    exit - to exit the programm
        """)

    def writeTasksToFile(self):
        with open('tasks.json', 'w') as tasksFile:
            tasksStr = []
            for task in self.tasksList:
                tasksStr.append(task.taskString)
            tasksFile.write(json.dumps(tasksStr))
            del tasksStr
            tasksFile.close()

    def createTask(self, taskString):
        print("Task created: " + taskString)
        self.tasksList.append(Task(taskString))
        self.writeTasksToFile()

    def removeTask(self, identifier):
        try:
            print("'" + self.tasksList[int(identifier)-1].taskString + "' has been removed")
            self.tasksList.pop(int(identifier)-1)
            self.writeTasksToFile()
        except:
            print("Please enter valid task identification number!")

    def showTasksList(self):
        if len(self.tasksList) < 1:
            print("Your tasks list is empty! Type 'add [task]' to add task.")
        else:
            print('List of your tasks:')
            i = 1
            for task in self.tasksList:
                print("     " + str(i) + " - " + task.taskString)
                i += 1

    def actionsList(self, action):
        if action == "exit":
            self.exitAction()
        elif action == "help":
            self.showHelp()
        elif action == "show":
            self.showTasksList()
        elif str(action)[0:4] == "add " and str(action)[4:] != '':
            self.createTask(action[4:])
        elif str(action)[0:7] == "remove " and str(action)[7:] != '':
            self.removeTask(action[7:])
        elif str(action)[0:3] == "rm " and str(action)[3:] != '':
            self.removeTask(action[3:])
        else:
            print("Please enter command in valid format (type 'help' for help)")

Main()