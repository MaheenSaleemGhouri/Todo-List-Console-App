# Data Model: Todo Completion Status Management

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
- **title**: Required, non-empty string (no whitespace-only strings)
- **description**: Optional, can be empty string
- **completed**: Boolean value, defaults to False
- **id**: Unique, auto-generated UUID string

### State Transitions
- **Mark Complete**: Todo status changes from incomplete (False) to complete (True)
- **Mark Incomplete**: Todo status changes from complete (True) to incomplete (False)
- **Toggle Status**: Todo status flips from current state to opposite state
- **Add**: New todo is created with default completed=False status
- **Update**: Title and description can be modified, completion status can be changed

### Operations
- **Mark Complete**: Set completion status to True for existing todo by ID
- **Mark Incomplete**: Set completion status to False for existing todo by ID
- **Toggle Status**: Flip completion status from current to opposite state for existing todo by ID
- **Add**: Create new todo with required title and optional description
- **Update**: Modify existing todo by ID with new title and/or description
- **Delete**: Remove existing todo by ID