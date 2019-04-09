from entities.user import User

from helper.db_helper import DBRequest


class RequestsHelper:

    @staticmethod
    def get_user(user: User, request: DBRequest):
        cursor = request.get_cursor()
        cursor.execute(f"SELECT * FROM users WHERE _id = '{user.get_id()}'")
        return cursor.fetchall()

    @staticmethod
    def insert_user(user: User, request: DBRequest):
        cursor = request.get_cursor()
        cursor.execute(f"INSERT INTO users VALUES ('{user.get_id()}', '{user.get_uname()}', '{user.get_password()}')")

    @staticmethod
    def update_uname(user:  User, request: DBRequest):
        cursor = request.get_cursor()
        cursor.execute(f"UPDATE users SET uname = '{user.get_uname()}' WHERE _id = '{user.get_id()}'")

    @staticmethod
    def update_password(user: User, request: DBRequest):
        cursor = request.get_cursor()
        cursor.execute(f"UPDATE users SET password = '{user.get_password()}' WHERE _id = '{user.get_id()}'")

    @staticmethod
    def delete_user(user: User, request: DBRequest):
        cursor = request.get_cursor()
        cursor.execute(f"DELETE FROM users WHERE _id = '{user.get_id()}'")

