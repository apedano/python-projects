import string
from dataclasses import dataclass


class WordChecker:

    wrong_char_placeholder = "_"

    def __init__(self, word_to_guess: string):
        self.__word_to_guess = word_to_guess

    def check(self, guess):
        result: CheckResult = CheckResult()
        for g in guess:
            if not g in self.__word_to_guess:
                result.wrong_chars.append(g)
                result.word += WordChecker.wrong_char_placeholder
                break





@dataclass
class CheckResult:
    wrong_position_chars: list()
    wrong_chars: list()
    word: string

