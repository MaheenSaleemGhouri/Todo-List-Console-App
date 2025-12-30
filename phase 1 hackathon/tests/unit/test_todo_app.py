"""
Unit tests for the Todo application status management functionality.

These tests verify the functionality of the Todo and TodoApp classes,
including the new status management operations (mark complete, mark incomplete, toggle).
"""
import sys
import os
# Add the src directory to the path so we can import todo_app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from todo_app import Todo, TodoApp


def test_todo_creation():
    """Test creating a new Todo item."""
    todo = Todo("Test title", "Test description")

    assert todo.title == "Test title"
    assert todo.description == "Test description"
    assert todo.completed == False
    assert todo.id is not None
    assert len(todo.id) > 0  # UUID should have a value


def test_todo_creation_with_completion_status():
    """Test creating a Todo item with completed status."""
    todo = Todo("Test title", "Test description", completed=True)

    assert todo.title == "Test title"
    assert todo.description == "Test description"
    assert todo.completed == True
    assert todo.id is not None


def test_todo_creation_without_description():
    """Test creating a Todo item without description."""
    todo = Todo("Test title")

    assert todo.title == "Test title"
    assert todo.description == ""
    assert todo.completed == False


def test_todo_creation_fails_without_title():
    """Test that creating a Todo item without title raises ValueError."""
    try:
        Todo("")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected


def test_todo_app_initialization():
    """Test initializing a TodoApp."""
    app = TodoApp()

    assert app.todos == []


def test_add_todo():
    """Test adding a todo to the application."""
    app = TodoApp()
    todo = app.add_todo("Test title", "Test description")

    assert len(app.todos) == 1
    assert app.todos[0] == todo
    assert todo.title == "Test title"
    assert todo.description == "Test description"


def test_add_todo_with_completion():
    """Test adding a todo with completion status."""
    app = TodoApp()
    todo = app.add_todo("Test title", "Test description", completed=True)

    assert len(app.todos) == 1
    assert app.todos[0] == todo
    assert todo.title == "Test title"
    assert todo.description == "Test description"
    assert todo.completed == True


def test_add_todo_validation():
    """Test validation of empty title during add."""
    app = TodoApp()

    try:
        app.add_todo("")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected

    try:
        app.add_todo("   ")  # Whitespace only
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected


def test_update_todo():
    """Test updating a todo's title and description."""
    app = TodoApp()
    original_todo = app.add_todo("Original title", "Original description")

    # Update both title and description
    success = app.update_todo(original_todo.id, "Updated title", "Updated description")

    assert success == True
    assert len(app.todos) == 1
    assert app.todos[0].title == "Updated title"
    assert app.todos[0].description == "Updated description"


def test_update_todo_title_only():
    """Test updating only the title of a todo."""
    app = TodoApp()
    original_todo = app.add_todo("Original title", "Original description")

    # Update only title
    success = app.update_todo(original_todo.id, "Updated title")

    assert success == True
    assert app.todos[0].title == "Updated title"
    assert app.todos[0].description == "Original description"  # Should remain unchanged


def test_update_todo_description_only():
    """Test updating only the description of a todo."""
    app = TodoApp()
    original_todo = app.add_todo("Original title", "Original description")

    # Update only description
    success = app.update_todo(original_todo.id, description="Updated description")

    assert success == True
    assert app.todos[0].title == "Original title"  # Should remain unchanged
    assert app.todos[0].description == "Updated description"


def test_update_todo_invalid_id():
    """Test updating a todo with invalid ID."""
    app = TodoApp()
    app.add_todo("Original title", "Original description")

    success = app.update_todo("invalid-id", "Updated title", "Updated description")

    assert success == False
    assert len(app.todos) == 1  # No change to todo list
    assert app.todos[0].title == "Original title"
    assert app.todos[0].description == "Original description"


def test_update_todo_empty_title():
    """Test validation of empty title during update."""
    app = TodoApp()
    original_todo = app.add_todo("Original title", "Original description")

    try:
        app.update_todo(original_todo.id, "")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected

    try:
        app.update_todo(original_todo.id, "   ")  # Whitespace only
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected

    # Original todo should remain unchanged
    assert app.todos[0].title == "Original title"


def test_delete_todo():
    """Test deleting a todo by ID."""
    app = TodoApp()
    todo1 = app.add_todo("Title 1", "Description 1")
    todo2 = app.add_todo("Title 2", "Description 2")
    todo3 = app.add_todo("Title 3", "Description 3")

    assert len(app.todos) == 3

    # Delete the second todo
    success = app.delete_todo(todo2.id)

    assert success == True
    assert len(app.todos) == 2
    assert todo1 in app.todos
    assert todo3 in app.todos
    assert todo2 not in app.todos


def test_delete_todo_invalid_id():
    """Test deleting a todo with invalid ID."""
    app = TodoApp()
    todo = app.add_todo("Title", "Description")

    assert len(app.todos) == 1

    success = app.delete_todo("invalid-id")

    assert success == False
    assert len(app.todos) == 1  # No change to todo list
    assert app.todos[0].title == "Title"


def test_get_all_todos():
    """Test getting all todos from the application."""
    app = TodoApp()
    todo1 = app.add_todo("Test title 1", "Test description 1")
    todo2 = app.add_todo("Test title 2", "Test description 2")

    todos = app.get_all_todos()

    assert len(todos) == 2
    assert todos[0] == todo1
    assert todos[1] == todo2


def test_find_todo_by_id():
    """Test finding a todo by its ID."""
    app = TodoApp()
    original_todo = app.add_todo("Test title", "Test description")

    found_todo = app.find_todo_by_id(original_todo.id)

    assert found_todo is not None
    assert found_todo.id == original_todo.id
    assert found_todo.title == original_todo.title
    assert found_todo.description == original_todo.description

    # Test with invalid ID
    not_found = app.find_todo_by_id("invalid-id")
    assert not_found is None


def test_validate_todo_display():
    """Test the validation function for todo display."""
    app = TodoApp()

    # Initially should return True when no todos exist
    assert app.validate_todo_display() == True

    # Add a valid todo
    app.add_todo("Test title", "Test description")
    assert app.validate_todo_display() == True

    # Add a todo with empty title should raise ValueError during creation
    try:
        app.add_todo("")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected


def test_mark_complete():
    """Test marking a todo as complete."""
    app = TodoApp()
    todo = app.add_todo("Test title", "Test description")

    # Verify initial state
    assert todo.completed == False

    # Mark as complete
    success = app.mark_complete(todo.id)

    assert success == True
    assert todo.completed == True


def test_mark_complete_invalid_id():
    """Test marking a todo as complete with invalid ID."""
    app = TodoApp()
    todo = app.add_todo("Test title", "Test description")

    # Verify initial state
    assert todo.completed == False

    # Try to mark with invalid ID
    success = app.mark_complete("invalid-id")

    assert success == False
    assert todo.completed == False  # Original todo should remain unchanged


def test_mark_incomplete():
    """Test marking a todo as incomplete."""
    app = TodoApp()
    todo = app.add_todo("Test title", "Test description", completed=True)

    # Verify initial state
    assert todo.completed == True

    # Mark as incomplete
    success = app.mark_incomplete(todo.id)

    assert success == True
    assert todo.completed == False


def test_mark_incomplete_invalid_id():
    """Test marking a todo as incomplete with invalid ID."""
    app = TodoApp()
    todo = app.add_todo("Test title", "Test description", completed=True)

    # Verify initial state
    assert todo.completed == True

    # Try to mark with invalid ID
    success = app.mark_incomplete("invalid-id")

    assert success == False
    assert todo.completed == True  # Original todo should remain unchanged


def test_toggle_status():
    """Test toggling a todo's completion status."""
    app = TodoApp()

    # Test toggling incomplete to complete
    todo1 = app.add_todo("Test title 1", "Test description 1")
    assert todo1.completed == False

    success1 = app.toggle_status(todo1.id)
    assert success1 == True
    assert todo1.completed == True

    # Test toggling complete to incomplete
    todo2 = app.add_todo("Test title 2", "Test description 2", completed=True)
    assert todo2.completed == True

    success2 = app.toggle_status(todo2.id)
    assert success2 == True
    assert todo2.completed == False


def test_toggle_status_invalid_id():
    """Test toggling a todo's status with invalid ID."""
    app = TodoApp()
    todo = app.add_todo("Test title", "Test description")

    # Verify initial state
    assert todo.completed == False

    # Try to toggle with invalid ID
    success = app.toggle_status("invalid-id")

    assert success == False
    assert todo.completed == False  # Original todo should remain unchanged


if __name__ == "__main__":
    # Run the tests
    test_todo_creation()
    test_todo_creation_with_completion_status()
    test_todo_creation_without_description()
    test_todo_creation_fails_without_title()
    test_todo_app_initialization()
    test_add_todo()
    test_add_todo_with_completion()
    test_add_todo_validation()
    test_update_todo()
    test_update_todo_title_only()
    test_update_todo_description_only()
    test_update_todo_invalid_id()
    test_update_todo_empty_title()
    test_delete_todo()
    test_delete_todo_invalid_id()
    test_get_all_todos()
    test_find_todo_by_id()
    test_validate_todo_display()
    test_mark_complete()
    test_mark_complete_invalid_id()
    test_mark_incomplete()
    test_mark_incomplete_invalid_id()
    test_toggle_status()
    test_toggle_status_invalid_id()

    print("All tests passed!")