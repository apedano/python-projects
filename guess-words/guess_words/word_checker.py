import string
from guess_words.commons import CheckResult


class WordChecker:

    wrong_char_placeholder = "_"

    def __init__(self, word_to_guess: string):
        self.__word_to_guess = word_to_guess

    def check(self, guess):
        result: CheckResult = CheckResult()
        index:int = 0
        for g in guess:
            if not g in self.__word_to_guess:
                result.wrong_chars.add(g)
                result.word += WordChecker.wrong_char_placeholder
            elif self.__word_to_guess[index] == g:
                result.word += g
            else:
                result.word += WordChecker.wrong_char_placeholder
                result.wrong_position_chars.add(g)
            index+=1
        return result








