##Read readcalc
from readcalc import readcalc

calc_1 = readcalc.ReadCalc("A ladder.")
calc = readcalc.ReadCalc("""In the mid-1970’s, Walter Alvarez, a geologist, was studying Earth’s polarity. It had recently been learned that the orientation of the planet’s magnetic field reverses, so that every so often, in effect, south becomes north and vice versa. Alvarez and some colleagues had found that a certain formation of pinkish limestone in Italy, known as the scaglia rossa, recorded these occasional reversals. The limestone also contained the fossilized remains of millions of tiny sea creatures called foraminifera. Alvarez became interested in a thin layer of clay in the limestone that seemed to have been laid down around the end of the Cretaceous Period. Below the layer, certain species of foraminifera—or forams, for short—were preserved. In the clay layer, there were no forams. Above the layer, the earlier species disappeared and new forams appeared. Having been taught the uniformitarian view, which held that any apparent extinctions throughout geological time resulted from the incompleteness of the fossil record’ rather than an actual extinction, Alvarez was not sure what to make of the lacuna in geological time corresponding to the missing foraminifera, because the change looked very abrupt""")
calc_2 = readcalc.ReadCalc("A father beaver, a mother beaver, and their four little beavers lived in a home in a lake.")

class text:
    def __init__(self, calc):
        self.num_sentences = len(calc.get_sentences())
        self.num_words = len(calc.get_words())
        def __get_number_chars(words):
            """
                Returns the total number of chars in the text.
            """
            chars = 0
            for word in words:
                chars += len(word)
            return chars
        words = calc.get_words()
        self.num_letters = __get_number_chars(words = words)
        from dalechallwords import dale_chall_words
        def __get_dale_chall_difficult_words(words):
            return len([word for word in words if word not in dale_chall_words])

        self.dale_chall_word = __get_dale_chall_difficult_words(words)

    def get_bormuth(self, calc):
        self.Readability = 0.886593 - 0.083640*(self.num_letters/self.num_words) + 0.161911*(self.dale_chall_word/self.num_words)**3 -0.021401*(self.num_words/self.num_sentences) + 0.000577*(self.num_words/self.num_sentences)**2 - 0.000005*(self.num_words/self.num_sentences)**3
        return self.Readability

    def get_DRP_units(self):
        self.Readability = self.get_bormuth(calc)
        self.DRP_units = (1 - self.Readability) * 100
        return self.DRP_units

texts = text(calc_2)
texts.get_bormuth(calc_2)
texts.get_DRP_units()
