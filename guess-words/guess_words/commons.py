import string
from dataclasses import dataclass

words_length:int = 5

class WordsGameException(Exception):
    pass

@dataclass
class CheckResult:
    wrong_position_chars = set()
    wrong_chars = set()
    word: string = ""