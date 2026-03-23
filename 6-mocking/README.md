# Module 6 - Mocking and Patching (TDD)

**Goal**: Learn to mock external dependencies and test in isolation using TDD

## Context

In real applications, code often depends on:
- External APIs
- Database connections
- File system operations
- Time/date functions
- Random number generators

Mocking allows us to test our code without these dependencies.

## TDD Cycle

1. **(RED)** Run tests - they will fail because functions raise NotImplementedError
2. **(GREEN)** Implement functions using mocking patterns
3. **(REFACTOR)** Improve code if needed

## Steps

1. Open `test_weather_service.py` - defines expected behavior
2. Open `api_client.py` and `weather_service.py` - raise NotImplementedError
3. Run tests: `python test_weather_service.py` - all fail (RED)
4. Implement `api_client.py`:
   - `fetch_weather_data(city)` - return dict with city, temp, condition, humidity
   - `fetch_forecast(city, days)` - return list of day forecasts
   - `get_current_hour()` - return current hour (0-23)
5. Implement `weather_service.py`:
   - `get_weather(city)` - call api_client.fetch_weather_data
   - `get_forecast(city, days)` - call api_client.fetch_forecast
   - `is_good_weather(conditions)` - return True if "sunny" or "partly cloudy"
   - `get_greeting_based_on_time()` - return greeting based on hour
6. Use `unittest.mock` to test without real API calls:

```python
from unittest.mock import Mock, patch

# Example: Mock an API response
def test_get_weather_success(self):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"temp": 25, "condition": "sunny"}
    
    with patch('weather_service.requests.get', return_value=mock_response):
        result = get_weather("London")
        self.assertEqual(result["temp"], 25)
```

7. Run tests until all pass (GREEN)

5. Implement these tests:
   - `test_get_weather_success` - mock successful API response
   - `test_get_weather_api_error` - mock failed API response
   - `test_get_weather_timeout` - mock timeout
   - `test_get_forecast_with_patch` - use @patch decorator
   - `test_get_current_time_mocked` - mock datetime for time-dependent code

## Key Concepts

- `Mock()` - creates a mock object
- `patch()` - replaces an object temporarily
- `@patch` - decorator version of patch
- `return_value` - set what the mock returns
- `side_effect` - set what the mock does when called

## Run the tests

```bash
python test_weather_service.py
```