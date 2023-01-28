import os
import requests

from flask import Flask, request
app = Flask(__name__)

# environment variables
os.environ['bot_id'] = '2032c1c3b2d8f0ffa1e7c5b4f9'

@app.route("/messages", methods=['POST', 'GET'])
def messages():
  data = request.get_json()
  print(data, flush=True)

  # check if message (data) is hate speech and respond
  if data['sender_type'] != 'bot':
    checkHateSpeech(data)

  return 'ok', 200

# check for hate speech, if it is respond
def checkHateSpeech(data):
  hateSpeech = True #placeholder, just marking everything as hate speech

  if (hateSpeech):
    response('@' + data['name'] + ' watch your language. Your message has been flagged for hate speech.')

# function used to send messages to groupme api
def response(message):
  url = 'https://api.groupme.com/v3/bots/post'
  data = {'bot_id': os.getenv('bot_id'), 'text': message,}
  r = requests.post(url, json=data)
  print(r, flush=True)

if __name__ == "__main__":
  app.run()