import string
from abc import ABC, abstractmethod
from dataclasses import dataclass

class UserException(Exception):
    pass

class Encryption(ABC):

    @abstractmethod
    def encrypt(self, plain: string) -> string:
        pass

    @abstractmethod
    def decrypt(self, encrypted: string) -> string:
        pass

@dataclass
class User:
    username: string
    password: string
    email: string

    def __init__(self, encryption: Encryption):
        self.__encryption = encryption

    def _check_validity(self) -> string:
        pass

    def validate(self):
        validation_message: string = self.is_valid()
        if not self.is_valid() is None:
            raise UserException(f"User is not valid: {validation_message}")








