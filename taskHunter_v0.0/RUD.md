# Requirement Understanding Document of TaskHunter V0.0

## Requirements

- tasks.txt
	- User creates it firstly, and can edit it any time
	- Tool can update of tasks lates date. When was it did lates
- people.txt
	- Only user can create and edit it.
- sprints.txt
	- Tool creates it according to users input
	- It keeps sprint duration, start and finish dates of current sprint.

## Use Case

```plantuml
@startuml

User -> (Create tasks.txt) : Manually
User -> (Create people.txt) : Manually
User --> (Define sprint durations) : TaskHunter
User --> (Create sprints task plan) : TaskHunter
User --> (Reset sprints) : TaskHunter

@enduml
```

## Sequance Diagram

```plantuml
@startuml
actor User

User -> Initialize : Run TaskHunter
activate Initialize
alt if sprints.txt is empty
    Initialize->User: Get sprint duration and start date
	User->Initialize: Set sprint duration and start date
end
deactivate Initialize

User -> TaskSpliter : Get Sprint Plan
activate TaskSpliter
TaskSpliter -> User : Return SprintXXX excel
deactivate TaskSpliter

@enduml
```