# Data Model: Todo Application

## Todo Entity

**Name**: Todo
**Description**: Represents a task with unique ID, title, description, and completion status.

### Fields
- **id** (string): Unique identifier for the todo item, generated using UUID
- **title** (string): Brief description of the task
- **description** (string): Detailed information about the task
- **completed** (boolean): Indicates whether the task has been completed (true) or is pending (false)

### Relationships
- None (standalone entity)

### Validation Rules
- **title**: Required, non-empty string
- **description**: Optional, can be empty string
- **completed**: Boolean value, defaults to False
- **id**: Unique, auto-generated UUID string

### State Transitions
- Not applicable for viewing functionality (completion status is read-only for this feature)