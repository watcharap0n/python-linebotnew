import pyrebase
import json
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage, ImageSendMessage
from flask import Flask, request, abort
from linebot import LineBotApi
from datetime import datetime


app = Flask(__name__)



with open('model/config/database_test/firebase.json', encoding='utf8') as json_file:
    data = json.load(json_file)
    config = data['firebase']
    firebase = pyrebase.initialize_app(config)
    pb = pyrebase.initialize_app(config)
    db = firebase.database()
    line_bot_api = LineBotApi(data['Channel_access_token'])
    handler = WebhookHandler(data['Channel_secret'])





if __name__ == '__main__':
    app.run(port=5005, debug=True)