"""
Task model representing a single todo item with the following attributes:
- id (int): Auto-generated unique identifier
- title (str): Required title of the task
- description (str): Optional description of the task
- is_completed (bool): Status indicating if the task is complete
"""

class Task:
    def __init__(self, task_id, title, description="", is_completed=False):
        """
        Initialize a new Task instance.
        
        Args:
            task_id (int): Unique identifier for the task
            title (str): Required title of the task
            description (str): Optional description of the task (default: "")
            is_completed (bool): Status indicating if the task is complete (default: False)
        
        Raises:
            ValueError: If title is empty or contains only whitespace
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")
        
        self.id = task_id
        self.title = title.strip()
        self.description = description.strip() if description else ""
        self.is_completed = is_completed
    
    def __str__(self):
        """String representation of the task."""
        status = "✔ Complete" if self.is_completed else "✖ Incomplete"
        return f"ID: {self.id} | Title: {self.title} | Description: {self.description} | Status: {status}"
    
    def __repr__(self):
        """Developer-friendly representation of the task."""
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', is_completed={self.is_completed})"
    
    def to_dict(self):
        """Convert task to dictionary representation."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'is_completed': self.is_completed
        }
    
    def mark_complete(self):
        """Mark the task as complete."""
        self.is_completed = True
    
    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.is_completed = False