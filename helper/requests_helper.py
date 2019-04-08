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
        cursor.execute(f"INSERT INTO users VALUES ('{user.get_id()}', 'TEST00')")
