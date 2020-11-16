# This program assign tasks ramdomly
# Version 0.0

import TaskModule
import SprintModule
import datetime
import random

class todoTask:
    def __init__(self, id, date):
        self.id = id
        self.date = date
        self.assignedID = -1

class Person:
    def __init__(self, id, name, capacity):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.dayEffort = 0
        self.sprintEffort = 0
        self.actualEffort = 0

def GetPersonValue(peopleIn, id, varName):
    for p in peopleIn:
        if p.id == id:
            return getattr(p, varName)
    errorMessage = varName
    errorMessage += " couldn't be found in people. ID : "
    errorMessage += str(id)
    return errorMessage

def SetPersonValue(peopleIn, id, varName, val):
    for p in peopleIn:
        if p.id == id:
            return setattr(p, varName, val)
    errorMessage = varName
    errorMessage += " couldn't be found in people. ID : "
    errorMessage += str(id)
    return errorMessage

def CreateTodoList(todoListIn, tasksIn):
    for task in tasksIn.taskList:
        todoDate = task.lastDate + datetime.timedelta(days=task.period)
        while True:
            ## don't go on if todo date later than endDate
            if todoDate >= sprintInfo.endDate:
                break
            
            ## set start date to todo date if it is early than it
            if todoDate < sprintInfo.startDate:
                todoDate = sprintInfo.startDate

            newtodo = todoTask(task.id, todoDate)
            todoListIn.append(newtodo)
            todoDate = todoDate + datetime.timedelta(days=task.period)

def CalculateTodoEffort(todoListIn, tasksIn):
    totalEffort = 0
    for task in todoListIn:
        totalEffort += tasksIn.GetElemValue(task.id, "effort")
    return totalEffort

def splitEffort(totalEffortIn, peopleIn, sprintInfoIn):
    peoplecapacity = 0
    sprintDays = int((sprintInfoIn.endDate - sprintInfoIn.startDate).days)
    for person in peopleIn:
        peoplecapacity += GetPersonValue(peopleIn, person.id, "capacity")

    for person in peopleIn:
        cap = GetPersonValue(peopleIn, person.id, "capacity")
        sprintEff = (totalEffortIn*cap) / peoplecapacity
        SetPersonValue(peopleIn, person.id, "spritEffort", sprintEff)
        SetPersonValue(peopleIn, person.id, "dayEffort", sprintEff / sprintDays)
        print(GetPersonValue(peopleIn, person.id, "name") , ":", GetPersonValue(peopleIn, person.id, "spritEffort"), ":", GetPersonValue(peopleIn, person.id, "dayEffort"))

def PrintTodoList(todoListIn, tasksIn):
    print("----------------------------------------")
    print("Following tasks will done in this sprint")
    print("----------------------------------------")
    printedTasks = []
    for todo in todoListIn:
        if not todo.id in printedTasks:
            taskCount = sum(t.id == todo.id for t in todoListIn)
            print(tasksIn.GetElemValue(todo.id, "name"), "-", taskCount, "times")
            printedTasks.append(todo.id)
    print("----------------------------------------")

def RandomAssigner(todoListIn, peopleIn, sprintInfoIn, tasksIn):
    sprintDays = int((sprintInfoIn.endDate - sprintInfoIn.startDate).days)
    for day in range(sprintDays):
        currentDay = sprintInfoIn.startDate + datetime.timedelta(days=day)
        print("----------------------------------------")
        print(currentDay.strftime("%d/%m/%Y %A"))
        print("----------------------------------------")
        for todo in todoListIn:
            if todo.date != currentDay:
                continue

            taskEffort = tasksIn.GetElemValue(todo.id, "effort")
            isTaskAssigned = False
            for person in peopleIn:
                if person.dayEffort * (day + 1) * 1.5 > person.actualEffort + taskEffort:
                    todo.assignedID = person.id
                    person.actualEffort += taskEffort
                    peopleIn.sort(key=lambda x: x.actualEffort)
                    isTaskAssigned = True
                    print(tasksIn.GetElemValue(todo.id, "name"),"->\t", person.name)
                    break
            ## postpone task to next day if nobody assigned to it
            if not isTaskAssigned:
                todo.date = todo.date + datetime.timedelta(days=1)
    print("----------------------------------------")
    print("Total Efforts of people")
    for person in peopleIn:
        print(person.name,":",person.actualEffort)

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
    CreateTodoList(todoList, tasks)
    PrintTodoList(todoList, tasks)

    people = [Person(0,"Talha",100), Person(1,"Seda",100)]

    todoTotalEffort = CalculateTodoEffort(todoList, tasks)
    splitEffort(todoTotalEffort, people, sprintInfo)
    random.shuffle(people)

    RandomAssigner(todoList, people, sprintInfo, tasks)
