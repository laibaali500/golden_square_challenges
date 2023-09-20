## Function Design Recipe 4

## 1. Describe the Problem

_User story 4:_

> As a user  
> So that I can keep track of my tasks  
> I want a program that I can add todo tasks to and see a list of them.

> As a user  
> So that I can focus on tasks to complete  
> I want to mark tasks as complete and have them disappear from the list.


## 2. Design the Class Interface

```python
class TaskManager():

    def __init__(self):
        pass

    def add_task(self, task: str):
        # Parameters:
        #   task: a task to be added to the list of tasks
        pass

    def mark_task(self, task: str):
        # Parameters:
        #   task: a task to be ticked off the list
        pass

    def get_tasks(self):
        # Returns:
        #   str -- a list of tasks left to do, or, if there are none left, a message saying so
        pass
```

## 3. Create Examples as Tests

_A list of examples of what the function will take and return._

```python
"""
Given a task to be added
Getting tasks returns a list including this task
"""
manager = TaskManager()
manager.add_task("Vaccuum")
manager.get_tasks() => ("Vaccuum")

"""
Given tasks to be added
Getting tasks returns a list including these tasks
"""
manager = TaskManager()
manager.add_task("Vaccuum")
manager.add_task("Wash dishes")
manager.get_tasks() => ("""Vaccuum
                        Wash dishes""")

"""
Given a task to be added and marked off
Getting tasks returns no tasks
"""
manager = TaskManager()
manager.add_task("Vaccuum")
manager.add_task("Wash dishes")
manager.mark_task("Vaccuum")
manager.get_tasks() => ("Wash dishes")

"""
Given a task to be marked off
It returns an error if the task isn't in the list
"""
manager = TaskManager()
manager.mark_task("Vaccuum") => (ERROR -- "No tasks to mark off")

"""
Given no tasks to be added
Getting tasks returns an Exception with an error message
"""
manager = TaskManager()
manager.get_tasks() => (ERROR -- "No tasks have been added")
```