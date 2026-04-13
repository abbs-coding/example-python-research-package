import pytest

from example_python_research_package.example import count_words


def test_count_words_simple_sentence():
    text = "This is a simple sentence"
    assert count_words(text) == 5


def test_count_words_multiple_spaces():
    text = "This   sentence    has   extra spaces"
    assert count_words(text) == 5


def test_count_words_single_word():
    text = "Hello"
    assert count_words(text) == 1


def test_count_words_raises_on_empty_text():
    with pytest.raises(ValueError):
        count_words("")


def test_count_words_raises_on_whitespace_only():
    with pytest.raises(ValueError):
        count_words("   ")
