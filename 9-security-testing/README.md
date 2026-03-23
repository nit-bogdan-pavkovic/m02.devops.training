# Module 9 - Security Testing

**Goal**: Learn to identify common security vulnerabilities in web applications

## Common Vulnerabilities

- **SQL Injection** - malicious SQL in input
- **XSS (Cross-Site Scripting)** - malicious scripts in output
- **Input Validation** - missing or insufficient validation
- **Authentication** - weak or missing auth

## Steps

1. Start the Flask app from exercise 4:
   ```bash
   cd ../4-e2e && python app.py
   ```

2. Open `test_security.py` and examine the test structure

3. Implement these security tests:

   ### Input Validation Tests
   - Test missing required fields (no "a" or "b" in request)
   - Test invalid data types (strings instead of numbers)
   - Test boundary values (very large numbers)
   - Test empty strings

   ### SQL Injection Prevention (if applicable)
   - Test that special characters are handled safely
   - Ensure errors don't expose database details

   ### XSS Prevention (if applicable)
   - Test that HTML/script tags in input are escaped

   ### Error Handling
   - Test that errors don't expose stack traces
   - Test graceful handling of malformed JSON

4. Run tests: `python test_security.py`

## Challenge

- Add tests for rate limiting (if implemented)
- Test for information disclosure in error messages
- Verify secure headers are present