import sys
from pathlib import Path
import uuid
import logging

CORE_DIR = Path(__file__).resolve().parents[2] / "core"
CORE_DIR.mkdir(exist_ok=True)

LOG_FILE = CORE_DIR / "terminal_bench.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)




PROJECT_ROOT = Path.cwd()
TASKS_DIR = PROJECT_ROOT / "tasks"


def return_status(task_name, **kwargs):
    logging.info(f"return_status() called with task_name={task_name}")
    task_path = TASKS_DIR / task_name

    if not task_path.exists():
        logging.info(f"Task '{task_name}' not found. Creating new task...")
        print(f"Task '{task_name}' not found. Creating new task...")
        sys.path.insert(0, str(Path(__file__).parent))
        from terminal_bench.CLI.new_task import create_task
        create_task(task_name)
        print(f"Please add code to tasks/{task_name}/agents/agent.py and run again")
        return {"run_id": "N/A", "status": "task_created"}

    run_id = str(uuid.uuid4())
    logging.info(f"Generated run_id={run_id}")
    kwargs["run_id"] = run_id

    sys.path.insert(0, str(TASKS_DIR))
    task_module = __import__(f"{task_name}.main", fromlist=["main"])

    status = task_module.main(task_name, **kwargs)
    if not status:
        status = kwargs.get("status", "unknown")

    return {"run_id": run_id, "status": status}


def run_task(task_name=None):
    if not task_name:
        if len(sys.argv) < 2:
            print("Usage: run-task <task_name>")
            return
        task_name = sys.argv[1]

    logging.info(f"Running task {task_name}")
    res = return_status(task_name)
    print(f"Status: {res['status']}")

def main():
    run_task()


if __name__ == "__main__":
    main()
