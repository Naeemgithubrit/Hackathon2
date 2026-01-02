---
id: 1
title: Create Todo Constitution
stage: constitution
date: 2025-12-30
surface: agent
model: Qwen
feature: todo-console-app
branch: main
user: Naeem Shah
command: /sp.constitution
labels: [constitution, todo-app, python]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
 - .specify/templates/spec-template.md
 - .specify/templates/tasks-template.md
tests:
 - null
---

## Prompt

```
---
description: Create or update the project constitution from interactive or provided principle inputs, ensuring all dependent templates stay in sync.
handoffs: 
  - label: Build Specification
    agent: sp.specify
    prompt: Implement the feature specification based on the updated constitution. I want to build...
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

1. Load the existing constitution template at `.specify/memory/constitution.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

2. Collect/derive values for placeholders:
   - If user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated constitution content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

6. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

8. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.


/sp.constitution # SP CONSTITUTION
Project: In-Memory Todo Console Application  
Phase: I (Basic Level)  
Version: 1.0  

---

## 1. PURPOSE

This constitution defines the development rules, constraints, and standards for building
a Phase I command-line Todo application using **spec-driven development** with
**Claude Code** and **Spec-Kit Plus**.

The application must store all data **in memory only** and demonstrate clean,
maintainable, and testable Python code.

---

## 2. OBJECTIVE

Build a Python console-based Todo application that allows users to:

- Add tasks
- View tasks
- Update tasks
- Delete tasks
- Mark tasks as complete or incomplete

All features must follow specifications generated and evolved using Claude Code.

---

## 3. SCOPE (PHASE I ONLY)

### Included
- In-memory task storage (no database, no files)
- Command-line interface (CLI)
- Python 3.13+
- Single-user interaction
- Basic task lifecycle management

### Excluded
- Persistence (file or database)
- Authentication or users
- GUI or web interface
- External APIs

---

## 4. FUNCTIONAL REQUIREMENTS

The application MUST implement all **five (5) Basic Level features**:

1. **Add Task**
   - Accept title (required)
   - Accept description (optional)
   - Auto-generate unique task ID
   - Default status: incomplete

2. **View Tasks**
   - List all tasks
   - Display:
     - Task ID
     - Title
     - Description
     - Completion status (✔ Complete / ✖ Incomplete)

3. **Update Task**
   - Update title and/or description by task ID
   - Preserve task ID
   - Validate task existence

4. **Delete Task**
   - Delete task by ID
   - Handle invalid IDs gracefully

5. **Mark Task Complete / Incomplete**
   - Toggle task completion status by ID

---

## 5. NON-FUNCTIONAL REQUIREMENTS

- Code must follow **clean code principles**
- Functions should be small and single-purpose
- Meaningful variable and function names
- No global mutable state outside controlled structures
- Graceful error handling (no crashes on bad input)

---

## 6. ARCHITECTURE RULES

### Project Structure (MANDATORY)
```

## Response snapshot

I have successfully updated the project constitution for your In-Memory Todo Console Application. Here's what was accomplished:

**New Version and Bump Rationale:**
- Version: 1.0.0 (initial version)
- This is a new constitution specifically tailored for the Todo Console Application, replacing the generic template

**Files Updated:**
- ✅ `.specify/memory/constitution.md` - Updated with specific principles for the Todo application
- ✅ `.specify/templates/plan-template.md` - Updated to align with constitution requirements
- ✅ `.specify/templates/spec-template.md` - Updated to align with constitution requirements
- ✅ `.specify/templates/tasks-template.md` - Updated to align with constitution requirements

**Constitution Highlights:**
- Defines 6 core principles including in-memory storage, CLI interface, test-first approach, clean code architecture, error handling, and Python 3.13+ standards
- Specifies all 5 required functional requirements (add, view, update, delete, mark tasks)
- Establishes architecture rules and project structure
- Includes governance section for future amendments

**Suggested Commit Message:**
`docs: create constitution for Todo Console Application v1.0.0`

The constitution is now ready for use in your spec-driven development process. All dependent templates have been updated to align with the new constitution, ensuring consistency across your development workflow.

## Outcome

- ✅ Impact: Created new constitution for Todo Console Application and updated dependent templates
- 🧪 Tests: No tests required for this task
- 📁 Files: Updated constitution.md and 3 template files
- 🔁 Next prompts: Ready to proceed with feature specification
- 🧠 Reflection: Successfully implemented the constitution update process with proper template alignment

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A