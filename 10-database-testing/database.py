import sqlite3
import os

DB_NAME = "test_users.db"


def get_connection():
    raise NotImplementedError("Implement get_connection using TDD")


def init_database():
    raise NotImplementedError("Implement init_database using TDD")


def create_user(name, email, age=None):
    raise NotImplementedError("Implement create_user using TDD")


def get_user_by_id(user_id):
    raise NotImplementedError("Implement get_user_by_id using TDD")


def get_user_by_email(email):
    raise NotImplementedError("Implement get_user_by_email using TDD")


def get_all_users():
    raise NotImplementedError("Implement get_all_users using TDD")


def update_user(user_id, name=None, email=None, age=None):
    raise NotImplementedError("Implement update_user using TDD")


def delete_user(user_id):
    raise NotImplementedError("Implement delete_user using TDD")


def delete_all_users():
    raise NotImplementedError("Implement delete_all_users using TDD")


def drop_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
