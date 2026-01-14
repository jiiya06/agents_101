### Overview 

`terminal_bench` is a **basic Python-based agent system** built as a learning project and first step into agent-oriented workflows.

The agent automates simple tasks such as:
- Creating files and directories
- Printing a “Hello World” output
- Generating log files
- Verifying execution status using Pytest
- Creating new, templated task directories if they do not already exist

This project is intentionally minimal and exploratory. Work is still in progress, and updates are being pushed incrementally.

---

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
### Local (Virtual Environment)

```bash
cd terminal_bench
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
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

### Docker
```bash
docker-compose up --build
```

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

### Notes
- This project is a learning exercise, not a production-ready framework.
- Structure may change as experimentation continues.
- Contributions, suggestions, and feedback are welcome.
