# Module 2 - Unit tests (TDD)

**Goals**
- implement unit tests using TDD
- compare writing tests after vs before the code

## TDD Cycle

1. **(RED)** Run tests - they will fail because functions raise NotImplementedError
2. **(GREEN)** Implement each function in `math_sum.py` until tests pass
3. **(REFACTOR)** Improve code if needed

## Steps

1. Open and examine `test_math_sum.py` - it defines expected behavior
2. Open `math_sum.py` - functions raise NotImplementedError
3. Run tests: `python test_math_sum.py` - all tests fail (RED)
4. Implement `add` function to pass first test
5. Continue implementing each function: subtract, multiply, divide
6. Handle edge cases: division by zero should raise ValueError
7. Run tests until all pass (GREEN)

## Challenge

After passing all tests, add these functions using TDD:
- power (a^b) - raise ValueError for negative exponents
- modulo (a % b) - raise ValueError if divisor is zero


