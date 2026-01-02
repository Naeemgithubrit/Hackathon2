#!/usr/bin/env python3
"""
Main entry point for the Basic Todo Console Application.
Implements the CLI interface with command parsing and dispatching.
"""

import sys
import re
import os
import importlib.util

# Dynamically import Todo based on whether we're running as a module or directly
try:
    # Try relative import first (when run as module)
    from .todo import Todo
except ImportError:
    # Fall back to absolute import (when run directly)
    from todo import Todo


def print_help():
    """Print help information showing available commands."""
    help_text = """
Available Commands:
  add "title" "description"     - Add a new task with title and optional description
  view                          - View all tasks with their status
  update id "new title" "new description" - Update task by ID
  delete id                     - Delete task by ID
  complete id                   - Mark task as complete by ID
  incomplete id                 - Mark task as incomplete by ID
  help                          - Show this help message
  exit or quit                  - Exit the application

Examples:
  add "Buy groceries" "Milk, bread, eggs"
  view
  update 1 "Buy groceries and cook dinner" "Milk, bread, eggs, chicken"
  delete 1
  complete 2
  incomplete 3
"""
    print(help_text)


def parse_command(user_input):
    """
    Parse user command and extract arguments.
    
    Args:
        user_input (str): Raw user input string
        
    Returns:
        tuple: (command, args) where command is the command string and args is a list of arguments
    """
    # Split the input by spaces, but keep quoted strings together
    pattern = r'"([^"]*)"|(\S+)'
    matches = re.findall(pattern, user_input.strip())
    
    # Extract the actual matched string from each tuple
    parts = [match[0] if match[0] else match[1] for match in matches]
    
    if not parts:
        return "", []
    
    command = parts[0].lower()
    args = parts[1:]
    
    return command, args


def handle_add(todo_app, args):
    """
    Handle the 'add' command to add a new task.
    
    Args:
        todo_app (Todo): The Todo application instance
        args (list): List of arguments for the command
    """
    if len(args) < 1:
        print("Error: Missing title")
        print('Usage: add "title" "description"')
        return
    
    title = args[0]
    description = args[1] if len(args) > 1 else ""
    
    try:
        task = todo_app.add_task(title, description)
        print(f"Task added with ID: {task.id}")
    except ValueError as e:
        print(f"Error: {e}")
        print('Usage: add "title" "description"')


def handle_view(todo_app, args):
    """
    Handle the 'view' command to display all tasks.
    
    Args:
        todo_app (Todo): The Todo application instance
        args (list): List of arguments for the command (should be empty)
    """
    if args:
        print("Warning: 'view' command takes no arguments")
    
    tasks = todo_app.get_all_tasks()
    
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        status_icon = "✔" if task.is_completed else "✖"
        print(f"ID: {task.id} | Title: {task.title} | Description: {task.description} | Status: {status_icon}")


def handle_update(todo_app, args):
    """
    Handle the 'update' command to update a task.
    
    Args:
        todo_app (Todo): The Todo application instance
        args (list): List of arguments for the command
    """
    if len(args) < 2:
        print("Error: Missing required arguments")
        print('Usage: update id "new title" "new description"')
        return
    
    try:
        task_id = int(args[0])
    except ValueError:
        print("Error: Invalid task ID. Task ID must be a number.")
        print('Usage: update id "new title" "new description"')
        return
    
    # Check if the task exists
    task = todo_app.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found")
        return
    
    # Prepare new title and description
    new_title = args[1] if len(args) > 1 and args[1] != "" else None
    new_description = args[2] if len(args) > 2 else None
    
    try:
        success = todo_app.update_task(task_id, new_title, new_description)
        if success:
            print(f"Task {task_id} updated successfully")
        else:
            print(f"Error: Failed to update task {task_id}")
    except ValueError as e:
        print(f"Error: {e}")
        print('Usage: update id "new title" "new description"')


def handle_delete(todo_app, args):
    """
    Handle the 'delete' command to delete a task.
    
    Args:
        todo_app (Todo): The Todo application instance
        args (list): List of arguments for the command
    """
    if len(args) != 1:
        print("Error: Invalid number of arguments")
        print("Usage: delete id")
        return
    
    try:
        task_id = int(args[0])
    except ValueError:
        print("Error: Invalid task ID. Task ID must be a number.")
        print("Usage: delete id")
        return
    
    # Check if the task exists
    task = todo_app.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found")
        return
    
    success = todo_app.delete_task(task_id)
    if success:
        print(f"Task {task_id} deleted successfully")
    else:
        print(f"Error: Failed to delete task {task_id}")


def handle_complete(todo_app, args):
    """
    Handle the 'complete' command to mark a task as complete.
    
    Args:
        todo_app (Todo): The Todo application instance
        args (list): List of arguments for the command
    """
    if len(args) != 1:
        print("Error: Invalid number of arguments")
        print("Usage: complete id")
        return
    
    try:
        task_id = int(args[0])
    except ValueError:
        print("Error: Invalid task ID. Task ID must be a number.")
        print("Usage: complete id")
        return
    
    # Check if the task exists
    task = todo_app.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found")
        return
    
    success = todo_app.mark_complete(task_id)
    if success:
        print(f"Task {task_id} marked as complete")
    else:
        print(f"Error: Failed to mark task {task_id} as complete")


def handle_incomplete(todo_app, args):
    """
    Handle the 'incomplete' command to mark a task as incomplete.
    
    Args:
        todo_app (Todo): The Todo application instance
        args (list): List of arguments for the command
    """
    if len(args) != 1:
        print("Error: Invalid number of arguments")
        print("Usage: incomplete id")
        return
    
    try:
        task_id = int(args[0])
    except ValueError:
        print("Error: Invalid task ID. Task ID must be a number.")
        print("Usage: incomplete id")
        return
    
    # Check if the task exists
    task = todo_app.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found")
        return
    
    success = todo_app.mark_incomplete(task_id)
    if success:
        print(f"Task {task_id} marked as incomplete")
    else:
        print(f"Error: Failed to mark task {task_id} as incomplete")


def command_dispatcher(todo_app, command, args):
    """
    Dispatch commands to their respective handlers.
    
    Args:
        todo_app (Todo): The Todo application instance
        command (str): The command to execute
        args (list): List of arguments for the command
    """
    if command in ["exit", "quit"]:
        print("Goodbye!")
        sys.exit(0)
    elif command == "help":
        print_help()
    elif command == "add":
        handle_add(todo_app, args)
    elif command == "view":
        handle_view(todo_app, args)
    elif command == "update":
        handle_update(todo_app, args)
    elif command == "delete":
        handle_delete(todo_app, args)
    elif command == "complete":
        handle_complete(todo_app, args)
    elif command == "incomplete":
        handle_incomplete(todo_app, args)
    else:
        print(f"Error: Unknown command '{command}'")
        print("Type 'help' for available commands")


def initialize_application():
    """
    Implement application initialization and startup sequence.
    
    Returns:
        Todo: The initialized Todo application instance
    """
    try:
        todo_app = Todo()
        print("Basic Todo Console Application initialized successfully!")
        print("Type 'help' for available commands or 'exit' to quit.")
        return todo_app
    except Exception as e:
        print(f"Error: Failed to initialize application - {e}")
        sys.exit(1)


def main():
    """
    Main application entry point and loop.
    Continues until exit command is received.
    """
    # Application initialization
    todo_app = initialize_application()
    
    # Main application loop
    while True:
        try:
            user_input = input("> ").strip()
            
            if not user_input:
                continue
                
            command, args = parse_command(user_input)
            command_dispatcher(todo_app, command, args)
            
        except KeyboardInterrupt:
            print("\nReceived interrupt signal. Exiting...")
            break
        except EOFError:
            print("\nEnd of input. Exiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("The application will continue running.")
    
    # Graceful shutdown
    print("Shutting down gracefully...")


if __name__ == "__main__":
    main()