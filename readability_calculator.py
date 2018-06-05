##Read readcalc
calc = readcalc.ReadCalc("""In the mid-1970’s, Walter Alvarez, a geologist, was studying Earth’s polarity. It had recently been learned that the orientation of the planet’s magnetic field reverses, so that every so often, in effect, south becomes north and vice versa. Alvarez and some colleagues had found that a certain formation of pinkish limestone in Italy, known as the scaglia rossa, recorded these occasional reversals. The limestone also contained the fossilized remains of millions of tiny sea creatures called foraminifera. Alvarez became interested in a thin layer of clay in the limestone that seemed to have been laid down around the end of the Cretaceous Period. Below the layer, certain species of foraminifera—or forams, for short—were preserved. In the clay layer, there were no forams. Above the layer, the earlier species disappeared and new forams appeared. Having been taught the uniformitarian view, which held that any apparent extinctions throughout geological time resulted from the incompleteness of the fossil record’ rather than an actual extinction, Alvarez was not sure what to make of the lacuna in geological time corresponding to the missing foraminifera, because the change looked very abrupt""")
calc.get_smog_index()
calc.analyse_text()
calc
