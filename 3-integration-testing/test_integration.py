import unittest
from service import (
    process_and_store,
    retrieve_processed,
    update_value,
    delete_value,
    list_all_keys,
)
from datastore import database


class TestIntegration(unittest.TestCase):
    def setUp(self):
        database.clear()

    def test_process_store_and_retrieve(self):
        result = process_and_store("name", "  john  ")
        self.assertEqual(result, "JOHN")
        retrieved = retrieve_processed("name")
        self.assertEqual(retrieved, "john")

    def test_update_value(self):
        process_and_store("city", "london")
        update_value("city", "paris")
        retrieved = retrieve_processed("city")
        self.assertEqual(retrieved, "paris")

    def test_delete_value(self):
        process_and_store("temp", "value")
        result = delete_value("temp")
        self.assertTrue(result)
        retrieved = retrieve_processed("temp")
        self.assertIsNone(retrieved)

    def test_delete_nonexistent(self):
        result = delete_value("nonexistent")
        self.assertFalse(result)

    def test_list_all_keys(self):
        process_and_store("key1", "value1")
        process_and_store("key2", "value2")
        keys = list_all_keys()
        self.assertEqual(len(keys), 2)
        self.assertIn("key1", keys)
        self.assertIn("key2", keys)

    def test_retrieve_nonexistent_key(self):
        result = retrieve_processed("does_not_exist")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
