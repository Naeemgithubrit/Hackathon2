---
id: 3
title: Create Todo Plan
stage: plan
date: 2025-12-30
surface: agent
model: Qwen
feature: basic-todo-app
branch: 001-basic-todo-app
user: Naeem Shah
command: /sp.plan
labels: [planning, todo-app, python]
links:
  spec: specs/001-basic-todo-app/spec.md
  plan: specs/001-basic-todo-app/plan.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-basic-todo-app/plan.md
 - specs/001-basic-todo-app/research.md
 - specs/001-basic-todo-app/data-model.md
 - specs/001-basic-todo-app/quickstart.md
 - specs/001-basic-todo-app/contracts/cli-contract.md
 - QWEN.md
tests:
 - null
---

## Prompt

```
---
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
handoffs: 
  - label: Create Tasks
    agent: sp.tasks
    prompt: Break the plan into tasks
    send: true
  - label: Create Checklist
    agent: sp.checklist
    prompt: Create a checklist for the following domain...
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType qwen`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

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


/sp.plan You are acting as a Spec-Kit Plus planning agent.

Context:
- Project: In-Memory Todo Console Application
- Phase: I (Basic Level)
- Language: Python 3.13+
- Interface: Command-Line (Console)
- Data Storage: In-memory only
- Constitution: Follow /sp.constitution strictly
- Specification Source: /specs-history/phase-1-basic-todo-spec.md

Objective:
Create a clear, step-by-step implementation plan to build the Phase I Todo application
based strictly on the approved specification.

Planning Requirements:
- The plan MUST translate the specification into actionable development steps
- No implementation code is allowed
- No features outside Phase I may be introduced
- Each step must be simple, atomic, and easy to follow
- The plan should be suitable for execution by Claude Code

Plan Structure:
Organize the plan into logical phases and steps, including:

1. Project Setup
   - Environment setup using UV
   - Folder and file structure creation
   - Entry point definition

2. Data Model Design
   - Task entity definition
   - In-memory storage strategy
   - ID generation approach

3. Business Logic Layer
   - Task creation logic
   - Task retrieval and listing logic
   - Task update logic
   - Task deletion logic
   - Task completion toggle logic

4. CLI Interaction Layer
   - Menu design
   - User input handling
   - Output formatting
   - Error handling for invalid input

5. Integration Flow
   - Connecting CLI to business logic
   - Application control flow
   - Exit behavior

6. Validation and Testing (Manual)
   - Validation of each feature against acceptance criteria
   - Edge case verification
   - Error scenario testing

Constraints:
- No persistence
- No external libraries
- No GUI
- No async or multithreading
- No optimization beyond clarity and correctness

Output Rules:
- Use numbered steps
- Use clear, concise language
- Do NOT include Python code
- Do NOT repeat the full specification
- Do NOT modify or reinterpret requirements

Deliverable:
Produce a finalized implementation plan suitable for use with `/sp.implement`,
and store it as:

`/specs-history/phase-1-basic-todo-plan.md`
```

## Response snapshot

I have successfully completed the implementation plan for the Phase I Todo application. Here's what was accomplished:

**Branch**: `001-basic-todo-app`

**Plan File Path**: `C:\Users\Naeem shah\Desktop\TODO\specs\001-basic-todo-app\plan.md`

**Generated Artifacts**:
- `research.md` - Research summary with technology decisions
- `data-model.md` - Detailed data model for the Task entity
- `quickstart.md` - Quickstart guide for the application
- `contracts/cli-contract.md` - CLI interface contract
- Updated agent context in `QWEN.md`

**Constitution Compliance**: All constitutional requirements have been verified and confirmed in the plan:
- ✅ In-Memory Data Storage
- ✅ Command-Line Interface
- ✅ Test-First approach
- ✅ Clean Code Architecture
- ✅ Error Handling
- ✅ Python 3.13+ Standards

**Project Structure**: The plan follows the architecture rules specified in the constitution with:
- `main.py` - Entry point and CLI interface
- `todo.py` - Core Todo class with in-memory storage
- `task.py` - Task model/data structure
- `tests/` - Unit and integration tests

The implementation plan is now ready for the next phase. You can proceed with `/sp.tasks` to break the plan into specific implementation tasks.

## Outcome

- ✅ Impact: Created comprehensive implementation plan for Todo Console Application
- 🧪 Tests: No tests required for this task
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, contracts/cli-contract.md
- 🔁 Next prompts: Ready to proceed with task breakdown
- 🧠 Reflection: Successfully implemented the planning process with all required artifacts

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A