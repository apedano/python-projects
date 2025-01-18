import pytest
from guess_words.words_loader import WordsLoader
from guess_words.commons import words_length, WordsGameException

test_filename = "test_words.txt"

def prepare_test_words(word_list):
    # w writes the file overwriting the content
    with open(test_filename, 'w') as test_words_file:
        test_words_file.writelines(word_list)

def test_words_loader_valid_file():
    words = ["micio\n", "mamma\n", "cuore"]
    prepare_test_words(words)
    words_loader: WordsLoader = WordsLoader(test_filename, words_length)
    words_loader.load()

def test_words_loader_invalid_file():
    with pytest.raises(WordsGameException, match="Given words file .* is not a valid file"):
        WordsLoader("invalid_file.txt", words_length)

def test_words_loader_with_empty_file():
    with pytest.raises(WordsGameException, match="Words files does not contain any word"):
        prepare_test_words(list())
        words_loader = WordsLoader(test_filename, words_length)
        words_loader.load()

def test_words_loader_with_words_exceeding_length():
    with pytest.raises(WordsGameException, match="The words \\[troppo_lunga\\] are not 5 chars long. Fix it and retry"):
        prepare_test_words(["micio\n", "troppo_lunga\n", "cuore"])
        words_loader = WordsLoader(test_filename, words_length)
        words_loader.load()






