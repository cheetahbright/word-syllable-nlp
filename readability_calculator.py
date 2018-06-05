##Read readcalc
from readcalc import readcalc
calc_1 = readcalc.ReadCalc("A ladder.")
calc = readcalc.ReadCalc("""In the mid-1970’s, Walter Alvarez, a geologist, was studying Earth’s polarity. It had recently been learned that the orientation of the planet’s magnetic field reverses, so that every so often, in effect, south becomes north and vice versa. Alvarez and some colleagues had found that a certain formation of pinkish limestone in Italy, known as the scaglia rossa, recorded these occasional reversals. The limestone also contained the fossilized remains of millions of tiny sea creatures called foraminifera. Alvarez became interested in a thin layer of clay in the limestone that seemed to have been laid down around the end of the Cretaceous Period. Below the layer, certain species of foraminifera—or forams, for short—were preserved. In the clay layer, there were no forams. Above the layer, the earlier species disappeared and new forams appeared. Having been taught the uniformitarian view, which held that any apparent extinctions throughout geological time resulted from the incompleteness of the fossil record’ rather than an actual extinction, Alvarez was not sure what to make of the lacuna in geological time corresponding to the missing foraminifera, because the change looked very abrupt""")
calc_2 = readcalc.ReadCalc("My favorite snow is the happy snow that flutters down in friendly flakes smiling from peacful piles then invites me into powdery games laughing all the while and becomes a man of snowball shapes wearing a frosty smile.")
def get_bormuth(calc):
    num_sentences = len(calc.get_sentences())
    num_words = len(calc.get_words())
    def __get_number_chars(words):
        """
            Returns the total number of chars in the text.
        """
        chars = 0
        for word in words:
            chars += len(word)
        return chars
    num_letters = __get_number_chars(words = calc.get_words())

    from dalechallwords import dale_chall_words
    def __get_dale_chall_difficult_words(words):
        return len([word for word in words if word not in dale_chall_words])

    dale_chall_words = __get_dale_chall_difficult_words(words = calc.get_words())
    Readability = 0.886593 - 0.083640*(num_letters/num_words) + 0.161911*(dale_chall_words/num_words)**3 -0.021401*(num_words/num_sentences) + 0.000577*(num_words/num_sentences)**2 - 0.000005*(num_words/num_sentences)**3
    return Readability

def get_DRP_units(calc):
    Readability = get_bormuth(calc)
    DRP_units = (1 - Readability) * 100
    return DRP_units

test = get_DRP_units(calc_2)
print(test)
