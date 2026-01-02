# CLI Interface Contract: Basic Todo Console Application

## Overview
This document describes the command-line interface contract for the Basic Todo Console Application. The application provides a text-based interface for managing tasks.

## Command Structure
The application accepts commands in the format:
```
command [arguments]
```

## Commands

### Add Task
- **Command**: `add`
- **Arguments**: 
  - `title` (required): The title of the task (string)
  - `description` (optional): The description of the task (string)
- **Response**: Success message with assigned task ID
- **Error Cases**: 
  - Missing title: Error message prompting for title
  - Invalid input: Error message with usage instructions

### View Tasks
- **Command**: `view`
- **Arguments**: None
- **Response**: List of all tasks with ID, title, description, and completion status
- **Error Cases**: None

### Update Task
- **Command**: `update`
- **Arguments**:
  - `id` (required): The ID of the task to update (integer)
  - `new_title` (optional): The new title for the task (string)
  - `new_description` (optional): The new description for the task (string)
- **Response**: Success message confirming update
- **Error Cases**:
  - Invalid ID: Error message "Task not found"
  - Missing ID: Error message with usage instructions

### Delete Task
- **Command**: `delete`
- **Arguments**:
  - `id` (required): The ID of the task to delete (integer)
- **Response**: Success message confirming deletion
- **Error Cases**:
  - Invalid ID: Error message "Task not found"
  - Missing ID: Error message with usage instructions

### Mark Complete
- **Command**: `complete`
- **Arguments**:
  - `id` (required): The ID of the task to mark complete (integer)
- **Response**: Success message confirming status change
- **Error Cases**:
  - Invalid ID: Error message "Task not found"
  - Missing ID: Error message with usage instructions

### Mark Incomplete
- **Command**: `incomplete`
- **Arguments**:
  - `id` (required): The ID of the task to mark incomplete (integer)
- **Response**: Success message confirming status change
- **Error Cases**:
  - Invalid ID: Error message "Task not found"
  - Missing ID: Error message with usage instructions

### Help
- **Command**: `help`
- **Arguments**: None
- **Response**: List of available commands with usage instructions
- **Error Cases**: None

### Exit
- **Command**: `exit` or `quit`
- **Arguments**: None
- **Response**: Application terminates gracefully
- **Error Cases**: None

## Error Response Format
All error responses follow the format:
```
Error: [descriptive error message]
Usage: [command usage instructions]
```

## Success Response Format
All success responses follow the format:
```
[descriptive success message]
```

## Validation Rules
- Task titles must not be empty
- Task IDs must be positive integers
- Only existing tasks can be updated, deleted, or have their status changed