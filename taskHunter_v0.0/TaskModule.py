# Module : TaskModule.py
# This module reads tasks from a text file and stores them in an array
# Task Format : #{TASK_NAME},{TASK_PERIOD},{TASK_EFFORT},{TASK_LAST_DONE_DATE}

from enum import Enum
import datetime

### Enum for task info types
class TInfos(Enum):
    NAME        = 0
    PERIOD      = 1
    EFFORT      = 2
    LASTDATE    = 3
    MAXVALUE    = 4

minFeatureCount = TInfos.MAXVALUE.value - 1
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
        self.lastDate = datetime.datetime.min

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
                name=taskInfos[TInfos.NAME.value]
                period=int(taskInfos[TInfos.PERIOD.value])
                effort=int(taskInfos[TInfos.EFFORT.value])

                myTask=task(id, name, period, effort)

                if len(taskInfos) > TInfos.LASTDATE.value :
                    myTask.SetLastDate(taskInfos[TInfos.LASTDATE.value])
                else :
                     myTask.SetDefaultLastDate()  

                self.taskList.append(myTask)
    def PrintTaskList(self):
        format_row = "{:>25}" * 5
        print(format_row.format("ID","NAME","PERIOD","EFFORT","LAST DATE"))
        for myTask in self.taskList :
            print(format_row.format(myTask.id,myTask.name,myTask.period,myTask.effort,myTask.lastDate.strftime("%d/%m/%Y")))
        


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
    if not taskInfos[TInfos.PERIOD.value].isnumeric() or \
       not taskInfos[TInfos.EFFORT.value].isnumeric() :
        print('Format Error at Task :')
        print(taskInfos)
        print('Task Format : TASK_NAME,TASK_PERIOD,TASK_EFFORT,[TASK_LAST_DONE_DATE](DD/MM/YYYY)')
        return False
    
    return True