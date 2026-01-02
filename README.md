# Basic Todo Console Application

A simple command-line interface application for managing tasks in memory. This application allows users to perform the five core operations: add, view, update, delete, and mark tasks as complete/incomplete.

## Features

- Add new tasks with required title and optional description
- View all tasks with their ID, title, description, and completion status
- Update task details (title and/or description) by ID
- Delete tasks by ID
- Mark tasks as complete or incomplete by ID
- In-memory storage (no persistence to files or databases)
- Command-line interface for easy interaction
- Comprehensive error handling for invalid inputs

## Prerequisites

- Python 3.13+ installed on your system
- Basic command line familiarity

## Setup

1. Clone or download the project files
2. Navigate to the project directory in your command line
3. No additional installation required - pure Python implementation

## Running the Application

From the project root directory:

```bash
python -m src.main
```

Or navigate to the src directory and run:

```bash
cd src
python main.py
```

## Available Commands

- `add "title" "description"` - Add a new task with title and optional description
- `view` - View all tasks with their status
- `update id "new title" "new description"` - Update task by ID
- `delete id` - Delete task by ID
- `complete id` - Mark task as complete by ID
- `incomplete id` - Mark task as incomplete by ID
- `help` - Show available commands
- `exit` or `quit` - Exit the application

## Example Usage

```
> add "Buy groceries" "Milk, bread, eggs"
Task added with ID: 1

> add "Finish report" "Complete the quarterly report"
Task added with ID: 2

> view
ID: 1 | Title: Buy groceries | Description: Milk, bread, eggs | Status: ✖ Incomplete
ID: 2 | Title: Finish report | Description: Complete the quarterly report | Status: ✖ Incomplete

> complete 1
Task 1 marked as complete

> view
ID: 1 | Title: Buy groceries | Description: Milk, bread, eggs | Status: ✔ Complete
ID: 2 | Title: Finish report | Description: Complete the quarterly report | Status: ✖ Incomplete

> exit
```

## Error Handling

- Invalid commands will show an error message
- Invalid task IDs will show "Task not found" message
- Missing required arguments will show usage instructions
- The application will not crash on invalid input

## Architecture

The application follows a clean architecture with separation of concerns:

- `src/`: Source code directory containing:
  - `main.py`: Entry point and CLI interface
  - `todo.py`: Core Todo class with in-memory storage
  - `task.py`: Task model/data structure
- `tests/`: Unit and integration tests
  - `unit/`: Unit tests for individual components
  - `integration/`: Integration tests for CLI functionality

## Testing

To run the tests from the project root:

```bash
pytest
```

Or run the standalone test script:

```bash
python -m src.test_app
```

The application includes comprehensive unit tests for the Task and Todo classes, as well as integration tests for the CLI functionality.