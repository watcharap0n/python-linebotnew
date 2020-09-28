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

with open('config/database_older/firebase.json', encoding='utf8') as json_file:
    data = json.load(json_file)
    config = data['firebase']
    firebase = pyrebase.initialize_app(config)
    pb = pyrebase.initialize_app(config)
    db = pb.database()
    line_bot_api = LineBotApi(data['Channel_access_token'])
    handler = WebhookHandler(data['Channel_secret'])

app = Flask(__name__)

embedding = []
answers = []
xtrain = []
datasets = db.child('transaction_mango').child('datasets').get()
count = 0
for d in datasets.each():
    if d.val():
        txt = ''
        answers.append(d.val()['answers'])
        if d.val()['questions']:
            for i in d.val()['questions']:
                txt = txt + i
            xtrain.append(txt)
            embedding.append(count)
            count += 1

count_vect = CountVectorizer(tokenizer=tokenize)
Xtrain_count = count_vect.fit_transform(xtrain)
tf_transformer = TfidfTransformer(use_idf=False)
tf_transformer.fit(Xtrain_count)
Xtrain_tf = tf_transformer.transform(Xtrain_count)
SVM = svm.SVC(C=1.0, kernel='linear', degree=3,
              gamma='auto', probability=True)
SVM.fit(Xtrain_tf, embedding)
msg = ['หักเงิน']
Xtest_count = count_vect.transform(msg)
Xtest_tf = tf_transformer.transform(Xtest_count)
label = SVM.predict(Xtest_tf)
prop = SVM.predict_proba(Xtest_tf)[0][label]
p = float(prop)
confidence = (0.3565152559 / ((len(embedding) * p) ** 0.5)) ** 2
# print(label)
# print(answers)

idx_answer = []
for a in answers:
    idx = list(a)
    sli = idx[1:]
    idx_answer.append(sli)
print(idx_answer)
