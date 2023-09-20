# File: lib/task_manager

class TaskManager():

    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        # Parameters:
        #   task: a task to be added to the list of tasks
        self.tasks.append(task)

    def mark_task(self, task: str):
        # Parameters:
        #   task: a task to be ticked off the list
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            raise Exception("No tasks to mark off.")

    def get_tasks(self):
        # Returns:
        #   str -- a list of tasks left to do, or, if there are none left, a message saying so
        if len(self.tasks) > 0:
            return '\n'.join(self.tasks)
        else:
            raise Exception("No tasks have been added.")