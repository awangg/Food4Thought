import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords 
from nltk.tokenize import WordPunctTokenizer
import warnings
import string
import nltk
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('stopwords')



df = pd.read_csv('data/out.csv')
df_business = pd.read_csv('data/places.csv')
print(df.head())

#Select only stars and text
#replaced 'business_id', 'user_id', 'stars', 'text' with 
bus_data = df[['gPlusUserId', 'reviewerName', 'rating', 'reviewText']]
stop = []
for word in stopwords.words('english'):
    s = [char for char in word if char not in string.punctuation]
    stop.append(''.join(s))

print(stopwords.words('english'))

def text_process(mess):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    # Check characters to see if they are in punctuation
    if(isinstance(mess, float)):
        return " "
    else:
        nopunc = [char for char in mess if char not in string.punctuation]
    # Join the characters again to form the string.
        nopunc = ''.join(nopunc)
        
        # Now just remove any stopwords
        return " ".join([word for word in nopunc.split() if word.lower() not in stop])

bus_data['reviewText'] = bus_data['reviewText'].apply(text_process)

