# Module 10 - Database Testing

**Goal**: Learn to test database operations and ensure data integrity

## Context

Database testing verifies:
- CRUD operations (Create, Read, Update, Delete)
- Data integrity and constraints
- Transactions and rollback
- Query performance

## Steps

1. Install SQLite (already included in Python)
2. Open `database.py` - contains a simple user database
3. Open `test_database.py` - contains test stubs
4. Run `python test_database.py` to see which tests fail

## Tasks to implement

### Test Create operations
- `test_create_user` - create a new user
- `test_create_duplicate_user` - handle unique constraint

### Test Read operations
- `test_get_user_by_id` - retrieve user by ID
- `test_get_user_by_email` - retrieve user by email
- `test_get_all_users` - retrieve all users

### Test Update operations
- `test_update_user` - update user fields
- `test_update_nonexistent` - handle non-existent user

### Test Delete operations
- `test_delete_user` - delete a user
- `test_delete_nonexistent` - handle non-existent user

### Test Data Integrity
- `test_unique_email_constraint` - verify emails are unique
- `test_required_fields` - verify required fields are enforced

## Key Concepts

- Use `setUp` to create fresh database for each test
- Use `tearDown` to clean up
- Test both success and failure cases
- Verify data in database matches expected state