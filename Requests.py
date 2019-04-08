import User


class Requests:

    @staticmethod
    def get_user_by_logpass(user: User, db_cursor):
        uname = user.get_uname()
        password = user.get_password()

        db_cursor.execute(f"SELECT * FROM users WHERE uname = '{uname}' AND password = '{password}'")
        user = db_cursor.fetchall()
        return user
