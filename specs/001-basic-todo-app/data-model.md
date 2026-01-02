# Data Model: Basic Todo Console Application

## Task Entity

### Attributes
- **id** (int): Auto-generated unique identifier
  - Type: Integer
  - Constraints: Positive integer, unique within session
  - Generated: Auto-incrementing starting from 1
- **title** (str): Required title of the task
  - Type: String
  - Constraints: Required, non-empty
  - Validation: Must not be empty or whitespace-only
- **description** (str): Optional description of the task
  - Type: String
  - Constraints: Optional, can be empty
  - Default: Empty string if not provided
- **is_completed** (bool): Status indicating if the task is complete
  - Type: Boolean
  - Constraints: True/False value
  - Default: False (incomplete) for new tasks

### State Transitions
- New Task: `is_completed = False` (default)
- Complete Task: `is_completed = True` (when marked complete)
- Incomplete Task: `is_completed = False` (when marked incomplete)

### Validation Rules
- Title must be provided and not empty
- ID must be unique within the current session
- ID must be a positive integer
- Task must exist before update/delete operations

### Relationships
- No relationships with other entities (standalone entity)