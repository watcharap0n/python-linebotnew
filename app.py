from flask import Flask, request, abort, render_template, jsonify, json, redirect, url_for, session, flash, g
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from attacut import tokenize
import pyrebase
import json
from random import randrange
from numpy import random as np
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError, LineBotApiError)
from linebot.models import *

with open('config/firebase.json', encoding='utf8') as json_file:
    data = json.load(json_file)
    config = data['firebase']
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    line_bot_api = LineBotApi(data['Channel_access_token'])
    handler = WebhookHandler(data['Channel_secret'])

app = Flask(__name__)
app.secret_key = 'watcharaponweeraborirakz'


@app.route('/')
@app.route('/index')
def index():
    return 'index ready'


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        raw_json = request.get_json()
        json_line = json.dumps(raw_json)
        decoded = json.loads(json_line)
        with open('dataline.json', 'w') as dataline:
            json.dump(raw_json, dataline)
        body = request.get_data(as_text=True)
        signature = request.headers['X-Line-Signature']
        _type = decoded['events'][0]['message']['type']
        print(_type)
        print(signature)
        if _type == 'text':
            txt = decoded['events'][0]['message']['text']
            print(txt)
            try:
                handler.handle(body, signature)
            except InvalidSignatureError:
                abort(400)
        else:
            no_event = len(decoded['events'])
            for i in range(no_event):
                event = decoded['events'][i]
                event_handler(event)
    return 'ok'


def event_handler(event):
    rtoken = event['replyToken']
    _type = event['message']['type']
    sk_id = randrange(51626494, 51626533)
    if _type == 'sticker':
        replyObj = StickerSendMessage(package_id=str(11538), sticker_id=str(sk_id))
        line_bot_api.reply_message(rtoken, replyObj)


if __name__ == '__main__':
    app.run(debug=True)
