#!/usr/bin/env python3
"""
Todo Console Application - Core Logic

This module contains the core functionality for the todo application,
including the Todo class definition and in-memory storage mechanism.
"""

import uuid
from typing import List, Optional


class Todo:
    """
    Represents a todo item with unique ID, title, description, and completion status.

    Attributes:
        id (str): Unique identifier for the todo item, generated using UUID
        title (str): Brief description of the task
        description (str): Detailed information about the task
        completed (bool): Indicates whether the task has been completed (true) or is pending (false)
    """

    def __init__(self, title: str, description: str = "", completed: bool = False):
        """
        Initialize a new Todo instance.

        Args:
            title (str): Brief description of the task (required, non-empty string)
            description (str): Detailed information about the task (optional, can be empty string)
            completed (bool): Completion status, defaults to False
        """
        if not title or not title.strip():
            raise ValueError("Title is required and cannot be empty or whitespace only")

        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        """Return a string representation of the todo item."""
        status = "Completed" if self.completed else "Pending"
        return f"[{self.id}] {self.title} - {self.description} ({status})"

    def __repr__(self):
        """Return a detailed string representation of the todo item."""
        return f"Todo(id='{self.id}', title='{self.title}', description='{self.description}', completed={self.completed})"


class TodoApp:
    """
    Todo application class that manages todos in memory and provides viewing functionality.
    """

    def __init__(self):
        """Initialize the todo application with an empty list of todos."""
        self.todos: List[Todo] = []

    def add_todo(self, title: str, description: str = "", completed: bool = False) -> Todo:
        """
        Add a new todo to the application.

        Args:
            title (str): Title of the todo
            description (str): Description of the todo (optional)
            completed (bool): Completion status of the todo (optional, defaults to False)

        Returns:
            Todo: The newly created todo object
        """
        if not title or not title.strip():
            raise ValueError("Title is required and cannot be empty or whitespace only")

        todo = Todo(title, description, completed)
        self.todos.append(todo)
        return todo

    def update_todo(self, todo_id: str, title: str = None, description: str = None) -> bool:
        """
        Update an existing todo by ID.

        Args:
            todo_id (str): ID of the todo to update
            title (str, optional): New title for the todo
            description (str, optional): New description for the todo

        Returns:
            bool: True if the todo was updated, False if not found
        """
        # Find the todo with the given ID
        for todo in self.todos:
            if todo.id == todo_id:
                # Validate title if provided
                if title is not None:
                    if not title or not title.strip():
                        raise ValueError("Title cannot be empty or whitespace only")
                    todo.title = title

                # Update description if provided
                if description is not None:
                    todo.description = description

                return True

        # Todo not found
        return False

    def delete_todo(self, todo_id: str) -> bool:
        """
        Delete a todo by ID.

        Args:
            todo_id (str): ID of the todo to delete

        Returns:
            bool: True if the todo was deleted, False if not found
        """
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[i]
                return True

        # Todo not found
        return False

    def mark_complete(self, todo_id: str) -> bool:
        """
        Mark a todo as complete by ID.

        Args:
            todo_id (str): ID of the todo to mark as complete

        Returns:
            bool: True if the todo was marked complete, False if not found
        """
        todo = self.find_todo_by_id(todo_id)
        if todo:
            todo.completed = True
            return True
        return False

    def mark_incomplete(self, todo_id: str) -> bool:
        """
        Mark a todo as incomplete by ID.

        Args:
            todo_id (str): ID of the todo to mark as incomplete

        Returns:
            bool: True if the todo was marked incomplete, False if not found
        """
        todo = self.find_todo_by_id(todo_id)
        if todo:
            todo.completed = False
            return True
        return False

    def toggle_status(self, todo_id: str) -> bool:
        """
        Toggle the completion status of a todo by ID.

        Args:
            todo_id (str): ID of the todo to toggle

        Returns:
            bool: True if the todo status was toggled, False if not found
        """
        todo = self.find_todo_by_id(todo_id)
        if todo:
            todo.completed = not todo.completed
            return True
        return False

    def find_todo_by_id(self, todo_id: str) -> Optional[Todo]:
        """
        Find a todo by its ID.

        Args:
            todo_id (str): ID of the todo to find

        Returns:
            Todo or None: The found todo or None if not found
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos in the application.

        Returns:
            List[Todo]: List of all todo objects
        """
        return self.todos

    def display_todos(self):
        """Display all todos in a formatted table."""
        if not self.todos:
            self.display_no_todos_message()
            return

        # Calculate column widths
        id_width = max(5, len("ID"))
        title_width = max(10, len("Title"))
        desc_width = max(15, len("Description"))
        status_width = max(12, len("Status"))  # Increased for better status display

        for todo in self.todos:
            id_width = max(id_width, len(todo.id))
            title_width = max(title_width, len(todo.title))
            desc_width = max(desc_width, len(todo.description or ""))

        # Create header
        header = f"{'ID':<{id_width}} | {'Title':<{title_width}} | {'Description':<{desc_width}} | {'Status':<{status_width}}"
        separator = "-" * len(header)

        print(header)
        print(separator)

        # Print each todo with enhanced formatting
        for todo in self.todos:
            status = "[X] Completed" if todo.completed else "[ ] Pending"
            print(f"{todo.id:<{id_width}} | {todo.title:<{title_width}} | {todo.description:<{desc_width}} | {status:<{status_width}}")

    def validate_todo_display(self) -> bool:
        """Validate that all todos display with required information."""
        # This is a basic validation that all todos have the required fields
        for todo in self.todos:
            if not hasattr(todo, 'id') or not hasattr(todo, 'title') or not hasattr(todo, 'description') or not hasattr(todo, 'completed'):
                return False
            if not todo.title:  # Title is required
                return False
        return True

    def display_no_todos_message(self):
        """Display a message when no todos are available."""
        print("No todos available.")

    def run(self):
        """
        Run the todo application - for now, just display the todos.
        This method would normally handle user input and commands.
        """
        print("Todo Console Application")
        print("=" * 25)
        self.display_todos()


# Example usage for testing
if __name__ == "__main__":
    # Create a sample application with some todos
    app = TodoApp()
    app.add_todo("Buy groceries", "Milk, bread, eggs")
    app.add_todo("Finish report", "Complete the quarterly report", completed=True)
    app.run()