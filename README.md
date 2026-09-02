# Python Persistent To-Do List CLI

A modular, terminal-based task management utility built in Python. Implements full CRUD (Create, Read, Update, Delete) data operations backed by local JSON file storage for data persistence across sessions.

## Features
- **Data Persistence:** Tasks are serialized and saved automatically to `tasks.json`.
- **Full CRUD Support:** Add new tasks, view formatted lists, mark items complete, and delete old entries.
- **Input Guardrails:** Built-in exception handling for invalid numeric inputs and empty task titles.
- **Zero External Dependencies:** Built entirely with native Python modules (`json` and `os`).

## How to Run

1. Open your terminal in the project directory.
2. Execute the application script:

```bash
python main.py