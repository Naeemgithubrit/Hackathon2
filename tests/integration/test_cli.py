"""
Integration tests for CLI functionality.
Tests the integration between the CLI interface and the business logic.
"""

import pytest
import io
import sys
import os
from unittest.mock import patch, MagicMock
# Add the src directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from src.main import (
    parse_command,
    handle_add,
    handle_view,
    handle_update,
    handle_delete,
    handle_complete,
    handle_incomplete,
    command_dispatcher,
    initialize_application,
    main
)
from src.todo import Todo


def test_parse_command_with_title_only():
    """Integration test for add command with title only."""
    command, args = parse_command('add "Test Title"')
    assert command == "add"
    assert args == ["Test Title"]


def test_parse_command_with_title_and_description():
    """Integration test for add command with title and description."""
    command, args = parse_command('add "Test Title" "Test Description"')
    assert command == "add"
    assert args == ["Test Title", "Test Description"]


def test_parse_command_with_missing_title():
    """Integration test for add command with missing title (error case)."""
    command, args = parse_command('add')
    assert command == "add"
    assert args == []


def test_handle_add_command_with_title_only():
    """Integration test for add command with title only."""
    todo_app = Todo()
    
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    handle_add(todo_app, ["Test Title"])
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert "Task added with ID: 1" in output
    
    # Verify task was added
    tasks = todo_app.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Test Title"
    assert tasks[0].description == ""


def test_handle_add_command_with_title_and_description():
    """Integration test for add command with title and description."""
    todo_app = Todo()
    
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    handle_add(todo_app, ["Test Title", "Test Description"])
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert "Task added with ID: 1" in output
    
    # Verify task was added
    tasks = todo_app.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Test Title"
    assert tasks[0].description == "Test Description"


def test_handle_add_command_with_missing_title():
    """Integration test for add command with missing title (error case)."""
    todo_app = Todo()
    
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    handle_add(todo_app, [])
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert "Error:" in output
    assert "Missing title" in output
    
    # Verify no task was added
    tasks = todo_app.get_all_tasks()
    assert len(tasks) == 0


def test_handle_view_command():
    """Integration test for view command."""
    todo_app = Todo()
    
    # Add a task first
    todo_app.add_task("Test Task", "Test Description")
    
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    handle_view(todo_app, [])
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert "Test Task" in output
    assert "Test Description" in output
    assert "ID: 1" in output


def test_handle_update_command_with_valid_id():
    """Integration test for update command with valid ID."""
    todo_app = Todo()
    
    # Add a task first
    todo_app.add_task("Original Title", "Original Description")
    
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    handle_update(todo_app, ["1", "New Title", "New Description"])
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert "Task 1 updated successfully" in output
    
    # Verify task was updated
    updated_task = todo_app.get_task_by_id(1)
    assert updated_task is not None
    assert updated_task.title == "New Title"
    assert updated_task.description == "New Description"


def test_handle_update_command_with_invalid_id():
    """Integration test for update command with invalid ID."""
    todo_app = Todo()
    
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    handle_update(todo_app, ["999", "New Title", "New Description"])
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert "Error:" in output
    assert "Task with ID 999 not found" in output


def test_handle_delete_command_with_valid_id():
    """Integration test for delete command with valid ID."""
    todo_app = Todo()
    
    # Add a task first
    todo_app.add_task("Test Task", "Test Description")
    assert len(todo_app.get_all_tasks()) == 1
    
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    handle_delete(todo_app, ["1"])
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert "Task 1 deleted successfully" in output
    
    # Verify task was deleted
    tasks = todo_app.get_all_tasks()
    assert len(tasks) == 0


def test_handle_delete_command_with_invalid_id():
    """Integration test for delete command with invalid ID."""
    todo_app = Todo()
    
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    handle_delete(todo_app, ["999"])
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert "Error:" in output
    assert "Task with ID 999 not found" in output


def test_handle_complete_command_with_valid_id():
    """Integration test for complete command with valid ID."""
    todo_app = Todo()
    
    # Add a task first
    todo_app.add_task("Test Task", "Test Description")
    task = todo_app.get_task_by_id(1)
    assert task is not None
    assert task.is_completed is False
    
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    handle_complete(todo_app, ["1"])
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert "Task 1 marked as complete" in output
    
    # Verify task was marked complete
    updated_task = todo_app.get_task_by_id(1)
    assert updated_task is not None
    assert updated_task.is_completed is True


def test_handle_complete_command_with_invalid_id():
    """Integration test for complete command with invalid ID."""
    todo_app = Todo()
    
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    handle_complete(todo_app, ["999"])
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert "Error:" in output
    assert "Task with ID 999 not found" in output


def test_handle_incomplete_command_with_valid_id():
    """Integration test for incomplete command with valid ID."""
    todo_app = Todo()
    
    # Add a task first and mark it as complete
    todo_app.add_task("Test Task", "Test Description")
    todo_app.mark_complete(1)
    task = todo_app.get_task_by_id(1)
    assert task is not None
    assert task.is_completed is True
    
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    handle_incomplete(todo_app, ["1"])
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert "Task 1 marked as incomplete" in output
    
    # Verify task was marked incomplete
    updated_task = todo_app.get_task_by_id(1)
    assert updated_task is not None
    assert updated_task.is_completed is False


def test_handle_incomplete_command_with_invalid_id():
    """Integration test for incomplete command with invalid ID."""
    todo_app = Todo()
    
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    handle_incomplete(todo_app, ["999"])
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert "Error:" in output
    assert "Task with ID 999 not found" in output


def test_command_dispatcher_with_help():
    """Test command dispatcher with help command."""
    todo_app = Todo()
    
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    command_dispatcher(todo_app, "help", [])
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert "Available Commands:" in output
    assert "add" in output
    assert "view" in output
    assert "update" in output


def test_command_dispatcher_with_unknown_command():
    """Test command dispatcher with unknown command."""
    todo_app = Todo()
    
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    command_dispatcher(todo_app, "unknowncommand", [])
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert "Error:" in output
    assert "Unknown command" in output


def test_initialize_application():
    """Test application initialization."""
    todo_app = initialize_application()
    assert isinstance(todo_app, Todo)
    assert todo_app.tasks == []
    assert todo_app.next_id == 1