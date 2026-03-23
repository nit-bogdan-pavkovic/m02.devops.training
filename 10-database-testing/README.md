# Module 10 - Database Testing (TDD)

**Goal**: Learn to test database operations and ensure data integrity using TDD

## Context

Database testing verifies:
- CRUD operations (Create, Read, Update, Delete)
- Data integrity and constraints
- Transactions and rollback
- Query performance

## TDD Cycle

1. **(RED)** Run tests - they will fail because functions raise NotImplementedError
2. **(GREEN)** Implement database functions in database.py
3. **(REFACTOR)** Improve code if needed

## Steps

1. Open `test_database.py` - defines expected CRUD behavior
2. Open `database.py` - functions raise NotImplementedError
3. Run tests: `python test_database.py` - all fail (RED)
4. Implement database.py functions:
   - `get_connection()` - return sqlite3 connection
   - `init_database()` - create users table with schema
   - `create_user(name, email, age)` - insert user, raise if email exists
   - `get_user_by_id(user_id)` - return user dict or None
   - `get_user_by_email(email)` - return user dict or None
   - `get_all_users()` - return list of user dicts
   - `update_user(user_id, ...)` - update user fields, return success
   - `delete_user(user_id)` - delete user, return success
   - `delete_all_users()` - clear all users
5. Handle edge cases:
   - Unique email constraint (IntegrityError)
   - Required fields validation
   - Nonexistent user handling
6. Run tests until all pass (GREEN)