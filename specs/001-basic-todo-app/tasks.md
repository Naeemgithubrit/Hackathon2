---

description: "Task list template for feature implementation"
---

# Tasks: Basic Todo Console Application

**Input**: Design documents from `/specs/001-basic-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `main.py`, `todo.py`, `task.py` at repository root
- **Tests**: `tests/unit/`, `tests/integration/` at repository root
- Paths shown below follow the plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan (main.py, todo.py, task.py)
- [X] T002 [P] Create tests directory structure (tests/unit/, tests/integration/)
- [ ] T003 [P] Configure pytest for testing

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create Task model in task.py with id, title, description, is_completed attributes
- [X] T005 Create Todo class in todo.py with in-memory storage mechanism (Python list)
- [X] T006 [P] Create basic test files for Task model (tests/unit/test_task.py) and Todo class (tests/unit/test_todo.py)
- [X] T007 Implement auto-incrementing ID generation strategy starting from 1 in todo.py
- [X] T008 [P] Create main.py with basic application structure and entry point
- [X] T009 Create CLI menu structure in main.py with command parsing
- [X] T010 Implement command dispatcher to map user commands to business logic functions in main.py
- [X] T011 Implement main application loop that continues until exit command in main.py
- [X] T012 Add graceful shutdown mechanism when exit command is received in main.py
- [X] T013 Implement application initialization and startup sequence in main.py
- [X] T014 Add comprehensive error handling for application startup failures in main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Implement business logic for adding a new task with required title and optional description, ensuring validation and default incomplete status

**Independent Test**: The application allows users to add tasks with a required title and optional description, assigns a unique ID, and marks the task as incomplete by default. The task should appear in the task list when viewed.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T014 [P] [US1] Unit test for Task creation with required title validation in tests/unit/test_task.py
- [X] T015 [P] [US1] Unit test for Task creation with optional description in tests/unit/test_task.py
- [X] T016 [US1] Unit test for Task creation with default incomplete status in tests/unit/test_task.py
- [X] T017 [US1] Unit test for Todo.add_task method with validation in tests/unit/test_todo.py
- [X] T018 [US1] Integration test for add command with title only in tests/integration/test_cli.py
- [X] T019 [US1] Integration test for add command with title and description in tests/integration/test_cli.py
- [X] T020 [US1] Integration test for add command with missing title (error case) in tests/integration/test_cli.py

### Implementation for User Story 1

- [X] T021 [US1] Implement Task constructor with validation for required title in task.py
- [X] T022 [US1] Set default values for Task attributes (is_completed=False, description="") in task.py
- [X] T023 [US1] Implement Todo.add_task method with validation and auto-ID assignment in todo.py
- [X] T024 [US1] Implement CLI add command in main.py with argument parsing
- [X] T025 [US1] Add validation for required title in task creation in main.py
- [X] T026 [US1] Add user-friendly success response formatting for add command in main.py
- [X] T027 [US1] Add user-friendly error handling with actionable guidance for missing title in main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to view all tasks with their ID, title, description, and completion status

**Independent Test**: The application displays all tasks with their ID, title, description, and completion status in a clear, readable format.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T028 [P] [US2] Unit test for Todo.get_all_tasks functionality in tests/unit/test_todo.py
- [X] T029 [US2] Integration test for view command in tests/integration/test_cli.py

### Implementation for User Story 2

- [X] T030 [US2] Implement Todo.get_all_tasks method to retrieve from in-memory storage in todo.py
- [X] T031 [US2] Implement CLI view command in main.py with argument parsing
- [X] T032 [US2] Format task display with ID, title, description, and completion status in main.py
- [X] T033 [US2] Implement clear status indicators for completed/incomplete tasks (e.g., ✔/✖) in main.py
- [X] T034 [US2] Format task display with consistent alignment and spacing in main.py
- [X] T035 [US2] Add clear visual separators between different tasks in the list view in main.py
- [X] T036 [US2] Add handling for empty task list with appropriate user message in main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Details (Priority: P2)

**Goal**: Implement logic to update an existing task's title and/or description by task ID, including validation for invalid or non-existent IDs

**Independent Test**: The application allows users to update the title and/or description of an existing task by its ID, while preserving the task ID and other properties. The application properly validates task IDs and returns appropriate error messages for invalid or non-existent IDs.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T039 [P] [US3] Unit test for Todo.update_task functionality with valid ID in tests/unit/test_todo.py
- [X] T040 [P] [US3] Unit test for Todo.update_task with invalid/non-existent ID in tests/unit/test_todo.py
- [X] T041 [US3] Unit test for Todo.update_task with partial updates (title only, description only) in tests/unit/test_todo.py
- [X] T042 [US3] Integration test for update command with valid ID in tests/integration/test_cli.py
- [X] T043 [US3] Integration test for update command with invalid ID in tests/integration/test_cli.py
- [X] T044 [US3] Integration test for update command with missing ID in tests/integration/test_cli.py

### Implementation for User Story 3

- [X] T045 [US3] Implement Todo.update_task method with ID lookup in in-memory storage in todo.py
- [X] T046 [US3] Add validation in Todo.update_task to check for non-existent IDs in todo.py
- [X] T047 [US3] Implement logic to update only provided fields (title and/or description) in todo.py
- [X] T048 [US3] Preserve task ID and other properties when updating in todo.py
- [X] T049 [US3] Implement CLI update command in main.py with argument parsing
- [X] T050 [US3] Add validation in CLI to ensure task exists before updating in main.py
- [X] T051 [US3] Add error handling for invalid/non-existent IDs in main.py
- [X] T052 [US3] Format success response for update command in main.py

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P2)

**Goal**: Implement logic to delete a task by its ID from in-memory storage, handling invalid IDs gracefully without crashing the application

**Independent Test**: The application allows users to delete a task by its ID, removing it from the system completely. The application properly validates task IDs and handles invalid IDs gracefully without crashing, returning appropriate error messages.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T056 [P] [US4] Unit test for Todo.delete_task functionality with valid ID in tests/unit/test_todo.py
- [X] T057 [P] [US4] Unit test for Todo.delete_task with invalid/non-existent ID in tests/unit/test_todo.py
- [X] T058 [US4] Unit test for Todo.delete_task error handling without crashing in tests/unit/test_todo.py
- [X] T059 [US4] Integration test for delete command with valid ID in tests/integration/test_cli.py
- [X] T060 [US4] Integration test for delete command with invalid ID in tests/integration/test_cli.py
- [X] T061 [US4] Integration test for delete command error handling without crashing in tests/integration/test_cli.py

### Implementation for User Story 4

- [X] T062 [US4] Implement Todo.delete_task method with ID lookup and removal from in-memory storage in todo.py
- [X] T063 [US4] Add validation in Todo.delete_task to check for non-existent IDs in todo.py
- [X] T064 [US4] Add error handling in Todo.delete_task to prevent crashes on invalid IDs in todo.py
- [X] T065 [US4] Implement CLI delete command in main.py with argument parsing
- [X] T066 [US4] Add validation in CLI to ensure task exists before deletion in main.py
- [X] T067 [US4] Add error handling in CLI to prevent crashes on invalid IDs in main.py
- [X] T068 [US4] Add user-friendly success response formatting for delete command in main.py
- [X] T069 [US4] Add user-friendly error response formatting with actionable guidance for invalid ID cases in main.py

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Tasks Complete/Incomplete (Priority: P2)

**Goal**: Implement logic to mark a task as complete or incomplete by ID, ensuring correct state updates and validation

**Independent Test**: The application allows users to mark a task as complete or incomplete by its ID, correctly updating the task's state. The application properly validates task IDs and returns appropriate error messages for invalid or non-existent IDs.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T070 [P] [US5] Unit test for Todo.mark_complete functionality with valid ID in tests/unit/test_todo.py
- [X] T071 [P] [US5] Unit test for Todo.mark_incomplete functionality with valid ID in tests/unit/test_todo.py
- [X] T072 [US5] Unit test for Todo.mark_complete/mark_incomplete with invalid/non-existent ID in tests/unit/test_todo.py
- [X] T073 [US5] Unit test for correct state transition from incomplete to complete in tests/unit/test_todo.py
- [X] T074 [US5] Unit test for correct state transition from complete to incomplete in tests/unit/test_todo.py
- [X] T075 [US5] Integration test for complete command with valid ID in tests/integration/test_cli.py
- [X] T076 [US5] Integration test for incomplete command with valid ID in tests/integration/test_cli.py
- [X] T077 [US5] Integration test for complete/incomplete commands with invalid ID in tests/integration/test_cli.py

### Implementation for User Story 5

- [X] T078 [US5] Implement Todo.mark_complete method with ID lookup in in-memory storage in todo.py
- [X] T079 [US5] Implement Todo.mark_incomplete method with ID lookup in in-memory storage in todo.py
- [X] T080 [US5] Add validation in Todo.mark_complete/mark_incomplete to check for non-existent IDs in todo.py
- [X] T081 [US5] Ensure correct state updates in Todo.mark_complete/mark_incomplete methods in todo.py
- [X] T082 [US5] Implement CLI complete command in main.py with argument parsing
- [X] T083 [US5] Implement CLI incomplete command in main.py with argument parsing
- [X] T084 [US5] Add validation in CLI to ensure task exists before changing status in main.py
- [X] T085 [US5] Add error handling for invalid/non-existent IDs in main.py
- [X] T086 [US5] Add user-friendly success response formatting for complete/incomplete commands in main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T081 [P] Documentation updates in README.md
- [X] T082 Code cleanup and refactoring
- [X] T083 Performance optimization for CLI responsiveness
- [X] T084 [P] Implement comprehensive input validation across all CLI commands in main.py
- [X] T085 [P] Add comprehensive error handling for all user inputs in main.py
- [X] T086 [P] Implement user-friendly CLI menu with clear instructions in main.py
- [X] T087 [P] Add input sanitization for all user-provided values in main.py
- [X] T088 [P] Improve console output formatting for task list display in main.py
- [X] T089 [P] Implement clear status indicators for completed/incomplete tasks (e.g., ✔/✖) in main.py
- [X] T090 [P] Add color coding for different task statuses in console output in main.py
- [X] T091 [P] Format task display with consistent alignment and spacing in main.py
- [X] T092 [P] Implement user-friendly success messages for all operations in main.py
- [X] T093 [P] Implement user-friendly error messages with actionable guidance in main.py
- [X] T094 [P] Add clear visual separators between different tasks in the list view in main.py
- [X] T095 [P] Add graceful shutdown handling for unexpected errors in main.py
- [X] T096 [P] Add comprehensive error handling for invalid input across all commands in main.py
- [X] T097 [P] Add specific error handling for incorrect task IDs in all operations in main.py
- [X] T098 [P] Add error handling for edge cases like empty task lists in all operations in main.py
- [X] T099 [P] Additional unit tests (if requested) in tests/unit/
- [X] T100 Security hardening for input validation
- [X] T101 Run quickstart.md validation

---

## Phase V: Validation & Acceptance Testing

**Purpose**: Manually validate all Phase I features against the acceptance criteria, ensuring all five basic features work correctly and the application runs without errors

- [X] T102 [P] Validate 'Add New Tasks' feature works correctly per acceptance criteria in main.py
- [X] T103 [P] Validate 'View All Tasks' feature works correctly per acceptance criteria in main.py
- [X] T104 [P] Validate 'Update Task Details' feature works correctly per acceptance criteria in main.py
- [X] T105 [P] Validate 'Delete Tasks' feature works correctly per acceptance criteria in main.py
- [X] T106 [P] Validate 'Mark Tasks Complete/Incomplete' feature works correctly per acceptance criteria in main.py
- [X] T107 [P] Perform end-to-end testing of all features together without errors in main.py
- [X] T108 [P] Validate error handling works correctly for all invalid inputs in main.py
- [X] T109 [P] Verify application runs without errors for all basic operations in main.py
- [X] T110 [P] Confirm all acceptance criteria from spec.md are met in the implementation

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
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services (in this case, Task model before Todo methods)
- Core implementation before CLI integration
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
Task: "Unit test for Task creation with required title validation in tests/unit/test_task.py"
Task: "Unit test for Task creation with optional description in tests/unit/test_task.py"
Task: "Unit test for Task creation with default incomplete status in tests/unit/test_task.py"
Task: "Unit test for Todo.add_task method with validation in tests/unit/test_todo.py"
Task: "Integration test for add command with title only in tests/integration/test_cli.py"
Task: "Integration test for add command with title and description in tests/integration/test_cli.py"
Task: "Integration test for add command with missing title (error case) in tests/integration/test_cli.py"

# Launch all implementation for User Story 1 together:
Task: "Implement Task constructor with validation for required title in task.py"
Task: "Set default values for Task attributes (is_completed=False, description=) in task.py"
Task: "Implement Todo.add_task method with validation and auto-ID assignment in todo.py"
Task: "Implement CLI add command in main.py with argument parsing"
Task: "Add validation for required title in task creation in main.py"
Task: "Add success response formatting for add command in main.py"
Task: "Add error handling for missing title in main.py"
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
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
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