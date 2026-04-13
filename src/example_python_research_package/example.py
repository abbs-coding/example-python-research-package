"""
This module contains anexample function that demonstrate basic text
processing tasks, such as counting words in a string.
"""


def count_words(text: str) -> int:
    """Count the number of words in a piece of text.
    Words are defined as whitespace-separated tokens.

    Args:
        text: Input text.

    Returns:
        The number of words in the text.

    Raises:
        ValueError: If the input text is empty or only contains whitespace.
    """
    if text.strip() == "":
        raise ValueError("Text must contain at least one word")

    words = text.split()
    return len(words)
