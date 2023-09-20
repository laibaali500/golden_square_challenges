# File: tests/test_task_manager

import pytest
from lib.task_manager import *

def test_task_manager_one_task():
    manager = TaskManager()
    manager.add_task("Vaccuum")
    result = manager.get_tasks()
    assert result == "Vaccuum"

def test_task_manager_two_tasks():
    manager = TaskManager()
    manager.add_task("Vaccuum")
    manager.add_task("Wash dishes")
    result = manager.get_tasks() 
    assert result == "Vaccuum\nWash dishes"

def test_task_manager_mark_tasks():
    manager = TaskManager()
    manager.add_task("Vaccuum")
    manager.add_task("Wash dishes")
    manager.mark_task("Vaccuum")
    result = manager.get_tasks()
    assert result == "Wash dishes"

def test_task_manager_no_tasks_error1():
    manager = TaskManager()
    with pytest.raises(Exception) as e:
        result = manager.mark_task("Vaccuum")
    error_message = str(e.value)
    assert error_message == ("No tasks to mark off.")

def test_task_manager_no_tasks_error2():
    manager = TaskManager()
    with pytest.raises(Exception) as e:
        result = manager.get_tasks()
    error_message = str(e.value)
    assert error_message == "No tasks have been added."