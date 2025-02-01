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

class BaseUserManager:
    def __init__(self, retriever: RetrieverI):
        self._protected_retriever = retriever

    def _protected_retrieve_by_username(self, username: string):
        return self._protected_retriever.retrieve_by_username(username)

class UserRegistrator(BaseUserManager):

    def __init__(self, retriever: RetrieverI, adder: AdderI, encryption: Encryption):
        super().__init__(retriever)
        self.__adder = adder
        self.__encryption = encryption

    def register(self, user: User):
        user.validate()
        existing_user = self._protected_retrieve_by_username(user.username)
        if not existing_user is None:
            raise UserException(f"No user found with username: {user.username}")
        if not self._protected_retriever.retrieve_by_email(user.email) is None:
            raise UserException(f"Cannot register user {user.email} already used")
        user.password = self.__encryption.encrypt(user.password)
        self.__adder.add(user)

class UserAuthenticator(BaseUserManager):

    def __init__(self, retriever: RetrieverI, encryption: Encryption):
        super().__init__(retriever)
        self.__encryption = encryption
    def authenticate(self, user: User):

        retrieved_user: User = self._protected_retriever.retrieve_by_username(user.username)
        if retrieved_user is None:
            raise UserException(f"Username {user.username} not found")
        if self.__encryption.decrypt(retrieved_user.password) != user.password:
            raise UserException(f"Wrong password for user {user.username} ")
        retrieved_user.password = ""
        return retrieved_user

class UserEliminator(BaseUserManager):

    def __init__(self, deleter: DeleterI, retriever: RetrieverI):
        super().__init__(retriever)
        self.__deleter = deleter

    def eliminate(self, user: User):
        retrieved_user: User = self._protected_retriever.retrieve_by_username(user.username)
        if retrieved_user is None:
            raise UserException(f"Username {user.username} does not exist")
        self.__deleter.delete(user)