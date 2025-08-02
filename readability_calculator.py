"""Utilities for computing readability metrics.

This module exposes a small ``Text`` class that can be used to
calculate several readability statistics for a piece of text.  The
original project bundled a large amount of experimental code and
executed it on import, which made the module difficult to use in other
code and impossible to test.  The implementation below keeps just the
relevant pieces and ensures the module can be imported safely.
"""

from typing import Sequence


class Text:
    """Container for text statistics used in readability metrics.

    The class expects a ``calc`` object that provides ``get_sentences``
    and ``get_words`` methods similar to those from the ``readcalc``
    library.  Only the pieces required for our tests are implemented
    here.
    """

    def __init__(self, calc) -> None:
        self.num_sentences = len(calc.get_sentences())
        words = calc.get_words()
        self.num_words = len(words)
        self.num_letters = sum(len(word) for word in words)

        from dalechallwords import dale_chall_words

        def __get_dale_chall_difficult_words(words: Sequence[str]) -> int:
            """Return the count of *difficult* words.

            The Dale–Chall readability metric considers words not present in
            the official word list to be difficult.  The previous
            implementation incorrectly counted words that *were* in the list,
            effectively inverting the metric.
            """

            return len([word for word in words if word not in dale_chall_words])

        self.dale_chall_word = __get_dale_chall_difficult_words(words)

    def get_bormuth(self, calc) -> float:
        self.Readability = (
            0.886593
            - (0.03640 * (self.num_letters / self.num_words))
            + (0.161911 * (self.dale_chall_word / self.num_words))
            - (0.021401 * (self.num_words / self.num_sentences))
            - (0.000577 * (self.num_words / self.num_sentences))
            - (0.000005 * (self.num_words / self.num_sentences))
        )
        print(self.Readability)
        return self.Readability

    def get_DRP_units(self, calc) -> float:
        self.Readability2 = self.get_bormuth(calc)
        self.DRP_units = (1 - self.Readability2) * 100
        return self.DRP_units


if __name__ == "__main__":
    from readcalc import readcalc

    text_3 = (
        "What Australian mammal can leap 25 feet in one hop and move for short "
        "periods at 35 miles an hour? The red kangaroo. A full grown male stands "
        "as tall as a six foot person and weighs 200 pounds."
    )

    calc_3 = readcalc.ReadCalc(preprocesshtml="justext", text=text_3)
    texts = Text(calc_3)
    texts.get_bormuth(calc_3)
    texts.get_DRP_units(calc_3)
    print(texts.dale_chall_word)

