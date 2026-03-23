# Module 3 - Integration testing (TDD)

**Goal**: implement integration tests using TDD

## TDD Cycle

1. **(RED)** Run tests - they will fail because functions raise NotImplementedError
2. **(GREEN)** Implement functions in datastore.py and service.py
3. **(REFACTOR)** Improve code if needed

## Steps

1. Open `test_integration.py` - it defines expected behavior for the service
2. Open `datastore.py` and `service.py` - functions raise NotImplementedError
3. Run tests: `python test_integration.py` - all tests fail (RED)
4. Implement `datastore.py` first:
   - `store_value(key, value)` - store in dictionary
   - `get_value(key)` - retrieve from dictionary
   - `delete_value(key)` - remove from dictionary
   - `list_keys()` - return all keys
5. Then implement `service.py`:
   - `process_and_store(key, raw_value)` - trim whitespace, uppercase, store
   - `retrieve_processed(key)` - get value, return lowercase
   - `update_value(key, raw_value)` - update existing value
   - `delete_value(key)` - delete a value
   - `list_all_keys()` - list all keys
6. Run tests until all pass (GREEN)

## Tip

Start with datastore.py, test it in isolation, then build the service layer on top.
