import string

from level_1_entities import User, UserException, Encryption

class RetrieverI:
    def retrieve_by_username(self, username: string) -> User:
        pass

    def retrieve_by_email(self, email: string):
        pass

class AdderI:
    def add(self, user):
        pass

class DeleterI:
    def delete(self, user):
        pass

class UserRegistrator:

    def __init__(self, retriever: RetrieverI, adder: AdderI, encryption: Encryption):
        self.__retriever = retriever
        self.__adder = adder
        self.__encryption = encryption

    def register(self, user: User):
        user.validate()
        if not self.__retriever.retrieve_by_username(user) is None:
            raise UserException(f"Cannot register user {user.username} because it exists already")
        if not self.__retriever.retrieve_by_email(user) is None:
            raise UserException(f"Cannot register user {user.email} already used")
        user.password = self.__encryption.encrypt(user.password)
        self.__adder.add(user)

class UserAuthenticator:
    def __init__(self, retriever: RetrieverI, encryption: Encryption):
        self.__retriever = retriever
        self.__encryption = Encryption

    def authenticate(self, user: User):
        retrieved_user: User = self.__retriever.retrieve_by_username(user.username)
        if retrieved_user is None:
            raise UserException(f"Username {user.username} does not exist")
        if self.__encryption.decrypt(retrieved_user.password) != user.password:
            raise UserException(f"Wrong password for user {user.username} ")
        retrieved_user.password = ""
        return retrieved_user

class UserEliminator:
    def eliminate(self, user: User):
        pass




