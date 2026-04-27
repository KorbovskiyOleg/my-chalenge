# My challenge on Code

## How to run tests
==================

To run all tests:
```bash
python -m unittest discover -s tests -v
```

To run a specific test file:
```bash
python -m unittest tests.test_task1 -v
```

## Project Structure
==================
```
/workspace
├── src/              # Source code for tasks
│   ├── __init__.py
│   ├── task1.py      # First task implementation
│   ├── task2.py      # Create this for your next task
│   └── ...
│
└── tests/            # Unit tests for tasks
    ├── __init__.py
    ├── test_task1.py # Tests for task1.py
    ├── test_task2.py # Create this when you create task2.py
    └── ...
```

## Workflow
=========
1. Create your task implementation in `src/taskN.py`
2. I will create corresponding tests in `tests/test_taskN.py`
3. Run tests using the command above
