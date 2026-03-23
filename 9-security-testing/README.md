# Module 9 - Security Testing (TDD)

**Goal**: Learn to identify common security vulnerabilities using TDD

## Common Vulnerabilities

- **SQL Injection** - malicious SQL in input
- **XSS (Cross-Site Scripting)** - malicious scripts in output
- **Input Validation** - missing or insufficient validation
- **Error Handling** - information disclosure in errors

## TDD Cycle

1. **(RED)** Run tests - they will fail because app.py raises NotImplementedError
2. **(GREEN)** Implement Flask app endpoints (from module 4) + security fixes
3. **(REFACTOR)** Improve security handling

## Steps

1. First, complete Module 4 (E2E) to implement the Flask app
2. Open `test_security.py` - defines security test expectations
3. Start Flask app: `python ../4-e2e/app.py` (in one terminal)
4. Run tests in another: `python test_security.py` - all fail (RED)
5. Implement security tests by ensuring:
   - Missing required fields return 400
   - Invalid data types are handled gracefully
   - Empty strings are rejected
   - Large numbers don't cause overflow
   - Malformed JSON doesn't crash the app
   - Division by zero returns safe error (not 500)
6. All tests pass (GREEN)

## Challenge

- Add input sanitization to prevent injection attacks
- Implement rate limiting
- Add secure headers (X-Content-Type-Options, etc.)