# agents_101

`agents_101` is a **foundational Python project** focused on understanding how agent-oriented systems are **structured, packaged, tested, and executed**, at a terminal level.

Rather than emphasizing complex agent behavior, this repository serves as a **learning and experimentation environment** for the architectural patterns, tooling, and workflows that underpin larger and more capable agent systems.

The project focuses on simple tasks such as:
- Agent automating creation of files and directories
- Agent printing an output, eg., "hello world"
- Generating log files
- Verifying execution status using Pytest
- Creating new, templated task directories if they do not already exist
- Use of UUIDs for task and execution identification  
- Packaging and distribution concepts (e.g. setuptools)  
- Environment isolation and containerization (Docker)


This project is intentionally minimal and exploratory. The emphasis is on **correct structure, reproducibility, and extensibility**.
Work is still in progress, and updates are being pushed incrementally.

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
