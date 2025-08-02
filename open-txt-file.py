"""Experimental script for loading raw COCA text files.

This code was used during development to inspect the COCA dataset.
It relies on local files and is preserved for reference.
"""

import pandas as pd
import numpy as np
import os
import re
from collections import Counter


#import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
import nltk
nltk.download()


os.getcwd()


db_fic_1990 = pd.read_table(r"D:\COCA_Zipped_Files\db_fic_1990.txt", names = ["textID", "UNKNOWN", "wordID"], encoding="ISO-8859-1")
db_fic_1990.shape
db_fic_1990.head(10000)


data1.tail()
