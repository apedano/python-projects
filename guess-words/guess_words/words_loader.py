import os
import random

from guess_words.commons import words_length, WordsGameException


class WordsLoader:
    def __init__(self, filename, word_length: int):
        self.__filename = filename
        self.__word_length = word_length
        if not os.path.isfile(filename):
            raise WordsGameException("Given words file [{}] is not a valid file".format(filename))

    def choose_random_word(self):
        words = self.__load()
        # pick a random element from a list of strings.
        return random.choice(words)

    def __load(self):
        with open(self.__filename) as words_file:
            words = [line.rstrip('\n') for line in words_file]
            self.__validate(words)
            return words

    def __validate(self, words):
        if len(words) == 0:
            raise WordsGameException("Words files does not contain any word")
        # use comprehension

        wrong_words = [w for w in words if len(w) != words_length]
        if len(wrong_words) > 0:
            raise WordsGameException(
                "The words [{}] are not {} chars long. Fix it and retry".format(
                        "-".join(wrong_words), words_length)
            )

