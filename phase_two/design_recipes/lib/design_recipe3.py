# File: lib/design_recipe3.py

# Solution:
def isToDo(task):
    """Check if a task contains the string #TODO

    Parameters:
        str -- a task

    Returns:
        bool -- True if the string contains #TODO, else False

    Side effects:
        None
    """

    if "#TODO" in task:
        return True
    else:
        return False