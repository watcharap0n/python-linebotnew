import pyrebase
import json, webbrowser, lxml
from linebot import LineBotApi, WebhookHandler
import pandas as pd
from linebot.models import TextSendMessage, ImageSendMessage
from flask import Flask, request, abort
from linebot import LineBotApi
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import xlsxwriter

app = Flask(__name__)



with open('model/config/database_new/firebase.json', encoding='utf8') as json_file:
    data = json.load(json_file)
    config = data['firebase']
    firebase = pyrebase.initialize_app(config)
    pb = pyrebase.initialize_app(config)
    db = firebase.database()
    line_bot_api = LineBotApi(data['Channel_access_token'])
    handler = WebhookHandler(data['Channel_secret'])


def temperature():
    r = requests.get("https://weather.com/weather/today/l/13.72,100.40?par=google&temp=c")
    soup = BeautifulSoup(r.content, "html.parser")
    temp = soup.find('span', {'data-testid': 'TemperatureValue'})
    feelLike = soup.find('div', {'data-testid': 'FeelsLikeSection'})
    HighLow = soup.find('div', {'data-testid': 'WeatherDetailsLabel'})
    valueTemp = soup.find('div', {'data-testid': 'wxData'})
    humility = soup.find('span', {'data-testid': 'PercentageValue'})
    x = 'Temperature : {}\n{}\n{}  {}\nHumidity  {}'.format(temp.text, feelLike.text,
                                               HighLow.text, valueTemp.text,
                                              humility.text)
    return x


class News():
    @staticmethod
    def new_common():
        r = requests.get("https://www.thairath.co.th/news/local")
        soup = BeautifulSoup(r.content, "html.parser")
        newHit = soup.find('div', {'class': 'css-1y5neuu edxt67m0'})
        txt = newHit.text
        txt = txt.split(' '' ')
        str_txt = ', \n '
        str_txt = str_txt.join(txt)
        return str_txt

    @staticmethod
    def new_sport():
        r = requests.get("https://www.thairath.co.th/sport")
        soup = BeautifulSoup(r.content, "html.parser")
        score = soup.find('div', {'class': 'css-w104ue e18p2jld54'})
        t = ''
        for i in score:
            t = t + '\n' + i.text
        return t

r = requests.get("https://www.thairath.co.th/entertain")
soup = BeautifulSoup(r.content, "html.parser")
newother = soup.find('div', {'class': 'col-md-8'})
txt = ''
lst = []
for d in newother:
    txt = txt + '\n' + d.text
print(txt)






# test = 'ค้นหา รถ'
# x = test.split('ค้นหา')
# t = ''
# car = t.join(x)
# print(car)
# if car == ' รถ':
#     print(car)
# else:
#     print('No')



# for i in range(len(data)):
#     print(data[i].text)





