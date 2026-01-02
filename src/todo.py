"""
Todo class with in-memory storage mechanism (Python list)
Implements the core functionality for managing tasks in memory only
"""

try:
    # Try relative import first (when run as module)
    from .task import Task
except ImportError:
    # Fall back to absolute import (when run directly)
    from task import Task


class Todo:
    def __init__(self):
        """
        Initialize a new Todo instance with in-memory storage.
        """
        self.tasks = []
        self.next_id = 1  # Auto-incrementing ID starting from 1
    
    def add_task(self, title, description=""):
        """
        Add a new task with required title and optional description.
        
        Args:
            title (str): Required title of the task
            description (str): Optional description of the task (default: "")
            
        Returns:
            Task: The newly created Task object
            
        Raises:
            ValueError: If title is empty or contains only whitespace
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")
        
        task = Task(self.next_id, title, description, is_completed=False)
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def get_all_tasks(self):
        """
        Retrieve all tasks from in-memory storage.
        
        Returns:
            list: List of all Task objects
        """
        return self.tasks.copy()  # Return a copy to prevent external modification
    
    def get_task_by_id(self, task_id):
        """
        Find a task by its ID.
        
        Args:
            task_id (int): The ID of the task to find
            
        Returns:
            Task: The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id, new_title=None, new_description=None):
        """
        Update an existing task's title and/or description by task ID.
        
        Args:
            task_id (int): The ID of the task to update
            new_title (str, optional): New title for the task
            new_description (str, optional): New description for the task
            
        Returns:
            bool: True if task was updated, False if task was not found
            
        Raises:
            ValueError: If new_title is provided but is empty or contains only whitespace
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        # Validate new title if provided
        if new_title is not None:
            if not new_title or not new_title.strip():
                raise ValueError("Task title cannot be empty or contain only whitespace")
            task.title = new_title.strip()
        
        # Update description if provided
        if new_description is not None:
            task.description = new_description.strip() if new_description else ""
        
        return True
    
    def delete_task(self, task_id):
        """
        Delete a task by its ID.
        
        Args:
            task_id (int): The ID of the task to delete
            
        Returns:
            bool: True if task was deleted, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        self.tasks.remove(task)
        return True
    
    def mark_complete(self, task_id):
        """
        Mark a task as complete by its ID.
        
        Args:
            task_id (int): The ID of the task to mark complete
            
        Returns:
            bool: True if task was marked complete, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        task.mark_complete()
        return True
    
    def mark_incomplete(self, task_id):
        """
        Mark a task as incomplete by its ID.
        
        Args:
            task_id (int): The ID of the task to mark incomplete
            
        Returns:
            bool: True if task was marked incomplete, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        task.mark_incomplete()
        return True