import pandas as pd
import numpy as np
import os
import re
from collections import Counter


#import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords



os.getcwd()


data1 = pd.read_table(r"data/coca-sources.txt", header = 0, skiprows=[1], encoding="ISO-8859-1")
data1.shape
data1.head()

data1.tail()

# Are all the rows of the last column nulls?
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
data1.subgen.value_counts(normalize=True).describe()
# Note min max are not that far apart and the standard deviation is low

data1.subgen.value_counts(normalize=True).describe()["std"]\
/data1.subgen.value_counts(normalize=True).describe()["mean"]
# The ratio between the mean and the standard deviation is low
# This means there is not much relative variation which is good


############################
# Begin Analysis of Titles #
############################

# How many of the sources contain "child"
child_source_mask = data1["source"].str.lower().str.contains("child").fillna(False)
np.nansum(child_source_mask)
np.nansum(child_source_mask)/len(data1["source"])
# 1575 sources which is about 0.7% of the all the sources


child_in_sources_df = data1[child_source_mask]
child_in_sources_df.head(20)

child_in_sources_df["source"].nunique()
child_in_sources_df["source"].nunique()/data1["source"].nunique()
# 49 sources which is about 0.4% of the unique sources


############################
# Start sub genre analysis #
############################

# Look at one row per sub genre
data1.groupby("subgen")["title", col8_name].last()


def count_words2(series_of_titles, numb_counts = 10):
    """
    Finds words with highest counts

    Inputs:
        series_of_titles (pandas Series of str)
        numb_counts (int) = number of words from top of the sorted list
    Output:
        s (list of tuples) = word and number of occurances

    """

    # Combine all titles into 1 string
    all_titles = ""
    for title in series_of_titles.values:
        all_titles = all_titles + " "+str(title)

    # Tokenize list, normalize words by removing punctuations and making lowercase
    tokenized_words = all_titles.split(" ")
    cleaned_titles = [re.sub("\W+", "", str(title).lower()) for title in tokenized_words]
    # Find count per unique token
    counts = Counter(cleaned_titles)
    # Sort and remove stop words
    s = [(k, counts[k]) for k in sorted(counts, key=counts.get, reverse=True) if k not in stopwords.words('english')]

    return(s[:numb_counts])



subgen_gb = data1.groupby("subgen")
# Per subgen...
word_counts2 = {name:count_words2(x) for name, x in subgen_gb["title"]}
nunique_src = {name:x.nunique() for name,x in subgen_gb["source"]}
nunique_genre = {name:x.nunique() for name,x in subgen_gb["genre"]}
avg_wc = {name:x.mean() for name, x in subgen_gb["#words"]}

word_counts2
nunique_src
nunique_genre
avg_wc


#### Word count analysis from 5/12
# Same as word_counts2 above


def count_words(list_of_titles):
    """

    """

    all_titles = ""
    for title in list_of_titles:
        all_titles = all_titles + " "+str(title)
    # Tokenize list, normalize words by removing punctuations and making lowercase
    tokenized_words = all_titles.split(" ")
    cleaned_titles = [re.sub("\W+", "", str(title).lower()) for title in tokenized_words]
    # Find count per unique token
    counts = Counter(cleaned_titles)
    # Sort and remove stop words
    s = [(k, counts[k]) for k in sorted(counts, key=counts.get, reverse=True) if k not in stopwords.words('english')]

    return(s[:10])

list_of_titles1 = data1.groupby("subgen")["title"].apply(list)
word_counts = [count_words(x) for x in list_of_titles1]
word_counts[1]
