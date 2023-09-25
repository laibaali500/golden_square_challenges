# File: lib.diary.py


class Diary():

    def __init__(self):
        self.entries = []

    def write(self, entry):
        # Allows diary entries to be stored
        # Parameters:
        #   entry: an instance of DiaryEntry
        self.entries.append(entry)

    def selectEntry(self, time: int, speed: int):
        # Calculates maximum amount of words to be read given reading time & speed,
        # and returns the first entry with less words than this
        # Parameters:
        #   time: the time the user has to read, in minutes
        #   speed: the average reading speed of the reader, in words per minute
        # Returns: 
        #   str -- a single entry
        wordsToRead = speed*time
        closest = self.entries[0] #closest is first entry by default

        for x in self.entries :
            closestWords = len(closest.contents.split()) # number of words for closest
            xWords = len(x.contents.split()) # number of words for current entry
            if closestWords < xWords < wordsToRead :
                closest = x

            return closest.contents
        
    def listContacts(self):
        # Returns a list of contacts (str)
        allContacts = [(f"{i.title} : {i.number}") for i in self.entries]
        return allContacts


class DiaryEntry():

    def __init__(self, title: str, contents: str, number: str):
        # Parameters:
        #   title
        #   contents
        #   number
        self.title = title
        self.contents = contents
        self.number = number

class TodoList():
    
    def __init__(self):
        self.todos = []

    def add_todo(self, todo):
        # Adds todos to the list of todos
        # Parameters:
        #   todo: an instance of Todo
        self.todos.append(todo)

    def completed(self):
        # Gathers all completed todos
        # Returns:
        #   list -- all completed todos

        return [i.task for i in self.todos if i.completed == True]

    def incompleted(self):
        # Gathers all incompleted todos
        # Returns:
        #   list -- all incompleted todos
        return [i.task for i in self.todos if i.completed == False]


class Todo():
    
    def __init__(self, task):
        self.task = task
        self.completed = False

    def markComplete(self):
        # Marks a todo object as completed
        self.completed = True