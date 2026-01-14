# Overview

This is my first, basic, python-based agent. Basically a 101 to the journey of building agent systems, not much—but I learnt a lot.
The agent automates and performs a basic task to create a file and a print Hello world, create log files, check the validity and verify status using Pytest, and creating new, templated, empty task directories, if it already doesn't exist. Also implemented basic docker and setuptools. Work still in progress, updates being pushed.


## Project Structure
```
terminal_bench/
├── CLI/
│   ├── new_task.py         
│   ├── run_task.py         
│   └── status_checker.py  
├── core/
│   └── task_creator.py     
└── tasks/
    └── task_helloworld/   
        ├── agents/        
        ├── results/       
        ├── solutions/      
        ├── tests/         
        ├── main.py         
        └── tasks.yaml      
```

## Installation
```bash
cd terminal_bench
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
```

## Usage

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
