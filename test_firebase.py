import firebase_admin
import pyrebase
import json, webbrowser
from linebot import LineBotApi, WebhookHandler
import pandas as pd
from linebot.models import TextSendMessage, ImageSendMessage
from attacut import tokenize
from flask import Flask, request, abort, jsonify
from linebot import LineBotApi
from firebase_admin import credentials, auth
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import xlsxwriter

app = Flask(__name__)

cred = credentials.Certificate('model/config/database_test/authen_firebase.json')
firebase_auth = firebase_admin.initialize_app(cred)


with open('model/config/database_new/firebase.json', encoding='utf8') as json_file:
    data = json.load(json_file)
    config = data['firebase']
    firebase = pyrebase.initialize_app(config)
    pb = pyrebase.initialize_app(config)
    db = firebase.database()
    line_bot_api = LineBotApi(data['Channel_access_token'])
    handler = WebhookHandler(data['Channel_secret'])

group = ['CB010', 'CC010', 'CG010', 'CI010', 'CJ010', 'CM010', 'CF010',
         'CP010', 'CE010', 'CH010', 'CK010', 'CN010', 'CD010', 'RC010',
         'RA010', 'RB010']

ref = db.child('LineLiff').get()
lst = []
for i in ref.each()[1:]:
    if 'CC010' in i.val()['tag']:
        lst.append(i.val())


for l in range(0, len(lst)):
    print(l)
# for i in ref.each()[1:]:
#     print(i.val()['Tag'])
#     for t in i.val()['Tag']:
#         print(t)
# def temperature():
#     r = requests.get("https://weather.com/weather/today/l/13.72,100.40?par=google&temp=c")
#     soup = BeautifulSoup(r.content, "html.parser")
#     temp = soup.find('span', {'data-testid': 'TemperatureValue'})
#     feelLike = soup.find('div', {'data-testid': 'FeelsLikeSection'})
#     HighLow = soup.find('div', {'data-testid': 'WeatherDetailsLabel'})
#     valueTemp = soup.find('div', {'data-testid': 'wxData'})
#     humility = soup.find('span', {'data-testid': 'PercentageValue'})
#     x = 'Temperature : {}\n{}\n{}  {}\nHumidity  {}'.format(temp.text, feelLike.text,
#                                                HighLow.text, valueTemp.text,
#                                               humility.text)
#     return x




# @app.route('/stats')
# def stats():
#     if not g.user:
#         return redirect(url_for('welcome'))
#     ref = db2.child('chat-flex').get()
#     count = 1
#     lst = []
#     stats = []
#     for i in ref.each():
#         k = i.key()
#         msg = i.val()['reply']
#         stats.append(msg)
#         user = dict(i.val())
#         user.update({'index': count, 'key': k})
#         lst.append(user)
#         count += 1
#     Rental = [s for s in stats if 'Rental' in s]
#     CSM = [s for s in stats if 'Customer Service Management' in s]
#     QCM = [s for s in stats if 'Quality Control Management' in s]
#     Maintenance = [s for s in stats if 'Maintenance' in s]
#     MRP = [s for s in stats if 'MRP' in s]
#     Rent = [s for s in stats if 'เช่าสุดคุ้ม' in s]
#     PJ = [s for s in stats if 'Project Planning' in s]
#     Con = [s for s in stats if 'Construction' in s]
#     Real = [s for s in stats if 'Real Estate' in s]
#     Rental = len(Rental)
#     CSM = len(CSM)
#     QCM = len(QCM)
#     Maintenance = len(Maintenance)
#     MRP = len(MRP)
#     Rent = len(Rent)
#     PJ = len(PJ)
#     Con = len(Con)
#     Real = len(Real)
#     key_erp = {'Rental': Rental, 'CSM': CSM,
#                'QCM': QCM, 'Maintenance': Maintenance, 'MRP': MRP, 'เช่าสุดคุ้ม': Rent,
#                'Project Planning': PJ, 'Construction': Con, 'Real Estate': Real}
#     value_erp = Rental, CSM, QCM, Maintenance, MRP, Rent, PJ, Con, Real
#     value_erp = list(value_erp)
#     key_erp = max(key_erp)
#     value_erp = max(value_erp)
#
#     data = {
#         'user': lst,
#         'rental': Rental,
#         'csm': CSM,
#         'qcm': QCM,
#         'main': Maintenance,
#         'mrp': MRP,
#         'rent': Rent,
#         'pj': PJ,
#         'con': Con,
#         'real': Real,
#         'key_erp': key_erp,
#         'value_erp': str(value_erp)
#     }
#     return render_template('/customers_new/stats.html', data=data)
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

# ref = db.child('chat-flex').get()
# count = 1
# lst = []
# stats = []
# key = []
# for i in ref.each():
#     key.append(i.key())
#     msg = i.val()['message']
#     stats.append(msg)
#     user = dict(i.val())
#     user.update({'index': count})
#     lst.append(user)
#     # print(user)
#     count += 1

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
# line_bot_api.push_message('U29abee37b5e3255aa9d24e67099be87b', TextSendMessage(text=f'fwjif'))


# ref = db.child('chatbot_transactions').get()
#
# d = []
# for i in ref.each():
#     day = i.val()['day']
#     month = i.val()['month']
#     year = i.val()['year']
#     name = str(day) + '-' + str(month) + '-' + str(year)
#     d.append(name)
#
# stf = datetime.today()
# print(type(stf.strftime('%B')))
#
# t1 = [e for e in d if '24-10-2020' in e]
# t2 = [e for e in d if '26-10-2020' in e]
# t3 = [e for e in d if '27-10-2020' in e]
# t4 = [e for e in d if '28-10-2020' in e]




# ref = db.child('LineLiff').get()
# lst = []
# for o in ref.each():
#     e = o.key()
#     py = db.child('LineLiff').child(e).get()
#     day = py.val()['day']
#     month = py.val()['month']
#     year = py.val()['year']
#     hour = py.val()['hour']
#     minn = py.val()['min']
#     sec = py.val()['sec']
#     event = py.val()['event']
#     comment = event['comment']
#     company = event['company']
#     displayName = event['displayName']
#     email = event['email']
#     name = event['firstname']
#     picture = event['picture']
#     product = event['product']
#     tel = event['tel']
#     token = event['token']
#     group = {'Name': name, 'Product': product, 'Company': company,
#            'Tel': tel, 'Email': email, 'EmailLiff': token, 'Message': comment,
#            'Profile': displayName, 'Date': (f'{day}-{month}-{year}'), 'Time': (f'{hour}:{minn}:{sec}'),
#            'Picture': picture}
    # db.child('RestCustomer').push(group)
    # print(group)

#
# rest = db.child('RestCustomer').child('-ML61O1X2uVFWg62dyeO').get()
# for i in rest.each():
#     print(i.val())
    # profile = i.val()['Profile']
    # cTime = i.val()['Time']
    # cDate = i.val()['Date']
    # company = i.val()['Company']
    # email = i.val()['Email']
    # pEmail = i.val()['EmailLiff']
    # message = i.val()['Message']
    # picture = i.val()['Picture']
    # product = i.val()['Product']
    # tel = i.val()['Tel']
    # name = i.val()['Name']
    # group = {'Name': name, 'Product': product, 'Company': company, 'Tel': tel, 'Email': email,
    #          'EmailLiff': pEmail, 'Message': message, 'Profile': profile, 'Date': cDate, 'Time': cTime,
    #          'Picture': picture}
    # print(group)


