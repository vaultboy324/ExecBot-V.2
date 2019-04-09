from entities.user import User

from helper.requests_helper import RequestsHelper
from helper.db_helper import DBRequest


class Requests:

    @staticmethod
    def get_user(user: User):
        request = DBRequest()

        data = RequestsHelper.get_user(user, request)

        request.close()

        return data

    @staticmethod
    def insert_user(user: User):
        request = DBRequest()

        RequestsHelper.insert_user(user, request)

        request.complete()
        request.close()

    @staticmethod
    def check_user(user: User):
        request = DBRequest()

        data = RequestsHelper.get_user(user, request)

        request.complete()
        request.close()

        #Здесь добавить проверку на существование пользователя
        if data:
            return True
        return False

    @staticmethod
    def check_password(user: User):
        request = DBRequest()

        data = RequestsHelper.get_user(user, request)

        request.complete()
        request.close()

        #Здесь добавить проверку на корректность пароля
        if not data[0][2]:
            return False
        return True

    @staticmethod
    def update_name(user: User):
        request = DBRequest()

        RequestsHelper.update_uname(user, request)

        request.complete()
        request.close()

    @staticmethod
    def update_password(user: User):
        request = DBRequest()

        RequestsHelper.update_password(user, request)

        request.complete()
        request.close()

    @staticmethod
    def delete_user(user: User):
        request = DBRequest()

        RequestsHelper.delete_user(user, request)

        request.complete()
        request.close()