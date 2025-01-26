import string
from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: string
    password: string
    email: string

@dataclass
class UserDto:
    user: string
    psw: string
    mail: string

    def __init__(self, user:User):
        self.user=user.username
        self.mail=user.email
        self.psw=""

class UserException(Exception):
    pass

class UserRegistratorI:
    def register(self, user_dto: UserDto):
        pass

class UserAuthenticatorI:
    def authenticate(self, user_dto: UserDto):
        pass

class UserEliminatorI:
    def eliminate(self, user_dto: UserDto):
        pass

class UserFacade:
    def __init__(self,
                 registrator: UserRegistratorI,
                 authenticator: UserAuthenticatorI,
                 eliminator: UserEliminatorI):
        self.__registrator = registrator
        self.__authenticator = authenticator
        self.__eliminator = eliminator

    def register_user(self, user_dto:UserDto):
        return self.__registrator.register(user_dto)

    def authenticate_user(self, user_dto:UserDto):
        return self.__authenticator.authenticate(user_dto)

    def eliminate_user(self, user_dto:UserDto):
        return self.__eliminator.eliminate(user_dto)




