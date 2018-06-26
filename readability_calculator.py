##Read readcalc
from readcalc import readcalc
from nltk.tokenize import RegexpTokenizer # Regex handler
import re
#calc_1 = readcalc.ReadCalc("A ladder.")
#calc = readcalc.ReadCalc("""In the mid-1970’s, Walter Alvarez, a geologist, was studying Earth’s polarity. It had recently been learned that the orientation of the planet’s magnetic field reverses, so that every so often, in effect, south becomes north and vice versa. Alvarez and some colleagues had found that a certain formation of pinkish limestone in Italy, known as the scaglia rossa, recorded these occasional reversals. The limestone also contained the fossilized remains of millions of tiny sea creatures called foraminifera. Alvarez became interested in a thin layer of clay in the limestone that seemed to have been laid down around the end of the Cretaceous Period. Below the layer, certain species of foraminifera—or forams, for short—were preserved. In the clay layer, there were no forams. Above the layer, the earlier species disappeared and new forams appeared. Having been taught the uniformitarian view, which held that any apparent extinctions throughout geological time resulted from the incompleteness of the fossil record’ rather than an actual extinction, Alvarez was not sure what to make of the lacuna in geological time corresponding to the missing foraminifera, because the change looked very abrupt""")
text_4 = "Living things adapt to their environment so they  can  survive . An organism  adapts  when it develops  a  behavior  that makes it more likely to survive. It can  behavior  that makes it more likely to survive. It can  behavior also adapt by forming a physical characteristic or body  part that helps it survive. In a forest biome, some trees grow taller than the  other plants around them. This lets them reach the  sunlight. Growing taller is an adaptation that helps  trees survive. Shorter plants have adapted with their  behavior. They have learned to live in the shade with  less sunlight.  Animals in the forest have a wide variety of  adaptations. Monkeys have long tails. They can use  them almost like another hand. This helps them swing  quickly through the tops of trees. They can even  do this while holding their babies or gathering food.  Giraffes need to reach leaves at the tops of tall trees.  Having a long neck is an adaptation that allows them  to do this. Some animals adaptations prevent other animals  from wanting to eat them. A skunk’s horrible smell  makes larger animals choose something else to eat.  Even plants sometimes protect themselves in this  way. Roses and acacia trees both have dangerous  thorns. The thorns prevent animals from eating  their leaves."

text_3 = """What Australian mammal can leap 25 feet in one hop and move for short periods at 35 miles an hour? The red kangaroo. A full grown male stands as tall as a six foot person and weighs 200 pounds. This is slightly bigger than the grey kangaroo, making it the world’s largest marsupial. What’s a marsupial? A mammal where the mother has a pouch for carrying, feeding and protecting her young. While a red kangaroo may be the largest marsupial, the newborn baby is tiny, under an inch long. After a few months of sleeping, nursing and growing in mom’s stomach pouch the young kangaroo (joey) begins to come out. But it hurries back to the pouch fast when frightened, hungry or cold. Eventually, the joey gets so big it hangs out of the pouch. Then, at eight months old, it stays out. But the joey remains close to mom until ready to live on its own. Red kangaroos are good swimmers. However, they are best known for their hopping abilities. Their long, powerful hind legs have big feet. Hopping moves them quickly over their grassy, shrubby and desert habitats. Meanwhile, a thick tail helps them balance and steer. What do red kangaroos eat? Grass, leaves and other vegetation. And guess what - they often regurgitate food and chew their cud just like a cow. The red kangaroo’s vegetarian diet provides much of its water. It can also go long periods without drinking. Staying in the shade, panting and limiting most activity to nighttime helps the red kangaroo conserve water and stay cool. Red kangaroos travel together in groups called mobs. Mobs include both males and females, with one male being dominant. Males show their dominance by “boxing” with other males. They balance on their tails and try pushing each other off balance with their forearms or by kicking their hind legs. This kicking ability, along with their sharp claws, can also be used by kangaroos to defend against Australia’s wild dog, the dingo. """
#text_3 = "See spot run very quickly"
#text_3_clean = re.sub("([’]\w)", "", text_3)

#text_3_clean = re.sub("(\d+\s)", "", text_3_clean)

calc_3 = readcalc.ReadCalc(preprocesshtml = 'justext', text=text_3)

#text = text_3.lower()
#tokenizer = RegexpTokenizer(r'\w+')
#tokens = tokenizer.tokenize(text)
#tokens
calc_2 = readcalc.ReadCalc("The man is tall. He has a house.")

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
        print(f"THE WORDS ARE: {words}")
        self.num_letters = __get_number_chars(words = words)
        from dalechallwords import dale_chall_words
        def __get_dale_chall_difficult_words(words):
            return len([word for word in words if word in dale_chall_words])

        self.dale_chall_word = __get_dale_chall_difficult_words(words)

    def get_bormuth(self, calc):
        self.Readability = 0.886593 - (0.03640*(self.num_letters/self.num_words)) + (0.161911*(self.dale_chall_word/self.num_words)) - (0.021401*(self.num_words/self.num_sentences)) - (0.000577*(self.num_words/self.num_sentences)) - (0.000005*(self.num_words/self.num_sentences))
        #print(f"self.Readability = 0.886593 - (0.083640*({self.num_letters}/{self.num_words})) + (0.161911*({self.dale_chall_word}/{self.num_words})**3) - (0.021401*({self.num_words}/{self.num_sentences})) + (0.000577*({self.num_words}/{self.num_sentences})**2) - (0.000005*({self.num_words}/{self.num_sentences})**3)")
        print(self.Readability)
        return self.Readability

    def get_DRP_units(self, calc):
        self.Readability2 = self.get_bormuth(calc)
        self.DRP_units = (1 - self.Readability2) * 100
        return self.DRP_units

texts = text(calc_3)
texts.get_bormuth(calc_3)
texts.get_DRP_units(calc_3)
texts.dale_chall_word
calc_3
