from run_task import return_status

def check_status():
    task_name = input("Task Name: ")
    result = return_status(task_name)
    print(f"Run ID: {result['run_id']}")
    print(f"Status: {result['status']}")

if __name__ == '__main__':
    check_status()