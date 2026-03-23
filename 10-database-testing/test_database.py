import unittest
import database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        database.init_database()
        database.delete_all_users()

    def tearDown(self):
        database.delete_all_users()

    def test_create_user(self):
        pass

    def test_create_duplicate_user(self):
        pass

    def test_get_user_by_id(self):
        pass

    def test_get_user_by_email(self):
        pass

    def test_get_all_users(self):
        pass

    def test_update_user(self):
        pass

    def test_update_nonexistent(self):
        pass

    def test_delete_user(self):
        pass

    def test_delete_nonexistent(self):
        pass


if __name__ == "__main__":
    unittest.main()
