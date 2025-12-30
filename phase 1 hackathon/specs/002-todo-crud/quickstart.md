# Quickstart: Todo CRUD Operations

## Setup

1. Ensure Python 3.13+ is installed on your system
2. Navigate to the project directory
3. Run the application using: `python src/main.py`

## Usage

The application now supports CRUD operations:

- **Add a new todo**: Use the add command with a required title and optional description
- **Update an existing todo**: Use the update command with the todo ID and new title/description
- **Delete a todo**: Use the delete command with the todo ID
- **View all todos**: Use the existing view command

## Example Commands

```
# Add a new todo
python src/main.py add --title "New task" --description "Task details"

# Update an existing todo
python src/main.py update --id "todo-uuid" --title "Updated title" --description "Updated description"

# Delete a todo
python src/main.py delete --id "todo-uuid"

# View all todos
python src/main.py view
```

## Error Handling

The application provides clear error messages for:
- Invalid or non-existent IDs during update/delete operations
- Empty titles during add/update operations
- Invalid command formats

## Requirements

- Python 3.13+
- No additional dependencies required
- Console/terminal access