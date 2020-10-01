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

# cred = credentials.Certificate('config/authen_firebase.json')
# firebase_auth = firebase_admin.initialize_app(cred)

with open('config/database_test/firebase.json', encoding='utf8') as json_file:
    data = json.load(json_file)
    config = data['firebase']
    firebase = pyrebase.initialize_app(config)
    pb = pyrebase.initialize_app(config)
    db = pb.database()
    line_bot_api = LineBotApi(data['Channel_access_token'])
    handler = WebhookHandler(data['Channel_secret'])

app = Flask(__name__)
#
#
# quest = ['ขื่อนายนางสาวเบอร์ติดต่อ อีเมลล์ อีเมล บริษัทคอนแทคลูกค้า']
# answer = ['โอเคจ้าเดี๋ยวทำการติดต่อกลับนะ']
#
#
#
# count_vect = CountVectorizer(tokenizer=tokenize)
# Xtrain_count = count_vect.fit_transform(quest)
# tf_transformer = TfidfTransformer(use_idf=False)
# tf_transformer.fit(Xtrain_count)
# Xtrain_tf = tf_transformer.transform(Xtrain_count)
# SVM = svm.SVC(C=1.0, kernel='linear', degree=3,
#               gamma='auto', probability=True)
# SVM.fit(Xtrain_tf, answer)
# msg = ['']
# Xtest_count = count_vect.transform(msg)
# Xtest_tf = tf_transformer.transform(Xtest_count)
# label = SVM.predict(Xtest_tf)
# print(label)

ref = db.child('customer_email').get()

print(ref.val())

