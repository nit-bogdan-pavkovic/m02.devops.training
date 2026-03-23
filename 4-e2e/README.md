# Module 4 - End-to-end tests

**Goal**: implement end-to-end tests

## Steps

Create a virtualenv with the following code:

```shell
python -m venv venv
source venv/bin/activate
```

1. Install the dependencies using `pip install -r requirements.txt`
2. Open `app.py`, examine this Flask application - it now has:
   - GET `/` - Welcome message
   - POST `/add` - Add two numbers
   - POST `/subtract` - Subtract two numbers
   - POST `/multiply` - Multiply two numbers
   - POST `/divide` - Divide two numbers
   - GET `/health` - Health check endpoint
3. Open `test_e2e.py`, examine the test structure
4. Implement the following tests:
   - **test_home_page**: GET `/` returns 200 and "Welcome"
   - **test_add_endpoint**: POST `/add` with JSON `{"a": 5, "b": 3}` returns `{"result": 8}`
   - **test_subtract_endpoint**: POST `/subtract` with `{"a": 10, "b": 4}` returns `{"result": 6}`
   - **test_multiply_endpoint**: POST `/multiply` with `{"a": 3, "b": 7}` returns `{"result": 21}`
   - **test_divide_endpoint**: POST `/divide` with `{"a": 20, "b": 4}` returns `{"result": 5}`
   - **test_divide_by_zero**: POST `/divide` with `{"a": 10, "b": 0}` returns 400 error
   - **test_health_endpoint**: GET `/health` returns 200 and status "ok"
5. Run the Flask app (`python app.py`) in one terminal, then run tests in another: `python test_e2e.py`
 
