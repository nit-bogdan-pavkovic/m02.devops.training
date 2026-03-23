# Module 3 - Integration testing

**Goal**: implement integration tests

## Steps

1. Open `datastore.py` and `service.py` files and examine how they work
2. The service now includes:
   - `process_and_store(key, raw_value)` - process and store a value
   - `retrieve_processed(key)` - retrieve processed value
   - `update_value(key, raw_value)` - update existing value
   - `delete_value(key)` - delete a value
   - `list_all_keys()` - list all stored keys
3. Open `test_integration.py` and examine its content
4. Remove the `pass` keyword from the tests and implement:
   - test_process_store_and_retrieve
   - test_update_value
   - test_delete_value
   - test_list_all_keys
   - test_retrieve_nonexistent_key
5. Confirm that all tests work using `python test_integration.py`
