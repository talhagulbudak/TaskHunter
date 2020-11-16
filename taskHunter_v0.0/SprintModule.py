# Module : SprintModule.py
# This module can read sprints from a text file, can create new sprint file with user inputs and can update sprint file
# Sprint Format : {SPRINT_DURATION},{NEXT_SPRINT_START_DATE}

from enum import Enum
import time
import datetime
import calendar
import sys

### Enum for sprint info types
class SInfos(Enum):
    DURATION    = 0
    STARTDATE   = 1
    MAXVALUE    = 2

# Enum for duration types
class SDurations(Enum):
    FIRSTVALUE  = 0
    ONEWEEK     = 1
    TWOWEEK     = 2
    ONEMONTH    = 3
    MAXVALUE    = 4

class sprint:
    def __init__(self, filePath):
        ## Firstly read the sprint file and if it is empty or corrupted
        ## Create new file with user inputs
        self.filePath = filePath
        if not self.ReadSprintMap():
            while not self.CreateSprintMap():
                time.sleep(1)
            self.SaveSprintMap()

        if self.duration == SDurations.ONEWEEK.value:
            self.endDate = self.startDate + datetime.timedelta(days=7)
        elif self.duration == SDurations.TWOWEEK.value:
            self.endDate = self.startDate + datetime.timedelta(days=14)
        elif self.duration == SDurations.ONEMONTH.value:
            days_in_month = calendar.monthrange(self.startDate.year, self.startDate.month)[1]
            self.endDate = self.startDate + datetime.timedelta(days=days_in_month)
        else:
            print("Wrong Duration :", self.duration)
            sys.exit()
    ## This funstion gets sprint duration and first sprint start date form user
    ## It stores infos at self.duration and self.startDate variables
    def CreateSprintMap(self):
        print("Select a sprint duration :")
        for i in range(SDurations.FIRSTVALUE.value + 1, SDurations.MAXVALUE.value):
            print(SDurations(i).value, ":", SDurations(i).name)
        
        ## Set duration if it is in the duration types range            
        try:
            duration = int(input())
            if duration < SDurations.MAXVALUE.value and duration > SDurations.FIRSTVALUE.value:
                print(SDurations(duration).name, "is selected")
                self.duration = duration
            else:
                print("Value should be in range :", SDurations.FIRSTVALUE.value + 1, "-", SDurations.MAXVALUE.value - 1)
                return False
        except:
            print("Value should be in range :", SDurations.FIRSTVALUE.value + 1, "-", SDurations.MAXVALUE.value - 1)
            return False

        ## Set Start Date if it is a valid date
        dateStr = input('Enter First Sprint Start Date (DD/MM/YYYY) :')
        try:
            self.startDate = datetime.datetime.strptime(dateStr, '%d/%m/%Y')
        except ValueError:
            print("Incorrect format")
            return False
        
        return True

    ## This function writes duration and start date infos to a file.
    def SaveSprintMap(self):
        data = str(self.duration)
        data += ","
        data += self.startDate.strftime("%d/%m/%Y")
        f = open(self.filePath, "w")
        f.write(data)
        f.close()
    
    ## This function reads duration and start date infos from file 
    ## and restore them at self.duraion and self.startDate variables
    def ReadSprintMap(self):        
        f=open(self.filePath, "r")
        if f.mode == 'r':
            contents = f.read()
            contents_line = contents.splitlines()

            ## Only first line is important for us
            if len(contents_line) < 1 :
                print("sprint.txt is empty")
                return False

            line = contents_line[0]

            sprintInfos = line.split(',')

            ## dont add if infos are not compatible
            if not CheckSprintInfos(sprintInfos):
                return False

            # set features of task
            self.duration=int(sprintInfos[SInfos.DURATION.value])

            dateStr = sprintInfos[SInfos.STARTDATE.value]
            try:
                self.startDate = datetime.datetime.strptime(dateStr, '%d/%m/%Y')
            except ValueError:
                print("Incorrect format")
                return False
            
            return True

    def PrintSprintInfos(self):
        print("DURATION\t:", SDurations(self.duration).name, "\nSTART DATE\t:", self.startDate, "\nEND DATE\t:", self.endDate)


## check if sprint infos are compatible
def CheckSprintInfos(sprintInfos) :
    ## check the feature count
    ## and don't create a sprint if feature count less then min
    if len(sprintInfos) < SInfos.MAXVALUE.value :
        print('Count Error at Sprint Infos :')
        print(sprintInfos)
        return False
                
    ## check the format of task
    if not sprintInfos[SInfos.DURATION.value].isnumeric() :
        print('Format Error at Sprint Info :')
        print(sprintInfos)
        return False
    
    return True