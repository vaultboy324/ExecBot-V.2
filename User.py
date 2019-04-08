class User:
    def __init__(self, id, uname, password):
        self.set_id(id)
        self.set_uname(uname)
        self.set_password(password)
        pass

    def set_id(self, id):
        self.__id = id
        pass

    def set_uname(self, uname):
        self.__uname = uname
        pass

    def set_password(self, password):
        self.__password = self.__encrypt(password)
        pass

    def get_id(self):
        return self.__id

    def get_uname(self):
        return self.__uname

    def get_password(self):
        return self.__decrypt(self.__password)

    def __encrypt(self, string):
        code_string = string;
        return code_string;

    def __decrypt(self, string):
        encode_string = string;
        return encode_string;
