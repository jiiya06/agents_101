# Overview

Hey there! This is my first, small, python-based agent. Agent automates and performs a basic task to create a file and a print Hello world, create log files, check the validity and status using Pytest, and creating new, templated, empty task directories, if it already doesn't exist. Work still in progress, updates being pushed.


## Project Structure
```
terminal_bench/
├── CLI/
│   ├── new_task.py         # Create new benchmark tasks
│   ├── run_task.py         # Execute tasks and run tests
│   └── status_checker.py   # Check task execution status
├── core/
│   └── task_creator.py     # Task scaffolding utilities
└── tasks/
    └── task_helloworld/    # Example task
        ├── agents/         # Agent implementations
        ├── results/        # Task outputs
        ├── solutions/      # Reference solutions
        ├── tests/          # Test cases
        ├── main.py         # Task execution logic
        └── tasks.yaml      # Task description
```

## Installation
```bash
cd terminal_bench
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
```

## Usage of task_helloworld

### Running a Task

Execute an existing task and run its test suite:
```bash
python CLI/run_task.py 

OR

tsk
```

When prompted, enter the task name (e.g., `task_helloworld`).

### Creating a New Task

Generate scaffolding for a new task:
```bash
python CLI/new_task.py
```

This creates the necessary directory structure and files for your task.

### Checking Task Status

Verify the execution status of a task:
```bash
python CLI/status_checker.py
```

## Task Structure

Each task follows a standard structure:

- `agents/agent.py` - The automated agent that attempts to complete the task
- `tests/` - Contains test cases to verify task completion
- `results/` - Directory where agent outputs are stored
- `solutions/` - Reference implementations
- `main.py` - Orchestrates agent execution and testing
- `tasks.yaml` - Describes task requirements
