import numpy as np
import pandas as pd
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer

import pickle

model = pickle.load(open("model.sav", 'rb'))
prep = pickle.load(open("prepped.sav", 'rb'))

d = ['test string']
d = pd.DataFrame(d, columns=['col'])
d = d['col']

def tokenize(inpt, t):
    tok = TweetTokenizer()
    vec = CountVectorizer(analyzer="word", tokenizer=tok.tokenize, max_features=1010)
    t = vec.fit_transform(t)
    inpt = vec.transform(inpt).toarray()
    
    return inpt

d = tokenize(d, prep)


ans = model.predict(d)

#2 - regular, 1 - offensive, 0 - hate
print(ans[0])