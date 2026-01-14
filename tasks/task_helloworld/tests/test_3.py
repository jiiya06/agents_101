from pathlib import Path

def test_hello_world():
    hello_path = Path('../results/results.txt')
    content = hello_path.read_text()
    assert "Hello, World!" in content

if __name__ == "__main__":
    test_hello_world()
    print("test 3 passed")