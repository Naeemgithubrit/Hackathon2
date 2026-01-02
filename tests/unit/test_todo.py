"""
Unit tests for Todo class.
Tests all functionality of the Todo class including task management operations.
"""

import pytest
import sys
import os
# Add the src directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from src.todo import Todo
from src.task import Task


def test_todo_initialization():
    """Test Todo class initialization."""
    todo = Todo()
    assert todo.tasks == []
    assert todo.next_id == 1


def test_todo_add_task_method_with_validation():
    """Unit test for Todo.add_task method with validation."""
    todo = Todo()
    
    # Test adding a valid task
    task = todo.add_task("Test Title")
    assert task.id == 1
    assert task.title == "Test Title"
    assert task.description == ""
    assert task.is_completed is False
    assert len(todo.tasks) == 1
    
    # Test adding a task with description
    task_with_desc = todo.add_task("Test Title 2", "Test Description")
    assert task_with_desc.id == 2
    assert task_with_desc.title == "Test Title 2"
    assert task_with_desc.description == "Test Description"
    assert task_with_desc.is_completed is False
    assert len(todo.tasks) == 2
    
    # Test adding a task with empty title (should raise ValueError)
    with pytest.raises(ValueError):
        todo.add_task("")
    
    # Test adding a task with whitespace-only title (should raise ValueError)
    with pytest.raises(ValueError):
        todo.add_task("   ")


def test_todo_get_all_tasks():
    """Test getting all tasks."""
    todo = Todo()
    
    # Initially should return empty list
    tasks = todo.get_all_tasks()
    assert tasks == []
    assert len(tasks) == 0
    
    # Add some tasks
    todo.add_task("Task 1")
    todo.add_task("Task 2", "Description for Task 2")
    
    # Get all tasks
    tasks = todo.get_all_tasks()
    assert len(tasks) == 2
    assert isinstance(tasks[0], Task)
    assert isinstance(tasks[1], Task)
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"
    
    # Verify that the returned list is a copy (modifying it doesn't affect internal storage)
    original_len = len(todo.get_all_tasks())
    tasks.append(Task(999, "Fake Task"))
    new_len = len(todo.get_all_tasks())
    assert original_len == new_len  # Internal storage unchanged


def test_todo_get_task_by_id():
    """Test getting a task by its ID."""
    todo = Todo()
    
    # Add some tasks
    task1 = todo.add_task("Task 1")
    task2 = todo.add_task("Task 2", "Description for Task 2")
    
    # Test getting existing tasks
    retrieved_task1 = todo.get_task_by_id(1)
    assert retrieved_task1 is not None
    assert retrieved_task1.id == 1
    assert retrieved_task1.title == "Task 1"
    
    retrieved_task2 = todo.get_task_by_id(2)
    assert retrieved_task2 is not None
    assert retrieved_task2.id == 2
    assert retrieved_task2.title == "Task 2"
    assert retrieved_task2.description == "Description for Task 2"
    
    # Test getting non-existing task
    retrieved_task_none = todo.get_task_by_id(999)
    assert retrieved_task_none is None


def test_todo_update_task():
    """Test updating a task."""
    todo = Todo()
    
    # Add a task
    task = todo.add_task("Original Title", "Original Description")
    assert task.title == "Original Title"
    assert task.description == "Original Description"
    
    # Update both title and description
    success = todo.update_task(1, "New Title", "New Description")
    assert success is True
    
    updated_task = todo.get_task_by_id(1)
    assert updated_task.title == "New Title"
    assert updated_task.description == "New Description"
    
    # Update only title
    success = todo.update_task(1, "Updated Again Title")
    assert success is True
    
    updated_task = todo.get_task_by_id(1)
    assert updated_task.title == "Updated Again Title"
    assert updated_task.description == "New Description"  # Should remain unchanged
    
    # Update only description
    success = todo.update_task(1, new_description="Updated Description")
    assert success is True
    
    updated_task = todo.get_task_by_id(1)
    assert updated_task.title == "Updated Again Title"  # Should remain unchanged
    assert updated_task.description == "Updated Description"
    
    # Try to update non-existing task
    success = todo.update_task(999, "New Title")
    assert success is False
    
    # Try to update with empty title (should raise ValueError)
    with pytest.raises(ValueError):
        todo.update_task(1, "")


def test_todo_delete_task():
    """Test deleting a task."""
    todo = Todo()
    
    # Add some tasks
    todo.add_task("Task 1")
    todo.add_task("Task 2")
    todo.add_task("Task 3")
    
    assert len(todo.tasks) == 3
    
    # Delete a task
    success = todo.delete_task(2)
    assert success is True
    assert len(todo.tasks) == 2
    
    # Verify task 2 is gone and others remain
    remaining_ids = [task.id for task in todo.tasks]
    assert 2 not in remaining_ids
    assert 1 in remaining_ids
    assert 3 in remaining_ids
    
    # Try to delete non-existing task
    success = todo.delete_task(999)
    assert success is False
    assert len(todo.tasks) == 2  # Count should remain the same


def test_todo_mark_complete():
    """Test marking a task as complete."""
    todo = Todo()
    
    # Add a task
    task = todo.add_task("Test Task")
    assert task.is_completed is False
    
    # Mark as complete
    success = todo.mark_complete(1)
    assert success is True
    
    completed_task = todo.get_task_by_id(1)
    assert completed_task.is_completed is True
    
    # Try to mark non-existing task as complete
    success = todo.mark_complete(999)
    assert success is False


def test_todo_mark_incomplete():
    """Test marking a task as incomplete."""
    todo = Todo()
    
    # Add a task and mark it as complete
    task = todo.add_task("Test Task")
    todo.mark_complete(1)
    assert task.is_completed is True
    
    # Mark as incomplete
    success = todo.mark_incomplete(1)
    assert success is True
    
    incomplete_task = todo.get_task_by_id(1)
    assert incomplete_task.is_completed is False
    
    # Try to mark non-existing task as incomplete
    success = todo.mark_incomplete(999)
    assert success is False


def test_auto_incrementing_id_generation():
    """Test that IDs are auto-incremented starting from 1."""
    todo = Todo()
    
    # Add several tasks and verify IDs
    task1 = todo.add_task("Task 1")
    assert task1.id == 1
    
    task2 = todo.add_task("Task 2")
    assert task2.id == 2
    
    task3 = todo.add_task("Task 3")
    assert task3.id == 3
    
    # Delete middle task and add another - ID should continue sequence
    todo.delete_task(2)
    task4 = todo.add_task("Task 4")
    assert task4.id == 4
    
    # Verify remaining tasks have correct IDs
    assert todo.get_task_by_id(1) is not None  # Task 1 still exists
    assert todo.get_task_by_id(2) is None     # Task 2 was deleted
    assert todo.get_task_by_id(3) is not None # Task 3 still exists
    assert todo.get_task_by_id(4) is not None # Task 4 was added