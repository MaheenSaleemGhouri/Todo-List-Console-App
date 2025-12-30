---
id: 001
title: Update Constitution
stage: constitution
date: 2025-12-30
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: user
command: /sp.constitution
labels: [constitution, setup, governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

```text
You are an expert Python developer, agentic AI engineer, and professional project mentor with deep experience in spec-driven development, Claude Code workflows, and console-based applications.

You MUST strictly follow this constitution whenever the user types "/sp.constitution", provides specifications, or asks to start development.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STRICT CONSTITUTION RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ❗ PROJECT TYPE (NON-NEGOTIABLE)
- This is a Python console (CLI) application.
- No frontend, no web UI, no APIs.
- No database (in-memory data only).
- No authentication.
- No manual coding by the user — ALL code must be generated via Claude Code.
- Use Spec-Kit Plus + Agentic Dev Stack workflow ONLY.

2. ❗ MANDATORY DEVELOPMENT FLOW (ORDER CANNOT CHANGE)

You MUST follow these phases in exact order:

Phase 1: Project Understanding & Requirement Confirmation
Phase 2: Specification Writing (Spec-Kit Plus format)
Phase 3: Implementation Plan Generation
Phase 4: Task Breakdown (Atomic, Executable Tasks)
Phase 5: Claude Code Implementation
Phase 6: Console Testing & Edge Case Review
Phase 7: Code Quality Review & Refactoring Notes
Phase 8: Final Deliverables & Documentation

❌ Never skip, merge, or reorder phases without explicit user approval.

3. ❗ TECHNOLOGY STACK (FIXED)

- Language: Python 3.13+
- Environment Manager: UV
- App Type: In-memory Python Console Application
- Entry Point: /src/main.py (single main file)
- AI Tools: Claude Code, Spec-Kit Plus
- OS: Linux / WSL 2 (for Windows users)

Do NOT suggest or introduce:
- React, Node.js, Express
- Databases (MongoDB, PostgreSQL, etc.)
- Web frameworks
- Cloud services
- Authentication systems

4. ❗ CORE APPLICATION FEATURES (MANDATORY)

The application MUST implement ALL of the following:

- Add Todo (title + description)
- View all Todos with status indicators
- Update Todo (title/description)
- Delete Todo by ID
- Mark Todo as Complete / Incomplete

Todos must:
- Be stored in memory (list/dictionary)
- Have unique IDs
- Show clear status in console output

5. ❗ SPEC-DRIVEN DEVELOPMENT RULES

- Every implementation must be based on a written specification.
- Specs must be clear, versioned, and iteration-friendly.
- Each change requires:
  → Updated spec
  → Updated plan
  → Updated task list

Never write code without an approved spec.

6. ❗ CLAUDE CODE RULES

- Claude Code generates ALL Python code.
- The user NEVER writes code manually.
- Code must be clean, readable, and modular.
- Follow Python best practices and naming conventions.
- Comments ONLY where logic is non-obvious.

7. ❗ PROJECT STRUCTURE (MANDATORY)

GitHub repository MUST contain:

/sp.constitution
/specs-history/
/src/
  └── main.py
README.md
CLAUDE.md

8. ❗ DOCUMENTATION REQUIREMENTS

README.md MUST include:
- Project overview
- Features list
- Python & UV setup instructions
- How to run the console app
- Example console usage

CLAUDE.md MUST include:
- How Claude Code was used
- Rules followed during development
- Spec-Kit Plus workflow explanation

9.
```

## Response snapshot

The constitution has been successfully updated with the following key changes:

**New Version**: 1.0.0 (Initial version)
**Bump Rationale**: This is the initial constitution for the Todo CLI App project, establishing core principles for the Python console application development.

**Key Principles Established**:
1. Console-First Application - Focus on CLI interface with no web UI or APIs
2. In-Memory Data Storage - Simple, fast operation without external databases
3. Spec-Driven Development - All implementations must be based on written specifications
4. Claude Code Generation - All Python code must be generated via Claude Code
5. Core Todo Functionality - Mandatory features for todo management
6. Python Technology Stack - Using Python 3.13+ with UV as environment manager

**Files Updated**:
- `.specify/memory/constitution.md` - Contains the complete constitution with all required principles and guidelines

**Suggested Commit Message**: `docs: add initial constitution for Todo CLI App v1.0.0`

The constitution aligns with the project requirements specified by the user, emphasizing Python console application development with todo management functionality, using Claude Code for all implementation, and following spec-driven development practices.

## Outcome

- ✅ Impact: Created initial project constitution with all required principles and guidelines
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with comprehensive constitution
- 🔁 Next prompts: Specification writing phase will follow
- 🧠 Reflection: Constitution properly established core principles for Python console app

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS - All required elements included
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin specification writing phase