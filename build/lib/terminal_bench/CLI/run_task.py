import sys
from pathlib import Path
import uuid

PROJECT_ROOT = Path.cwd()
TASKS_DIR = PROJECT_ROOT / "tasks"


def return_status(task_name, **kwargs):
    task_path = TASKS_DIR / task_name

    if not task_path.exists():
        print(f"Task '{task_name}' not found. Creating new task...")
        sys.path.insert(0, str(Path(__file__).parent))
        from terminal_bench.CLI.new_task import create_task
        create_task(task_name)
        print(f"Please add code to tasks/{task_name}/agents/agent.py and run again")
        return {"run_id": "N/A", "status": "task_created"}

    run_id = str(uuid.uuid4())
    kwargs["run_id"] = run_id

    sys.path.insert(0, str(TASKS_DIR))
    task_module = __import__(f"{task_name}.main", fromlist=["main"])

    status = task_module.main(task_name, **kwargs)
    if not status:
        status = kwargs.get("status", "unknown")

    return {"run_id": run_id, "status": status}


def run_task():
    task_name = input("Task Name: ").strip()
    res = return_status(task_name)
    print(f"Status: {res['status']}")


def main():
    run_task()


if __name__ == "__main__":
    main()
