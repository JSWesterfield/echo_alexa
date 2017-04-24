from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/")

def get_headlines():
    titles = ["I am in new world","hack the world"]
    titles = '... '.join([i for i in titles])
    return titles  

@ask.intent('HelloIntent')
def hello(firstname):
    speech_text = "Hello %s" % firstname
    return statement(speech_text).simple_card('Hello', speech_text)

@ask.launch
def start_skill():
    print ("answering skill ... ")
    r = requests.get('http://localhost:5000/time/Pratik')
    data = r.json()
    answer = ""
    for each_friends, each_time in data['timing']:
        each_time = each_time.split("-")
        each_time = " to ".join(each_time)
        answer = answer  + " for time "+ each_time + " you can meet " + each_friends + " ... "
    return question(answer)

@ask.intent("YesIntent")
def share_headlines():
    headline_msg = 'The current world news headlines'
    return statement(headline_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'I am not sure why you asked me to run then, but okay... bye'
    return statement(bye_text)
    
if __name__ == '__main__':
    app.run(port=8000,debug=True)