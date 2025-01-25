from word_checker import WordChecker
from words_loader import WordsLoader

class Gamer():

    def __init__(self, word_loader: WordLoader, word_checker: WordChecker):
        self.__word_loader = word_loader
        self.__word_checker = word_checker

    def start_game(self, max_attempts):
        attempts = 0
