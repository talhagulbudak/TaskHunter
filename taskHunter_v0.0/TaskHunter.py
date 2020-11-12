# This program assign tasks ramdomly
# Version 0.0

import TaskModule
import SprintModule

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
