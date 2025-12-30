#!/usr/bin/env python3
"""
CLI Handler for Todo Application

This module handles command-line interface operations for the todo application,
processing user input and routing to appropriate functionality.
"""


class CLIHandler:
    """
    Handles command-line interface operations for the todo application.
    """

    def __init__(self, todo_app):
        """
        Initialize the CLI handler with a todo application instance.

        Args:
            todo_app: An instance of TodoApp to perform operations on
        """
        self.todo_app = todo_app

    def parse_command(self, args):
        """
        Parse command-line arguments and execute the appropriate operation.

        Args:
            args: Command-line arguments list (excluding script name)

        Returns:
            bool: True if command was executed successfully, False otherwise
        """
        if not args:
            self.show_help()
            return False

        command = args[0].lower()

        if command == "add":
            return self.handle_add(args[1:])
        elif command == "update":
            return self.handle_update(args[1:])
        elif command == "delete":
            return self.handle_delete(args[1:])
        elif command == "view":
            return self.handle_view()
        elif command == "help":
            self.show_help()
            return True
        else:
            print(f"Unknown command: {command}")
            self.show_help()
            return False

    def handle_add(self, args):
        """
        Handle the add command to create a new todo.

        Args:
            args: Arguments for the add command (title and optional description)

        Returns:
            bool: True if command was executed successfully, False otherwise
        """
        if len(args) < 1:
            print("Error: Add command requires at least a title")
            print("Usage: add <title> [description]")
            return False

        title = args[0]
        description = " ".join(args[1:]) if len(args) > 1 else ""

        try:
            todo = self.todo_app.add_todo(title, description)
            print(f"Successfully added todo: '{todo.title}' with ID: {todo.id}")
            return True
        except ValueError as e:
            print(f"Error adding todo: {e}")
            return False

    def handle_update(self, args):
        """
        Handle the update command to modify an existing todo.

        Args:
            args: Arguments for the update command (id, title, and optional description)

        Returns:
            bool: True if command was executed successfully, False otherwise
        """
        if len(args) < 2:
            print("Error: Update command requires an ID and at least a title or description")
            print("Usage: update <id> <title> [description]")
            return False

        todo_id = args[0]
        title = args[1]
        description = " ".join(args[2:]) if len(args) > 2 else ""

        try:
            success = self.todo_app.update_todo(todo_id, title, description)
            if success:
                print(f"Successfully updated todo with ID: {todo_id}")
            else:
                print(f"Error: Todo with ID {todo_id} not found")
            return success
        except ValueError as e:
            print(f"Error updating todo: {e}")
            return False

    def handle_delete(self, args):
        """
        Handle the delete command to remove a todo.

        Args:
            args: Arguments for the delete command (id)

        Returns:
            bool: True if command was executed successfully, False otherwise
        """
        if len(args) < 1:
            print("Error: Delete command requires an ID")
            print("Usage: delete <id>")
            return False

        todo_id = args[0]

        try:
            success = self.todo_app.delete_todo(todo_id)
            if success:
                print(f"Successfully deleted todo with ID: {todo_id}")
            else:
                print(f"Error: Todo with ID {todo_id} not found")
            return success
        except Exception as e:
            print(f"Error deleting todo: {e}")
            return False

    def handle_view(self):
        """
        Handle the view command to display all todos.

        Returns:
            bool: True if command was executed successfully, False otherwise
        """
        self.todo_app.display_todos()
        return True

    def show_help(self):
        """
        Display help information for available commands.
        """
        print("Todo Application Commands:")
        print("  add <title> [description]    - Add a new todo")
        print("  update <id> <title> [description] - Update an existing todo")
        print("  delete <id>                  - Delete a todo by ID")
        print("  view                         - View all todos")
        print("  help                         - Show this help message")