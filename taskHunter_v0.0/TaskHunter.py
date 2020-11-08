# This program assign tasks ramdomly
# Version 0.0

import TaskModule

if __name__ == "__main__":
    print('*******************************************************')
    print('****************Wellcome to TaskHunter.****************')
    print('*******************************************************')
    print('***You can sure that TaskHunter assigns tasks fairly***')
    print('*******************************************************')

tasksFilePath = './tasks.txt'
tasks = TaskModule.tasks(tasksFilePath)
tasks.PrintTaskList()
