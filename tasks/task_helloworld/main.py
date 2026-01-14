import subprocess
import uuid
from pathlib import Path

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.stdout.strip(), result.stderr.strip()

def main(task_name, **kwargs):
    run_id = kwargs.get('run_id', 'no-id')
    
    print(f"Task: {task_name}")
    print(f"Run ID: {run_id}")
    
    task_dir = Path(__file__).parent
    
    command = f'cd {task_dir}/agents && python3 agent.py'
    run_command(command)
    status = "verification_pending"
    kwargs['status'] = status
    
    command = f'cd {task_dir}/tests && python3 test_1.py'
    run_command(command)
    status = "test1_passed"
    kwargs['status'] = status
    
    command = f'cd {task_dir}/tests && python3 test_2.py'
    run_command(command)
    status = "test2_passed"
    kwargs['status'] = status
    
    command = f'cd {task_dir}/tests && python3 test_3.py'
    run_command(command)
    status = "test3_passed"
    kwargs['status'] = status
    
    status = "Successfully Completed"
    kwargs['status'] = status
    return status

if __name__ == "__main__":
    main("task_helloworld")