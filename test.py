import numpy as np
import pandas as pd
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer

import pickle

model = pickle.load(open("model.sav", 'rb'))

d = [["test string"]]

def tokenize(inpt):
    tok = TweetTokenizer()
    vec = CountVectorizer(analyzer="word", tokenizer=tok.tokenize, max_features=1010)
    inpt = vec.fit_transform(inpt).toarray()
    ex = [0 for i in range(0,1010-inpt[0].size)]
    inpt = np.append(inpt, ex)
    
    return inpt

d[0] = tokenize(d[0])

ans = model.predict(d)

#2 - regular, 1 - offensive, 0 - hate
print(ans[0])