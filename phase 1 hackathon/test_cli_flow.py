#!/usr/bin/env python3
"""
Test script to verify the CLI functionality works as expected
"""
from src.todo_app import TodoApp
from src.cli_handler import CLIHandler

def test_cli_flow():
    """Test the complete CLI flow"""
    print("Testing CLI flow...")

    # Create a todo app instance
    app = TodoApp()
    cli = CLIHandler(app)

    print("\n1. Testing add command:")
    cli.handle_add(["Test Todo", "This is a test description"])

    print("\n2. Testing view command:")
    cli.handle_view()

    print("\n3. Testing update command:")
    if app.todos:
        todo_id = app.todos[0].id
        cli.handle_update([todo_id, "Updated Todo", "This is an updated description"])

        print("\n4. View after update:")
        cli.handle_view()

        print("\n5. Testing delete command:")
        cli.handle_delete([todo_id])

        print("\n6. View after delete:")
        cli.handle_view()

if __name__ == "__main__":
    test_cli_flow()