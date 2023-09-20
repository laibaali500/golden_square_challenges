## Function Design Recipe 3

## 1. Describe the Problem

_User story 3:_

> As a user
> So that I can keep track of my tasks
> I want to check if a text includes the string #TODO.

## 2. Design the Function Signature

_The name of the function, its parameters, return value, and side effects:_

```python
def isToDo(task):
    """Check if a task contains the string #TODO

    Parameters:
        str -- a task

    Returns:
        bool -- True if the string contains #TODO, else False

    Side effects:
        None
    """

    pass
```

## 3. Create Examples as Tests

_A list of examples of what the function will take and return._

```python
"""
Given a string "Check for bugs #TODO"
It returns True
"""
isToDo("Check for bugs #TODO") => (True)

"""
Given a string "Check for bugs"
It returns False
"""
isToDo("Check for bugs") => (False)

"""
Given a string "Check for bugs #todo"
It returns False
"""
isToDo("Check for bugs #todo") => (False)
```