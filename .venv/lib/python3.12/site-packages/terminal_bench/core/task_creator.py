import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

def main(task_name):
    command = f'cd tasks && mkdir {task_name} && cd {task_name} && mkdir agents results tests solutions && touch main.py tasks.yaml'
    run_command(command)
    command = f'cd tasks/{task_name}/agents && touch agent.py'
    run_command(command)