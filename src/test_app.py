#!/usr/bin/env python3
"""
Simple test script to verify the application functionality
"""

import sys
import os

# Add the parent directory to the path so we can import the modules
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

try:
    # Try relative import first (when run as module)
    from .todo import Todo
    from .task import Task
except ImportError:
    # Fall back to absolute import (when run directly)
    from todo import Todo
    from task import Task

def test_basic_functionality():
    """Test the basic functionality of the Todo app."""
    print("Testing basic functionality...")
    
    # Initialize the app
    todo = Todo()
    
    # Test adding tasks
    print("1. Testing add_task functionality...")
    task1 = todo.add_task("Test Task 1", "Description for task 1")
    task2 = todo.add_task("Test Task 2")
    
    assert task1.id == 1
    assert task1.title == "Test Task 1"
    assert task1.description == "Description for task 1"
    assert task1.is_completed == False
    
    assert task2.id == 2
    assert task2.title == "Test Task 2"
    assert task2.description == ""
    assert task2.is_completed == False
    
    print("   [PASS] Add task functionality works correctly")
    
    # Test getting all tasks
    print("2. Testing get_all_tasks functionality...")
    all_tasks = todo.get_all_tasks()
    assert len(all_tasks) == 2
    assert all_tasks[0].id == 1
    assert all_tasks[1].id == 2
    print("   [PASS] Get all tasks functionality works correctly")

    # Test getting task by ID
    print("3. Testing get_task_by_id functionality...")
    retrieved_task = todo.get_task_by_id(1)
    assert retrieved_task is not None
    assert retrieved_task.title == "Test Task 1"
    print("   [PASS] Get task by ID functionality works correctly")

    # Test updating tasks
    print("4. Testing update_task functionality...")
    success = todo.update_task(1, "Updated Task 1", "Updated description")
    assert success == True

    updated_task = todo.get_task_by_id(1)
    assert updated_task.title == "Updated Task 1"
    assert updated_task.description == "Updated description"
    print("   [PASS] Update task functionality works correctly")

    # Test marking complete/incomplete
    print("5. Testing mark_complete/mark_incomplete functionality...")
    assert todo.mark_complete(1) == True
    completed_task = todo.get_task_by_id(1)
    assert completed_task.is_completed == True

    assert todo.mark_incomplete(1) == True
    incomplete_task = todo.get_task_by_id(1)
    assert incomplete_task.is_completed == False
    print("   [PASS] Mark complete/incomplete functionality works correctly")

    # Test deleting tasks
    print("6. Testing delete_task functionality...")
    assert len(todo.get_all_tasks()) == 2
    success = todo.delete_task(1)
    assert success == True
    assert len(todo.get_all_tasks()) == 1
    print("   [PASS] Delete task functionality works correctly")

    print("\n[ALL PASS] All basic functionality tests passed!")


def test_error_handling():
    """Test error handling functionality."""
    print("\nTesting error handling...")
    
    todo = Todo()
    
    # Test adding task with empty title (should raise ValueError)
    print("1. Testing error handling for empty title...")
    try:
        todo.add_task("")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("   [PASS] Empty title validation works correctly")

    # Test updating with empty title (should raise ValueError)
    print("2. Testing error handling for empty title in update...")
    task = todo.add_task("Valid Task")
    try:
        todo.update_task(task.id, "")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("   [PASS] Empty title validation in update works correctly")

    # Test operations on non-existent task IDs
    print("3. Testing operations on non-existent task IDs...")
    assert todo.get_task_by_id(999) is None
    assert todo.update_task(999, "New Title") is False
    assert todo.delete_task(999) is False
    assert todo.mark_complete(999) is False
    assert todo.mark_incomplete(999) is False
    print("   [PASS] Non-existent task ID handling works correctly")
    
    print("\n[ALL PASS] All error handling tests passed!")


if __name__ == "__main__":
    test_basic_functionality()
    test_error_handling()
    print("\n[SUCCESS] All tests passed! The application is working correctly.")