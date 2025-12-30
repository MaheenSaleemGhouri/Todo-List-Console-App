---
description: "Task list for todo CRUD operations"
---

# Tasks: Todo CRUD Operations

**Input**: Design documents from `/specs/002-todo-crud/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Extend existing project structure with CLI handler module in src/cli_handler.py
- [X] T002 Update main.py to integrate CLI handler functionality
- [X] T003 [P] Create tests/unit directory for CRUD operation tests

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Enhance TodoApp class in src/todo_app.py with add_todo method
- [X] T005 Enhance TodoApp class in src/todo_app.py with update_todo method
- [X] T006 Enhance TodoApp class in src/todo_app.py with delete_todo method
- [X] T007 Implement ID validation logic in src/todo_app.py
- [X] T008 Implement title validation logic in src/todo_app.py
- [X] T009 Create CLI command handler in src/cli_handler.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Todo (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todos with a title and optional description

**Independent Test**: The system allows users to add a new todo with a title and optional description, which then appears in the todo list with a unique ID and pending status.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T010 [P] [US1] Unit test for adding todo with title and description in tests/unit/test_todo_app.py
- [X] T011 [P] [US1] Unit test for adding todo with title only (no description) in tests/unit/test_todo_app.py
- [X] T012 [P] [US1] Unit test for validation of empty title during add in tests/unit/test_todo_app.py

### Implementation for User Story 1

- [X] T013 [P] [US1] Implement add todo validation in src/todo_app.py
- [X] T014 [US1] Add CLI command for adding todos in src/cli_handler.py
- [X] T015 [US1] Implement success message for add operation in src/todo_app.py
- [X] T016 [US1] Implement error handling for empty title in src/todo_app.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Update Existing Todo (Priority: P2)

**Goal**: Allow users to update existing todos by ID with new title and/or description

**Independent Test**: The system allows users to update a todo's title and description by providing the todo ID, with proper validation and error handling for invalid IDs.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T017 [P] [US2] Unit test for updating todo title in tests/unit/test_todo_app.py
- [X] T018 [P] [US2] Unit test for updating todo description in tests/unit/test_todo_app.py
- [X] T019 [P] [US2] Unit test for validation of invalid ID during update in tests/unit/test_todo_app.py
- [X] T020 [P] [US2] Unit test for validation of empty title during update in tests/unit/test_todo_app.py

### Implementation for User Story 2

- [X] T021 [P] [US2] Implement update todo validation in src/todo_app.py
- [X] T022 [US2] Add CLI command for updating todos in src/cli_handler.py
- [X] T023 [US2] Implement ID validation for update operation in src/todo_app.py
- [X] T024 [US2] Implement success message for update operation in src/todo_app.py
- [X] T025 [US2] Implement error handling for invalid ID during update in src/todo_app.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Delete Todo by ID (Priority: P3)

**Goal**: Allow users to delete todos by providing the todo ID

**Independent Test**: The system allows users to delete a todo by providing the todo ID, with proper validation and error handling for invalid IDs.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T026 [P] [US3] Unit test for deleting existing todo in tests/unit/test_todo_app.py
- [X] T027 [P] [US3] Unit test for validation of invalid ID during delete in tests/unit/test_todo_app.py

### Implementation for User Story 3

- [X] T028 [P] [US3] Implement delete todo validation in src/todo_app.py
- [X] T029 [US3] Add CLI command for deleting todos in src/cli_handler.py
- [X] T030 [US3] Implement ID validation for delete operation in src/todo_app.py
- [X] T031 [US3] Implement success message for delete operation in src/todo_app.py
- [X] T032 [US3] Implement error handling for invalid ID during delete in src/todo_app.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T033 [P] Documentation updates in README.md
- [X] T034 Code cleanup and refactoring in src/todo_app.py and src/cli_handler.py
- [X] T035 Error message consistency across all operations in src/todo_app.py
- [X] T036 [P] Additional unit tests in tests/unit/test_todo_app.py
- [X] T037 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for adding todo with title and description in tests/unit/test_todo_app.py"
Task: "Unit test for adding todo with title only (no description) in tests/unit/test_todo_app.py"
Task: "Unit test for validation of empty title during add in tests/unit/test_todo_app.py"

# Launch implementation tasks where possible:
Task: "Implement add todo validation in src/todo_app.py"
Task: "Add CLI command for adding todos in src/cli_handler.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence