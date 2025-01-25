from guess_words.word_checker import WordChecker
from guess_words.commons import CheckResult


def test_correct_word():
    word_to_guess = "principe"
    word_checker: WordChecker = WordChecker(word_to_guess)
    check_result: CheckResult = word_checker.check(word_to_guess)
    assert check_result.word == word_to_guess

def test_not_correct_chars():
    word_to_guess = "principe"
    word_checker: WordChecker = WordChecker(word_to_guess)
    check_result: CheckResult = word_checker.check("prascibe")
    assert check_result.word == "pr__ci_e"
    assert check_result.wrong_chars == {'a', 's', 'b'}
    assert check_result.wrong_position_chars == set()

def test_not_correct_position():
    word_to_guess = "principe"
    word_checker: WordChecker = WordChecker(word_to_guess)
    check_result: CheckResult = word_checker.check("prascibe")
    assert check_result.word == "pr__ci_e"
    assert check_result.wrong_chars == {'a', 's', 'b'}
    assert check_result.wrong_position_chars == set()


