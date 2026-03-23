import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"


class TestSecurity(unittest.TestCase):
    def test_missing_field_a(self):
        pass

    def test_missing_field_b(self):
        pass

    def test_invalid_data_type(self):
        pass

    def test_empty_string_value(self):
        pass

    def test_very_large_number(self):
        pass

    def test_malformed_json(self):
        pass

    def test_division_by_zero_returns_safe_error(self):
        pass


if __name__ == "__main__":
    unittest.main()
