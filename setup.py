from setuptools import setup, find_packages

setup(
    name="terminal-bench",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "tsk=terminal_bench.cli:cli"
        ]
    },
)

