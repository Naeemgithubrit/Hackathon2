"""
Unit tests for Task model.
Tests all functionality of the Task class including initialization, validation, and state management.
"""

import pytest
import sys
import os
# Add the src directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from src.task import Task


def test_task_creation_with_required_title_validation():
    """Unit test for Task creation with required title validation."""
    # Valid title should work
    task = Task(1, "Valid Title")
    assert task.title == "Valid Title"
    
    # Empty title should raise ValueError
    with pytest.raises(ValueError):
        Task(2, "")
    
    # Whitespace-only title should raise ValueError
    with pytest.raises(ValueError):
        Task(3, "   ")
    
    # Title with leading/trailing whitespace should be stripped
    task_with_spaces = Task(4, "  Title With Spaces  ")
    assert task_with_spaces.title == "Title With Spaces"


def test_task_creation_with_optional_description():
    """Unit test for Task creation with optional description."""
    # Task with description
    task_with_desc = Task(1, "Title", "Description")
    assert task_with_desc.title == "Title"
    assert task_with_desc.description == "Description"
    
    # Task without description (should default to empty string)
    task_without_desc = Task(2, "Title")
    assert task_without_desc.title == "Title"
    assert task_without_desc.description == ""
    
    # Task with empty description
    task_empty_desc = Task(3, "Title", "")
    assert task_empty_desc.title == "Title"
    assert task_empty_desc.description == ""


def test_task_creation_with_default_incomplete_status():
    """Unit test for Task creation with default incomplete status."""
    task = Task(1, "Title")
    assert task.is_completed is False
    
    # Also test that we can explicitly set completed status
    completed_task = Task(2, "Title", "Description", True)
    assert completed_task.is_completed is True
    
    # And that we can explicitly set incomplete status
    incomplete_task = Task(3, "Title", "Description", False)
    assert incomplete_task.is_completed is False


def test_task_str_representation():
    """Test string representation of Task."""
    task = Task(1, "Test Title", "Test Description", False)
    str_repr = str(task)
    assert "ID: 1" in str_repr
    assert "Title: Test Title" in str_repr
    assert "Description: Test Description" in str_repr
    assert "Status: ✖ Incomplete" in str_repr
    
    completed_task = Task(2, "Test Title", "Test Description", True)
    str_repr_completed = str(completed_task)
    assert "Status: ✔ Complete" in str_repr_completed


def test_task_repr_representation():
    """Test developer-friendly representation of Task."""
    task = Task(1, "Test Title", "Test Description", False)
    repr_str = repr(task)
    assert "Task(id=1, title='Test Title', description='Test Description', is_completed=False)" in repr_str


def test_task_to_dict():
    """Test conversion of Task to dictionary."""
    task = Task(1, "Test Title", "Test Description", True)
    task_dict = task.to_dict()
    
    expected_dict = {
        'id': 1,
        'title': 'Test Title',
        'description': 'Test Description',
        'is_completed': True
    }
    
    assert task_dict == expected_dict


def test_task_mark_complete():
    """Test marking a task as complete."""
    task = Task(1, "Test Title", "Test Description", False)
    assert task.is_completed is False
    
    task.mark_complete()
    assert task.is_completed is True


def test_task_mark_incomplete():
    """Test marking a task as incomplete."""
    task = Task(1, "Test Title", "Test Description", True)
    assert task.is_completed is True
    
    task.mark_incomplete()
    assert task.is_completed is False