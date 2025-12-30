# Todo Console Application

A simple Python console application for managing and viewing todo items with full CRUD operations.

## Features

- Add new todos with title and optional description
- View all todos with ID, title, description, and status
- Update existing todos by ID
- Delete todos by ID
- Clear status indicators ([X] Completed / [ ] Pending)
- Tabular display format for easy reading
- In-memory storage (no persistent storage)
- Command-line interface for all operations

## Requirements

- Python 3.13+

## Setup

1. Clone the repository
2. Navigate to the project directory
3. Run the application with: `python src/main.py`

## Usage

The application supports the following commands:

- `add <title> [description]` - Add a new todo
- `update <id> <title> [description]` - Update an existing todo
- `delete <id>` - Delete a todo by ID
- `view` - View all todos
- `help` - Show help information

## Example Usage

```
# Add a new todo
python src/main.py add "Buy groceries" "Milk, bread, eggs"

# View all todos
python src/main.py view

# Update a todo (use the ID from the view command)
python src/main.py update <id> "Updated title" "Updated description"

# Delete a todo (use the ID from the view command)
python src/main.py delete <id>
```

## Example Output

```
Todo Console Application
=========================
ID                                   | Title      | Description           | Status
--------------------------------------------------------------------------------
123e4567-e89b-12d3-a456-426614174000 | Buy groceries | Milk, bread, eggs    | [ ] Pending
123e4567-e89b-12d3-a456-426614174001 | Finish report | Complete the quarterly report | [X] Completed
```