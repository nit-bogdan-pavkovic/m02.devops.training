# Module 6 - Mocking and Patching

**Goal**: Learn to mock external dependencies and test in isolation

## Context

In real applications, code often depends on:
- External APIs
- Database connections
- File system operations
- Time/date functions
- Random number generators

Mocking allows us to test our code without these dependencies.

## Steps

1. Open `api_client.py` - simulates an external API call
2. Open `weather_service.py` - uses the API client
3. Open `test_weather_service.py` - contains test stubs
4. Implement the tests using `unittest.mock`:

```python
from unittest.mock import Mock, patch

# Example: Mock an API response
def test_get_weather(self):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"temp": 25, "condition": "sunny"}
    
    with patch('weather_service.requests.get', return_value=mock_response):
        result = get_weather("London")
        self.assertEqual(result["temp"], 25)
```

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