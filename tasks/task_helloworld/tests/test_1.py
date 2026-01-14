from pathlib import Path

def hello_world_content():
    hello_path = Path('../results/hello.py')
    content = hello_path.read_text()
    assert "print" in content
    assert "Hello, World!" in content

if __name__ == "__main__":
    hello_world_content()
    print("test 2 passed")