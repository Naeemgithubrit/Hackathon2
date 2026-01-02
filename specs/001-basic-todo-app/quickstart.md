# Quickstart Guide: Basic Todo Console Application

## Prerequisites
- Python 3.13+ installed on your system
- Basic command line familiarity

## Setup
1. Clone or download the project files
2. Navigate to the project directory in your command line
3. No additional installation required - pure Python implementation

## Running the Application
```bash
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