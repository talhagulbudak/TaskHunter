# Module : TaskModule.py
# This module reads tasks from a text file and stores them in an array
# Task Format : #{TASK_NAME},{TASK_PERIOD},{TASK_EFFORT},{TASK_LAST_DONE_DATE}

import datetime

minFeatureCount = 3
nameIndex = 0
periodIndex = 1
effortIndex = 2
lastDateIndex = 3

class task:
    def __init__(self, id, name, period, effort):
        self.id = id
        self.name = name
        self.period = period
        self.effort = effort
    def SetLastDate(self, lastDateStr):
        try:
            lastdate = datetime.datetime.strptime(lastDateStr, '%d/%m/%Y')
            self.lastDate = lastdate
        except ValueError:
            print("Format Error at last date of task : ", line)
            print("Date format should be DD/MM/YYYY")
            self.SetDefaultLastDate()
    def SetDefaultLastDate(self):
        self.lastDate = datetime.date.min

class tasks:
    def __init__(self, filePath):
        self.taskList = []

        f=open(filePath, "r")
        if f.mode == 'r':
            contents = f.read()
            contents_line = contents.splitlines()

            id = 0
            for line in contents_line:
                # check if it is commentouted line
                if line[0] == '#' :
                    continue
                
                taskInfos = line.split(',')
                
                ## dont add if infos are not compatible
                if not CheckTaskInfos(taskInfos):
                    continue
                
                # set features of task
                id += 1
                name=taskInfos[nameIndex]
                period=taskInfos[periodIndex]
                effort=taskInfos[effortIndex]

                myTask=task(id, name, period, effort)

                if len(taskInfos) > lastDateIndex :
                    myTask.SetLastDate(taskInfos[lastDateIndex])
                else :
                     myTask.SetDefaultLastDate()   

                self.taskList.append(myTask)
    def PrintTaskList(self):
        format_row = "{:>25}" * 5
        print(format_row.format("ID","NAME","PERIOD","EFFORT","LAST DATE"))
        for myTask in self.taskList :
            print(format_row.format(myTask.id,myTask.name,myTask.period,myTask.effort,myTask.lastDate.strftime("%m/%d/%Y")))
        


## check if task infos are compatible
def CheckTaskInfos(taskInfos) :
    ## check the feature count
    ## and don't create a task if feature count less then min
    if len(taskInfos) < minFeatureCount :
        print('Count Error at Task :')
        print(taskInfos)
        print('Task Format : TASK_NAME,TASK_PERIOD,TASK_EFFORT,[TASK_LAST_DONE_DATE](DD/MM/YYYY)')
        return False
                
    ## check the format of task
    if not taskInfos[periodIndex].isnumeric() or \
       not taskInfos[effortIndex].isnumeric() :
        print('Format Error at Task :')
        print(taskInfos)
        print('Task Format : TASK_NAME,TASK_PERIOD,TASK_EFFORT,[TASK_LAST_DONE_DATE](DD/MM/YYYY)')
        return False
    
    return True