"""Tests for the :mod:`readability_calculator` module."""

import os
import sys

# Ensure the repository root is on ``sys.path`` so that the module under
# test can be imported when the tests are executed directly.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from readability_calculator import Text


class DummyCalc:
    """Simple stand-in for the ``readcalc`` object used by the library."""

    def __init__(self, words, sentences=1):
        self._words = words
        self._sentences = sentences

    def get_words(self):
        return self._words

    def get_sentences(self):
        return ["dummy"] * self._sentences


def test_dale_chall_difficult_word_count():
    """Words not present in the Dale–Chall list count as difficult."""

    words = ["cat", "dog", "xylophone"]
    calc = DummyCalc(words)
    t = Text(calc)
    # "cat" and "dog" are in the Dale-Chall list, but "xylophone" is not.
    assert t.dale_chall_word == 1

