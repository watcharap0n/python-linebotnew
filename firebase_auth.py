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
import base64
from linebot import (LineBotApi, WebhookHandler)


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

with open('img/file_path.png', 'rb') as image_file:
    encoded_string = base64.b64decode(image_file.read())
    print(encoded_string)



# imgdata = base64.b64decode(encoded_string)
# filename = 'img/sad.png'
# with open(filename, 'wb') as f:
#     f.write(imgdata)

