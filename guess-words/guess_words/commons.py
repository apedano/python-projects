import string
from dataclasses import dataclass

words_length:int = 5

class WordsGameException(Exception):
    pass

@dataclass
class CheckResult:

    def __init__(self):
        self.wrong_position_chars = set([])
        self.wrong_chars = set([])
        self.word: string = ""

