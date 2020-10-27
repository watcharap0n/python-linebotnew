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


# class News():
#     @staticmethod
#     def new_common():
#         r = requests.get("https://www.thairath.co.th/news/local")
#         soup = BeautifulSoup(r.content, "html.parser")
#         newHit = soup.find('div', {'class': 'css-1y5neuu edxt67m0'})
#         txt = newHit.text
#         txt = txt.split(' '' ')
#         str_txt = ', \n '
#         str_txt = str_txt.join(txt)
#         return str_txt
#
#     @staticmethod
#     def new_sport():
#         r = requests.get("https://www.thairath.co.th/sport")
#         soup = BeautifulSoup(r.content, "html.parser")
#         score = soup.find('div', {'class': 'css-w104ue e18p2jld54'})
#         t = ''
#         for i in score:
#             t = t + '\n' + i.text
#         return t

# r = requests.get("https://www.thairath.co.th/entertain")
# soup = BeautifulSoup(r.content, "html.parser")
# newother = soup.find('div', {'class': 'col-md-8'})
# txt = ''
# lst = []
# for d in newother:
#     txt = txt + '\n' + d.text
# print(txt)






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

ref = db.child('chat-flex').get()
count = 1
lst = []
stats = []
key = []
for i in ref.each():
    key.append(i.key())
    msg = i.val()['message']
    stats.append(msg)
    user = dict(i.val())
    user.update({'index': count})
    lst.append(user)
    # print(user)
    count += 1

# key = key.


# db.child('chat-flex').child(remove).remove()

# db.child('chat-flex').child('-MKQ4L43DDgj01wsQu31').remove()


# ERPSoftware = [s for s in stats if '@ERPSoftware' in s]
# Business = [s for s in stats if '@Business' in s]
# NewFeature = [s for s in stats if '@NewFeature' in s]
# Optional = [s for s in stats if '@Optional' in s]
# rent = [s for s in stats if '@Product' in s]
#
#
# ERPSoftware = len(ERPSoftware)
# Business = len(Business)
# NewFeature = len(NewFeature)
# Optional = len(Optional)
# rent = len(rent)
#
# key_erp = {'ERPSoftware': ERPSoftware, 'Business': Business,
#            'NewFeature': NewFeature, 'Optional': Optional, 'เช่าสุดคุ้ม': rent}
# value_erp = ERPSoftware, Business, NewFeature, Optional, rent
# value_erp = list(value_erp)
# key_erp = max(key_erp)
# value_erp = max(value_erp)
#
#
# data = {
#     'user': lst,
#     'erpsoftware': str(ERPSoftware),
#     'business': str(Business),
#     'newfeature': str(NewFeature),
#     'optional': str(Optional),
#     'key_erp': key_erp,
#     'value_erp': str(value_erp)
# }


# date_time = []
# ref = db.child('chat-flex').get()
# for e in ref.each():
#     # index = e['index']
#     profile = e.val()['profile']
#     erp = e.val()['message']
#     reply = e.val()['reply']
#     year = e.val()['year']
#     month = e.val()['month']
#     day = e.val()['day']
#     dbTime = {'profile': profile, 'question': erp, 'reply': reply, 'year': year, 'month': month, 'day': day}
#     date_time.append(dbTime)
# dbDatetime = date_time
# data = pd.DataFrame(dbDatetime)
# datatoexcel = pd.ExcelWriter('static/excel/Stats.xlsx', engine='xlsxwriter')
# data.to_excel(datatoexcel, sheet_name='Sheet1')
# datatoexcel.save()


# for s in stats:
#     if '@ERPSoftware' in s:
#         print(s)



# first = input('firstname: ')
# last = ''
# tel = ''
# email = input('email: ')
#
# if last or tel:
#     print('OK')
#     print(first)
#     print(tel)
#     print(email)
# else:
#     print('NO')
#     print(first)
#     print(tel)
#     print(email)
line_bot_api.push_message('U29abee37b5e3255aa9d24e67099be87b', TextSendMessage(text=f'fwjif'))