# Module 7 - Test Coverage (TDD)

**Goal**: Learn to measure and improve code coverage using TDD

## Context

Code coverage measures how much of your source code is executed during tests. Common metrics:
- **Line coverage** - percentage of lines executed
- **Branch coverage** - percentage of branches taken
- **Function coverage** - percentage of functions called

## TDD Cycle

1. **(RED)** Run tests - they will fail because functions raise NotImplementedError
2. **(GREEN)** Implement functions in calculator.py to make tests pass
3. **(REFACTOR)** Improve code, then measure coverage to find gaps

## Steps

1. Open `test_calculator.py` - defines expected behavior for all functions
2. Open `calculator.py` - functions raise NotImplementedError
3. Run tests: `python -m pytest test_calculator.py -v` - all fail (RED)
4. Implement each function in calculator.py to make tests pass:
   - add, subtract, multiply, divide
   - power, square_root, modulo
   - is_even, is_positive, factorial
5. Run tests until all pass (GREEN)
6. Install coverage: `pip install coverage`
7. Measure coverage:
   ```bash
   coverage run -m pytest test_calculator.py
   coverage report -m
   ```
8. Look at "Missing" column - these lines aren't tested
9. Add more test cases to achieve >80% coverage
10. Generate HTML report: `coverage html`

## Challenge

- Achieve 100% line coverage
- Add edge case tests for: negative numbers, zero, large numbers