import string
from level_2_use_case_logic import User
from dataclasses import dataclass
from level_2_use_case_logic import UserRegistrator, UserAuthenticator, UserEliminator


@dataclass
class UserDto:
    id: int
    user: string
    psw: string
    mail: string

    def __init__(self, user:User):
        self.user=user.username
        self.mail=user.email
        self.psw=""

class UserAdapter:
    def from_dto_to_entity(self, user_dto: UserDto) -> User:
        pass

    def from_entity_to_dto(self, user: User) -> UserDto:
        pass

class UserDao:
    def load_by_id(self, id: int):
        pass

    def load_by_username(self, username: string):
        pass

    def delete(self, id: int):
        pass

class UserFacade:
    def __init__(self,
                 registrator: UserRegistrator,
                 authenticator: UserAuthenticator,
                 eliminator: UserEliminator,
                 user_adapter: UserAdapter):
        self.__registrator = registrator
        self.__authenticator = authenticator
        self.__eliminator = eliminator
        self.__adapter = user_adapter

    def register_user(self, user_dto: UserDto):
        return self.__registrator.register(
            self.__adapter.from_dto_to_entity(user_dto))

    def authenticate_user(self, user_dto: UserDto):
        return self.__authenticator.authenticate(
            self.__adapter.from_dto_to_entity(user_dto)
        )

    def eliminate_user(self, user_dto: UserDto):
        return self.__eliminator.eliminate(
            self.__adapter.from_dto_to_entity(user_dto)
        )