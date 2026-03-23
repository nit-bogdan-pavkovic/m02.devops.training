# Module 7 - Test Coverage

**Goal**: Learn to measure and improve code coverage

## Context

Code coverage measures how much of your source code is executed during tests. Common metrics:
- **Line coverage** - percentage of lines executed
- **Branch coverage** - percentage of branches taken
- **Function coverage** - percentage of functions called

## Steps

1. Open `calculator.py` - contains functions to test
2. Open `test_calculator.py` - contains basic tests
3. First, run tests normally: `python -m pytest test_calculator.py -v`
4. Install coverage: `pip install coverage`
5. Run with coverage:
   ```bash
   coverage run -m pytest test_calculator.py
   coverage report
   ```
6. See which lines are not covered - look for "Missing" column
7. Add more tests to improve coverage to 100%
8. Generate HTML report: `coverage html`
   - Open `htmlcov/index.html` in browser to see visual coverage

## Goals

- Achieve >80% line coverage
- Identify and cover edge cases
- Understand what coverage doesn't tell you

## Additional Commands

```bash
# Show coverage with missing lines
coverage report -m

# Run specific module coverage
coverage run --source=calculator -m pytest test_calculator.py

# Combine coverage from multiple test runs
coverage combine
```