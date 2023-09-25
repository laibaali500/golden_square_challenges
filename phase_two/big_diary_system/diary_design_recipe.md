# Multi-Class Planned Design Recipe

## 1. Describe the Problem

> As a user  
> So that I can record my experiences  
> I want to keep a regular diary

> As a user  
> So that I can reflect on my experiences  
> I want to read my past diary entries 

> As a user  
> So that I can reflect on my experiences in my busy day  
> I want to select diary entries to read based on how much time I have and my
> reading speed

> As a user  
> So that I can keep track of my tasks  
> I want to keep a todo list along with my diary

> As a user  
> So that I can keep track of my contacts  
> I want to see a list of all of the mobile phone numbers in all my diary
> entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

_Also design the interface of each class in more detail._

```python

class Diary():

    def __init__(self):
        pass

    def write(self, entry):
        # Allows diary entries to be stored
        # Parameters:
        #   entry: an instance of DiaryEntry
        pass

    def selectEntry(self, time: int, speed: int):
        # Calculates maximum amount of words to be read given reading time & speed,
        # and returns the first entry with less words than this
        # Parameters:
        #   time: the time the user has to read, in minutes
        #   speed: the average reading speed of the reader, in words per minute
        # Returns: 
        #   str -- a single entry
        pass

    def listContacts(self):
        # Returns a list of contacts (str)
        pass



class DiaryEntry():

    def __init__(self, title: str, contents: str, number: str):
        # Parameters:
        #   title
        #   contents
        #   number
        pass



class TodoList():
    
    def __init__(self):
        pass

    def add_todo(self, todo):
        # Adds todos to the list of todos
        # Parameters:
        #   todo: an instance of Todo

    def completed(self):
        # Gathers all completed todos
        # Returns:
        #   list -- all completed todos

        pass

    def incompleted(self):
        # Gathers all incompleted todos
        # Returns:
        #   list -- all incompleted todos
        pass


class Todo():
    
    def __init__(self, task):
        pass

    def markComplete(self):
        # Marks a todo object as completed
        pass
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

```

_Encode each example as a test. You can add to the above list as you go._