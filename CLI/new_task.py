import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.task_creator import main

def create_task(task_name):
    main(task_name)
    print(f"Task '{task_name}' created successfully")

if __name__ == '__main__':
    task_name = input("New Task Name: ")
    create_task(task_name)