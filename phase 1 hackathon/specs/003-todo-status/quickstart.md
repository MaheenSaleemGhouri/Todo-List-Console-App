# Quickstart: Todo Completion Status Management

## Setup

1. Ensure Python 3.13+ is installed on your system
2. Navigate to the project directory
3. Run the application using: `python src/main.py`

## Usage

The application now features a menu-driven interface for all operations:

- **Main Menu**: Select options 1-8 to perform different operations
- **View Todos**: Option 1 - Displays all todos with clear status indicators
- **Add Todo**: Option 2 - Create new todos with title and optional description
- **Update Todo**: Option 3 - Modify existing todos by ID
- **Delete Todo**: Option 4 - Remove todos by ID
- **Mark Complete**: Option 5 - Mark a todo as complete by ID
- **Mark Incomplete**: Option 6 - Mark a todo as incomplete by ID
- **Toggle Status**: Option 7 - Flip the completion status of a todo by ID
- **Exit**: Option 8 - Close the application

## Example Flow

```
Todo Console Application
========================
1. View all todos
2. Add a new todo
3. Update an existing todo
4. Delete a todo
5. Mark todo as complete
6. Mark todo as incomplete
7. Toggle todo status
8. Exit
Choose an option: 1

ID                                   | Title      | Description           | Status
--------------------------------------------------------------------------------
123e4567-e89b-12d3-a456-426614174000 | Buy groceries | Milk, bread, eggs    | [ ] Pending
123e4567-e89b-12d3-a456-426614174001 | Finish report | Complete the quarterly report | [X] Completed
```

## Edge Case Handling

The application handles these edge cases:
- No todos available in the system
- Invalid todo IDs during status operations
- Invalid menu selections
- Empty input validation

## Requirements

- Python 3.13+
- No additional dependencies required
- Console/terminal access