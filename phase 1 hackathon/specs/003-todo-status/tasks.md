---
description: "Task list for todo completion status management"
---

# Tasks: Todo Completion Status Management

**Input**: Design documents from `/specs/003-todo-status/`
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

- [X] T001 Extend todo_app.py with mark_complete method in src/todo_app.py
- [X] T002 Extend todo_app.py with mark_incomplete method in src/todo_app.py
- [X] T003 [P] Extend todo_app.py with toggle_status method in src/todo_app.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Enhance TodoApp class in src/todo_app.py with status management methods
- [X] T005 Create menu display functionality in src/main.py
- [X] T006 Implement menu navigation logic in src/main.py
- [X] T007 Add status display indicators in src/todo_app.py
- [X] T008 Implement edge case handling in src/todo_app.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Mark Todo Complete/Incomplete (Priority: P1) 🎯 MVP

**Goal**: Enable users to mark todos as complete or incomplete by ID with proper validation

**Independent Test**: The system allows users to mark a todo as complete or incomplete by providing its ID, with proper validation and clear status indicators in the display.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T009 [P] [US1] Unit test for marking todo as complete in tests/unit/test_todo_app.py
- [X] T010 [P] [US1] Unit test for marking todo as incomplete in tests/unit/test_todo_app.py
- [X] T011 [P] [US1] Unit test for validation of invalid ID during status change in tests/unit/test_todo_app.py

### Implementation for User Story 1

- [X] T012 [P] [US1] Implement mark complete validation in src/todo_app.py
- [X] T013 [US1] Add menu option for marking complete in src/main.py
- [X] T014 [US1] Implement success message for mark complete operation in src/main.py
- [X] T015 [US1] Implement error handling for invalid ID during mark complete in src/todo_app.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Toggle Completion Status (Priority: P2)

**Goal**: Allow users to toggle the completion status of a todo by ID

**Independent Test**: The system allows users to toggle a todo's completion status by providing its ID, changing from complete to incomplete or vice versa.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T016 [P] [US2] Unit test for toggling complete todo to incomplete in tests/unit/test_todo_app.py
- [X] T017 [P] [US2] Unit test for toggling incomplete todo to complete in tests/unit/test_todo_app.py

### Implementation for User Story 2

- [X] T018 [P] [US2] Implement toggle status logic in src/todo_app.py
- [X] T019 [US2] Add menu option for toggling status in src/main.py
- [X] T020 [US2] Implement success message for toggle operation in src/main.py
- [X] T021 [US2] Implement error handling for invalid ID during toggle in src/todo_app.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Improved Console Menu System (Priority: P3)

**Goal**: Provide a simple console menu system that provides clear navigation options

**Independent Test**: The system presents a menu with clear options for viewing, adding, updating, deleting, marking complete/incomplete, and exiting the application.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T022 [P] [US3] Unit test for main menu display in tests/unit/test_todo_app.py
- [X] T023 [P] [US3] Unit test for menu option selection in tests/unit/test_todo_app.py

### Implementation for User Story 3

- [X] T024 [P] [US3] Implement main menu display in src/main.py
- [X] T025 [US3] Add all menu options with proper numbering in src/main.py
- [X] T026 [US3] Implement menu navigation flow in src/main.py
- [X] T027 [US3] Add input validation for menu selections in src/main.py
- [X] T028 [US3] Implement return to main menu functionality in src/main.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T029 [P] Documentation updates in README.md
- [X] T030 Code cleanup and refactoring in src/main.py and src/todo_app.py
- [X] T031 Error message consistency across all operations in src/main.py
- [X] T032 [P] Additional unit tests in tests/unit/test_todo_app.py
- [X] T033 Run quickstart.md validation

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
Task: "Unit test for marking todo as complete in tests/unit/test_todo_app.py"
Task: "Unit test for marking todo as incomplete in tests/unit/test_todo_app.py"
Task: "Unit test for validation of invalid ID during status change in tests/unit/test_todo_app.py"

# Launch implementation tasks where possible:
Task: "Implement mark complete validation in src/todo_app.py"
Task: "Add menu option for marking complete in src/main.py"
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