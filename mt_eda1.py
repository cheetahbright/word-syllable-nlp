import pandas as pd
import numpy as np
import os
import pandassql
import re

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords



os.getcwd()


data1 = pd.read_table(r"data/coca-sources.txt", header = 0, skiprows=[1], encoding="ISO-8859-1")
data1.shape
data1.head()

data1.tail()

# Are all the rows of the last column nulls
all(data1.iloc[:,8].isnull())

col8_name = data1.columns[8]
data1.drop(col8_name, axis = 1, inplace = True)
data1.rename(columns={data1.columns[7]:col8_name}, inplace = True)

data1.head()
data1.tail()
data1.replace("--", np.nan, inplace = True )
data1.set_index("textID", inplace=True)
data1.subgen = data1.subgen.astype("category")

data1.nunique()
data1.genre.unique()

data1.describe()
data1.subgen.value_counts(normalize=True)


child_source_mask = data1["source"].str.lower().str.contains("child").fillna(False)
np.nansum(child_source_mask)
child_in_sources_df = data1[child_source_mask]

child_in_sources_df.head(20)


# Look at one row per sub genre
data1.groupby("subgen")["title", col8_name].last()


##

from collections import Counter


data_temp = data1[data1.subgen == 200.0]
data_temp.shape
data_temp.title[data_temp.title == np.nan]


all_titles = ""

for title in data_temp.title.values:
    all_titles = all_titles + " "+str(title)

len(all_titles)
tokenized_words = all_titles.split(" ")
counts = Counter(tokenized_words)
print(counts)

def count_words(list_of_titles):
    """

    """

    # Regex

    all_titles = ""
    for title in list_of_titles:
        all_titles = all_titles + " "+str(title)

    tokenized_words = all_titles.split(" ")
    cleaned_titles = [re.sub("\W+", "", str(title).lower()) for title in tokenized_words]
    len(cleaned_titles)
    counts = Counter(cleaned_titles)

    s = [(k, counts[k]) for k in sorted(counts, key=counts.get, reverse=True) if k not in stopwords.words('english')]

    return(s[:10])

#subgen_gb = data1.groupby("subgen")

list_of_titles1 = data1.groupby("subgen")["title"].apply(list)
word_counts = [count_words(x) for x in list_of_titles1]
word_counts[0]


#{name:word_counts(x["title"].apply(list)) for name, x in subgen_gb.iteritems()}



list_of_titles = subgen_gb["title"].apply(list)[1]


type(subgen_counts)
print(subgen_counts)





from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer(max_features=30)
vectWordFreq = vect.fit_transform(data_temp.title.values).toarray()
vectNames = vect.get_feature_names()
vectdf = pd.DataFrame(vectWordFreq,columns = self.vectNames, index=self.songNames)




data2[data2.title == "--"]
