# model imports
import numpy as np
import pandas as pd
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer
import pickle

model = pickle.load(open("model.sav", 'rb'))
prep = pickle.load(open("prepped.sav", 'rb'))

# server imports
import os
import requests
from flask import Flask, request

app = Flask(__name__)

# environment variables
os.environ['bot_id'] = '2032c1c3b2d8f0ffa1e7c5b4f9'

@app.route("/messages", methods=['POST'])
def messages():
  data = request.get_json()
  print(data, flush=True)

  # check if message (data) is hate speech and respond
  if data['sender_type'] != 'bot':
    checkHateSpeech(data)

  return 'ok', 200

# tokenize message input
def tokenize(inpt, t):
    tok = TweetTokenizer()
    vec = CountVectorizer(analyzer="word", tokenizer=tok.tokenize, max_features=1010)
    t = vec.fit_transform(t).toarray()
    inpt = vec.transform(inpt).toarray()
    return inpt

# check for hate speech, if it is respond
def checkHateSpeech(data):
  message = data['text']
  d = [message]
  d = pd.DataFrame(d, columns=['col'])
  d = d['col']
  d = tokenize(d, prep)

  #2 - regular, 1 - offensive, 0 - hate
  ans = model.predict(d)
  hateSpeech = True if ans == 0 or ans == 1 else False

  if (hateSpeech):
    response('@' + data['name'] + ' watch your language. Your message has been flagged for foul language.')

# function used to send messages to groupme api
def response(message):
  url = 'https://api.groupme.com/v3/bots/post'
  data = {'bot_id': os.getenv('bot_id'), 'text': message,}
  r = requests.post(url, json=data)
  print(r, flush=True)

if __name__ == "__main__":
  app.run()