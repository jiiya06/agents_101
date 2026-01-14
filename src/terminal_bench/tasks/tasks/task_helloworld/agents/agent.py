import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout.strip(), result.stderr.strip()

def main():
    command = 'cd ../results && touch hello.py && echo "print(\\"Hello, World!\\")" > hello.py'
    run_command(command)
    command = 'cd ../results && touch results.txt && python3 hello.py > results.txt'
    run_command(command)

if __name__ == "__main__":
    main()