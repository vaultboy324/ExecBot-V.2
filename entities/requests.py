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
