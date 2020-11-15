# This program assign tasks ramdomly
# Version 0.0

import TaskModule
import SprintModule
import datetime

class todoTask:
    def __init__(self, id, name, date):
        self.id = id
        self.name = name
        self.date = date

def PrintTodoList(todoListIn):
    print("----------------------------------------")
    print("Following tasks will done in this sprint")
    print("----------------------------------------")
    printedTasks = []
    for todo in todoListIn:
        if not todo.id in printedTasks:
            taskCount = sum(t.id == todo.id for t in todoListIn)
            print(todo.name, "-", taskCount, "times")
            printedTasks.append(todo.id)
    print("----------------------------------------")

if __name__ == "__main__":
    print('*******************************************************')
    print('****************Wellcome to TaskHunter.****************')
    print('*******************************************************')
    print('***You can sure that TaskHunter assigns tasks fairly***')
    print('*******************************************************')

    tasksFilePath = './tasks.txt'
    sprintFilePath = './sprint.txt'

    tasks = TaskModule.tasks(tasksFilePath)
    tasks.PrintTaskList()

    sprintInfo = SprintModule.sprint(sprintFilePath)
    sprintInfo.PrintSprintInfos()

    ## Create a todo list
    todoList = []
    for task in tasks.taskList:
        todoDate = task.lastDate + datetime.timedelta(days=task.period)
        while True:
            ## don't go on if todo date later than endDate
            if todoDate >= sprintInfo.endDate:
                break
            
            ## set start date to todo date if it is early than it
            if todoDate < sprintInfo.startDate:
                todoDate = sprintInfo.startDate

            newtodo = todoTask(task.id, task.name, todoDate)
            todoList.append(newtodo)
            todoDate = todoDate + datetime.timedelta(days=task.period)
    
    PrintTodoList(todoList)            