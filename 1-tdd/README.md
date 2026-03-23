# Module 1 - TDD (Test-Driven Development)

**Goal**: Experiment with the TDD development methodology

## TDD Cycle

1. **(RED)** Write a test, run it - it should fail
2. **(GREEN)** Write minimal code to make the test pass
3. **(REFACTOR)** Improve code while keeping tests passing

## Steps

### Part A: Factorial

1. Open `test_factorial.py` - defines expected behavior
2. Open `factorial.py` - function raises NotImplementedError
3. **(RED)** Run `python test_factorial.py` - tests fail
4. **(GREEN)** Implement `factorial(n)` in factorial.py:
   - factorial(0) = 1
   - factorial(1) = 1
   - factorial(n) = n * factorial(n-1)
   - Raise ValueError for negative numbers
5. Run tests until all pass

### Part B: Fibonacci (Challenge)

1. Open `test_fibonacci.py` - defines expected behavior
2. **(RED)** Run `python test_fibonacci.py` - tests fail
3. **(GREEN)** Add `fibonacci(n)` function to factorial.py:
   - fibonacci(0) = 0
   - fibonacci(1) = 1
   - fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
   - Raise ValueError for negative numbers
4. Run tests until all pass

## Tip

Write the test first, then implement. This is the core of TDD.
