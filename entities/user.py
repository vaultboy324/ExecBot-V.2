from helper.crypt_helper import Crypt_helper


class User:
    def __init__(self, id):
        self.set_id(id)
        pass

    def set_id(self, id):
        self.__id = id
        pass

    def set_uname(self, uname):
        self.__uname = uname
        pass

    def set_initial_password(self):
        self.__password = ""

    def set_password(self, password):
        self.__password = self.__encrypt(password)
        pass

    def get_id(self):
        return self.__id

    def get_uname(self):
        return self.__uname

    def get_password(self):
        return self.__password

    def create_new_user(self, id):
        if self.get_id() == 0:
            self.set_id(id)
        pass

    def create_user_by_response(self, sap_user):
        self.set_uname(sap_user[0][1])
        self.__password = sap_user[0][2]

    def get_encode_password(self):
        return self.__decrypt(self.__password).decode()

    def set_role(self, role):
        self.role = role
        pass

    def get_role(self):
        return self.role

    def set_task_list(self, tasks):
        self.task_list = []

        for task in tasks:
            self.__add_task_to_list(task)

        pass

    def get_task_list(self):
        return self.task_list

    def set_task_time(self, index, time):
        self.task_list[index] = time

    def __add_task_to_list(self, task):
        current_task = {}
        current_task["task"] = task["task"]
        current_task["time"] = task["time"]
        self.task_list.push(current_task)


    def __encrypt(self, string):
        key = Crypt_helper.get_hash_key()
        code_string = Crypt_helper.encrypt_string(string.encode(), key.encode());
        return code_string;

    def __decrypt(self, string):
        key = Crypt_helper.get_hash_key()
        encode_string = Crypt_helper.decrypt_string(string.encode(), key.encode());
        return encode_string;