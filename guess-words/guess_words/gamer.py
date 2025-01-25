from word_checker import WordChecker
from words_loader import WordsLoader
from commons import words_length, CheckResult

class Gamer():

    def __init__(self):
        self.__word_loader = WordsLoader('../word_files.txt',
                                         words_length)

    def start_game(self, max_attempts):
        word_to_guess = self.__word_loader.choose_random_word()
        word_checker :WordChecker = WordChecker(word_to_guess)
        print(f'Iniziamo a giocare! Hai {max_attempts} tentativi possibili.')
        exit_sequence = 'X'
        for attempt in range(1, max_attempts+1, 1):
            print(f'Tentativo # {attempt} di {max_attempts}.')
            word_attempted =  ""
            while True:
                word_attempted = input(f' Inserisci la parola da indovinare da {words_length} caratteri ({exit_sequence} per uscire):')
                if word_attempted == exit_sequence:
                    return
                if len(word_attempted) != words_length:
                    print(f'Inserire una parola di {words_length} lettere')
                    continue
                if len(word_attempted) == words_length:
                    break
            check_result: CheckResult = word_checker.check(word_attempted)
            if check_result.word == word_to_guess:
                print(f'Congratulazioni hai indovinato la parola segreta {word_to_guess}!')
                return
            print(f'Corrette: {check_result.word}')
            print(f'Corrette in posizione sbagliata: {check_result.wrong_position_chars}')
            print(f'Errate: {check_result.wrong_chars}')
        print('Sei stato una mezza sega, non hai indovinato!')









