#!/usr/bin/env python3
"""
Todo Console Application - Main Entry Point

This is the main entry point for the console application that allows users to
view their todo items with proper formatting and status indicators.
"""

import sys
from todo_app import TodoApp


def display_menu():
    """Display the main menu options."""
    print("\nTodo Console Application")
    print("=" * 25)
    print("1. View all todos")
    print("2. Add a new todo")
    print("3. Update an existing todo")
    print("4. Delete a todo")
    print("5. Mark todo as complete")
    print("6. Mark todo as incomplete")
    print("7. Toggle todo status")
    print("8. Exit")
    print()


def get_user_input(prompt: str) -> str:
    """Get input from user with a prompt."""
    return input(prompt).strip()


def run_menu_system():
    """Run the menu-driven system."""
    app = TodoApp()

    while True:
        display_menu()
        choice = get_user_input("Choose an option (1-8): ")

        if choice == "1":
            # View all todos
            app.run()
        elif choice == "2":
            # Add a new todo
            title = get_user_input("Enter title: ")
            if not title:
                print("Title is required!")
                continue
            description = get_user_input("Enter description (optional): ")
            try:
                app.add_todo(title, description)
                print(f"Successfully added todo: '{title}'")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            # Update an existing todo
            if not app.get_all_todos():
                print("No todos available to update.")
                continue
            app.display_todos()
            todo_id = get_user_input("Enter the ID of the todo to update: ")
            title = get_user_input("Enter new title (or press Enter to keep current): ")
            description = get_user_input("Enter new description (or press Enter to keep current): ")

            # Only update fields that were provided
            update_title = title if title else None
            update_description = description if description else None

            try:
                success = app.update_todo(todo_id, update_title, update_description)
                if success:
                    print("Todo updated successfully!")
                else:
                    print("Todo not found!")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            # Delete a todo
            if not app.get_all_todos():
                print("No todos available to delete.")
                continue
            app.display_todos()
            todo_id = get_user_input("Enter the ID of the todo to delete: ")
            success = app.delete_todo(todo_id)
            if success:
                print("Todo deleted successfully!")
            else:
                print("Todo not found!")
        elif choice == "5":
            # Mark todo as complete
            if not app.get_all_todos():
                print("No todos available.")
                continue
            app.display_todos()
            todo_id = get_user_input("Enter the ID of the todo to mark complete: ")
            success = app.mark_complete(todo_id)
            if success:
                print("Todo marked as complete!")
            else:
                print("Todo not found!")
        elif choice == "6":
            # Mark todo as incomplete
            if not app.get_all_todos():
                print("No todos available.")
                continue
            app.display_todos()
            todo_id = get_user_input("Enter the ID of the todo to mark incomplete: ")
            success = app.mark_incomplete(todo_id)
            if success:
                print("Todo marked as incomplete!")
            else:
                print("Todo not found!")
        elif choice == "7":
            # Toggle todo status
            if not app.get_all_todos():
                print("No todos available.")
                continue
            app.display_todos()
            todo_id = get_user_input("Enter the ID of the todo to toggle: ")
            success = app.toggle_status(todo_id)
            if success:
                print("Todo status toggled!")
            else:
                print("Todo not found!")
        elif choice == "8":
            # Exit
            print("Thank you for using the Todo Console Application!")
            break
        else:
            print("Invalid option! Please choose a number between 1-8.")

        # Pause before showing menu again
        input("\nPress Enter to continue...")


def main():
    """Main function to run the todo application."""
    # If command line arguments are provided, run in CLI mode (for backward compatibility)
    if len(sys.argv) > 1:
        print("Running in CLI mode. For menu interface, run without arguments.")
        # For now, just run the menu system regardless of arguments
        # This can be modified later to handle CLI arguments
    else:
        # Run the menu-driven system
        run_menu_system()


if __name__ == "__main__":
    main()