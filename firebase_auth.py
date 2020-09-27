from flask import Flask, request, abort, render_template, jsonify, json, redirect, url_for, session, flash, g
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from attacut import tokenize
import pyrebase
from datetime import datetime, timedelta
import firebase_admin
from firebase_admin import credentials, auth
import json
from random import randrange
from numpy import random
import numpy as np
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError, LineBotApiError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            ImageSendMessage, StickerSendMessage, AudioSendMessage, FlexSendMessage,
                            ImagemapSendMessage,
                            BaseSize, URIImagemapAction, ImagemapArea)
from mangoerp.mangoerp_card import mangoerp

cred = credentials.Certificate('config/authen_firebase.json')
firebase_auth = firebase_admin.initialize_app(cred)

with open('config/database_test/firebase.json', encoding='utf8') as json_file:
    data = json.load(json_file)
    config = data['firebase']
    firebase = pyrebase.initialize_app(config)
    pb = pyrebase.initialize_app(config)
    db = pb.database()
    line_bot_api = LineBotApi(data['Channel_access_token'])
    handler = WebhookHandler(data['Channel_secret'])

app = Flask(__name__)

@app.route('/api/signup')
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or password is None:
        return {'message': 'Error missing email or password'},400
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        day = datetime.today().day
        month = datetime.today().month
        second = datetime.today().second
        minute = datetime.today().minute
        hour = datetime.today().hour
        year = datetime.today().year
        data = {'email': user.email, 'userToken': user.uid,
                'Datetime': {'day': day, 'month': month, 'year': year, 'hour': hour, 'minute': minute, 'second': second}}
        db.child('id').push(data)
        return {'message': f'Successfully created user {user.email}'}, 200
    except:
        return {'message': 'Error creating user'}, 400


if __name__ == '__main__':
    app.run(debug=True, port=5003)
