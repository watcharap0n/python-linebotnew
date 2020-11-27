# from flask import Flask, request, abort, render_template, jsonify, json, redirect, url_for, session, flash, g, \
#     make_response, send_from_directory
# import json, uuid, time, os, warnings, pyrebase, firebase_admin, base64, requests, pandas as pd
# from flask_bootstrap import Bootstrap
# from datetime import timedelta
# from random import randrange
# from numpy import random
# from bs4 import BeautifulSoup
# from model_image import *
# from PIL import Image
# from mangoerp.myClass import *
# from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
# from sklearn import svm
# from attacut import tokenize
# from datetime import datetime
# from firebase_admin import credentials, auth
# from mangoerp.mangoerp_card import *
# from mangoerp.flex_message import *
# from linebot import LineBotApi, WebhookHandler
# from linebot.exceptions import (InvalidSignatureError, LineBotApiError)
# from linebot.models import (MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, QuickReply, QuickReplyButton,
#                             StickerSendMessage, RichMenu, RichMenuArea, RichMenuBounds, RichMenuSize, CameraAction)
#
# warnings.simplefilter('error', Image.DecompressionBombWarning)
#
# app = Flask(__name__)
# bootstrap = Bootstrap(app)
# app.secret_key = 'watcharaponweeraborirakz'
#
# cred = credentials.Certificate('model/config/database_test/authen_firebase.json')
# firebase_auth = firebase_admin.initialize_app(cred)
#
#
# def database_test():
#     with open('model/config/database_test/firebase.json', encoding='utf8') as json_file:
#         data = json.load(json_file)
#         config = data['firebase']
#         firebase = pyrebase.initialize_app(config)
#         pb = pyrebase.initialize_app(config)
#         db = firebase.database()
#         line_bot_api = LineBotApi(data['Channel_access_token'])
#         handler = WebhookHandler(data['Channel_secret'])
#     return db, line_bot_api, handler, pb
#
#
# def database_new():
#     with open('model/config/database_new/firebase.json', encoding='utf8') as json_file:
#         data = json.load(json_file)
#         config = data['firebase']
#         firebase = pyrebase.initialize_app(config)
#         db = firebase.database()
#         line_bot_api = LineBotApi(data['Channel_access_token'])
#         handler = WebhookHandler(data['Channel_secret'])
#     return db, line_bot_api, handler
#
#
# def database_older():
#     with open('model/config/database_older/firebase.json', encoding='utf8') as json_file:
#         data = json.load(json_file)
#         config = data['firebase']
#         firebase = pyrebase.initialize_app(config)
#         db = firebase.database()
#         line_bot_api = LineBotApi(data['Channel_access_token'])
#         handler = WebhookHandler(data['Channel_secret'])
#     return db, line_bot_api, handler
#
#
# data_test = database_test()
# db1 = data_test[0]
# line_bot_api1 = data_test[1]
# handler1 = data_test[2]
# pb = data_test[3]
#
# data_new = database_new()
# db2 = data_new[0]
# line_bot_api2 = data_new[1]
# handler2 = data_new[2]
#
# data_older = database_older()
# db3 = data_older[0]
# line_bot_api3 = data_older[1]
# handler3 = data_older[2]
#
#
# @app.before_request
# def before_request():
#     try:
#         if 'user_id' in session:
#             user = session['user_id']['displayName']
#             g.user = user
#         else:
#             g.user = None
#     except:
#         print("error login")
#
#
# @app.before_request
# def make_session_permanent():
#     session.permanent = True
#     app.permanent_session_lifetime = timedelta(minutes=60)
#
#
# @app.route('/log', methods=['GET', 'POST'])
# def log():
#     return render_template('customers_new/log.html')
#
#
# @app.route('/api/demorequest', methods=['GET', 'POST'])
# def customerDemo():
#     if request.method == 'POST':
#         try:
#             to = TimeDate()
#             event_email = request.get_json()
#             event_email = dict(event_email)
#             groupBy = {'event': event_email, 'Date': f'{to.day}-{to.month}-{to.year}',
#                        'Time': f'{to.hour}:{to.minute}:{to.second}', 'tag': ['']}
#             print(groupBy)
#             db2.child('requestDemo').push(groupBy)
#             db2.child('feature_selection').push(groupBy)
#             response = app.response_class(
#                 response=json.dumps(event_email),
#                 mimetype='application/json'
#             )
#             return response
#         except:
#             return jsonify({'error Sending: Please try again'}, 400)
#
#
# @app.route('/api/contract', methods=['GET', 'POST'])
# def customerContract():
#     if request.method == 'POST':
#         try:
#             to = TimeDate
#             event_email = request.get_json()
#             event_email = dict(event_email)
#             groupBy = {'event': event_email, 'Date': f'{to.day}-{to.month}-{to.year}',
#                        'Time': f'{to.hour}:{to.minute}:{to.second}', 'tag': ['']}
#             print(groupBy)
#             db2.child('requestcontract').push(groupBy)
#             db2.child('feature_selectionBycontract').push(groupBy)
#             response = app.response_class(
#                 response=json.dumps(event_email),
#                 mimetype='application/json'
#             )
#             return response
#         except:
#             return jsonify({'error Sending: Please try again'}, 400)
#
#
# def sessionCustomer(user, password):
#     getLogin = pb.auth().sign_in_with_email_and_password(user, password)
#     with open('log_LoginSession', 'w') as logLogin:
#         json.dump(getLogin, logLogin)
#     session['user_id'] = getLogin
#
#
# @app.route('/lg/<string:customer>', methods=['GET', 'POST'])
# def login(customer):
#     user = None
#     newCustomer = {'customer': 'new'}
#     trainCustomer = {'customer': 'old'}
#     customers = [newCustomer, trainCustomer]
#     if request.method == 'GET':
#         for i in customers:
#             if i['customer'] == customer:
#                 user = i['customer']
#                 break
#         data = {
#             'customer': user
#         }
#         return render_template('main/login.html', data=data)
#     if request.method == 'POST':
#         error = 'Invalid credentials. Please try again.'
#         session.pop('user_id', None)
#         user = request.form['username']
#         password = request.form['password']
#         if customer == 'new':
#             try:
#                 sessionCustomer(user, password)
#                 flash('You were successfully logged in')
#                 return redirect(url_for('new_chart'))
#             except:
#                 data = {
#                     'user': user,
#                     'error': error
#                 }
#                 return render_template('main/login.html', data=data)
#         elif customer == 'old':
#             try:
#                 sessionCustomer(user, password)
#                 flash('You were successfully logged in')
#                 return redirect(url_for('index_customer'))
#             except:
#                 data = {
#                     'user': user,
#                     'error': error
#                 }
#                 return render_template('main/login.html', data=data)
#
#
# @app.route('/logout')
# def logout():
#     session.clear()
#     print(session)
#     return redirect(url_for('welcome'))
#
#
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'GET':
#         return render_template('main/signup.html')
#     elif request.method == 'POST':
#         error = 'Please fill in all information.'
#         confirm_error = 'Passwords do not match.'
#         userId = request.form['userId']
#         position = request.form['staff']
#         first_name = request.form['firstname']
#         last_name = request.form['lastname']
#         email = request.form['email']
#         password = request.form['password']
#         confirm_pwd = request.form['confirmpwd']
#         if password != confirm_pwd:
#             return render_template('main/signup.html', error=confirm_error)
#         if email is None or password is None or first_name is None or last_name is None:
#             return render_template('main/signup.html', error=error)
#         try:
#             user = auth.create_user(email=email, password=password, display_name=userId)
#             to = TimeDate()
#             day = to.day
#             month = to.month
#             second = to.second
#             minute = to.minute
#             hour = to.hour
#             year = to.year
#             data = {'firstname': first_name, 'lastname': last_name, 'email': user.email, 'userToken': user.uid,
#                     'userId': user.display_name, 'position': position, 'Datetime':
#                         {'day': day, 'month': month,'year': year, 'hour': hour, 'minute': minute, 'second': second}}
#             db1.child('id').push(data)
#             return redirect(url_for('welcome'))
#         except:
#             return render_template('main/signup.html', error=error)
#
#
# @app.route('/setting')
# def settingPage():
#     if not g.user:
#         return redirect(url_for('welcome'))
#     return render_template('main/setting.html')
#
#
# @app.route('/forgot', methods=['GET', 'POST'])
# def forgot():
#     if request.method == 'POST':
#         forgot = request.form['email']
#         try:
#             pb.auth().send_password_reset_email(forgot)
#             return render_template('main/forgot.html', error='Please check your email verify reset password.')
#         except:
#             return render_template('main/forgot.html', error='error')
#     return render_template('main/forgot.html')
#
#
# @app.route('/')
# @app.route('/welcome')
# def welcome():
#     return render_template('main/welcome.html')
#
#
# @app.route('/training/<string:site>', methods=['GET', 'POST'])
# def trianing(site):
#     if request.method == 'GET':
#         if request.path == '/training/event':
#             lst = []
#             news = {'news': ['รับข้อมูลข่าวสาร', 'ไม่รับข้อมูลข่าวสาร']}
#             lst.append(news)
#             return render_template('customers_old/event.html', lst=lst)
#
#
# @app.route('/mango/<string:site>', methods=['GET', 'POST'])
# def line_liff(site):
#     if request.path == '/mango/construction':
#         print(site)
#         x = 'Construction'
#         page_data = get_link(x)
#         Insert = db2.child('chat-flex').push(page_data)
#         print('show: ', Insert)
#         lst = []
#         product = {'product': ['RealEstate', 'Project Planning', 'CSM', 'QCM', 'Maintenance', 'Rental', 'MRP']}
#         lst.append(product)
#         return render_template('customers_new/event/construction.html', lst=lst)
#     elif request.path == '/mango/planing':
#         print(site)
#         x = 'Project Planning'
#         page_data = get_link(x)
#         Insert = db2.child('chat-flex').push(page_data)
#         print('show: ', Insert)
#         lst = []
#         product = {'product': ['Construction', 'RealEstate', 'CSM', 'QCM', 'Maintenance', 'Rental', 'MRP']}
#         lst.append(product)
#         return render_template('customers_new/event/planing.html', lst=lst)
#     elif request.path == '/mango/reales':
#         print(site)
#         x = 'Real Estate'
#         page_data = get_link(x)
#         Insert = db2.child('chat-flex').push(page_data)
#         print('show: ', Insert)
#         lst = []
#         product = {'product': ['Construction', 'Project Planning', 'CSM', 'QCM', 'Maintenance', 'Rental', 'MRP']}
#         lst.append(product)
#         return render_template('customers_new/event/reales.html', lst=lst)
#     elif request.path == '/mango/rent':
#         print(site)
#         x = 'เช่าสุดคุ้ม'
#         page_data = get_link(x)
#         Insert = db2.child('chat-flex').push(page_data)
#         print('show: ', Insert)
#         lst = []
#         product = {'product': ['เช่าสุดคุ้ม', "ลดแรงส่งท้ายปี", "แบ่งชำระ เบา เบา"]}
#         lst.append(product)
#         return render_template('customers_new/event/rent.html', lst=lst)
#     elif request.path == '/mango/anywhere':
#         print('anywhere')
#         lst = []
#         product = {'product': ['Construction', 'RealEstate', 'Project Planning', 'Other']}
#         lst.append(product)
#         return render_template('customers_new/event/quote.html', lst=lst)
#     elif request.path == '/mango/powerbi':
#         print(site)
#         lst = []
#         product = {'product': 'Power BI'}
#         lst.append(product)
#         return render_template('customers_new/event/powerbi.html', lst=lst)
#
#
# @app.route('/trainLetme', methods=['GET', 'POST'])
# def trainLetme():
#     if request.method == 'POST':
#         event = request.form.to_dict()
#         print(event)
#         to = TimeDate()
#         insert = {'channel': 'LINE', 'tag': [''], 'day': to.day, 'month': to.month,
#                   'year': to.year, 'hour': to.hour, 'min': to.minute, 'sec': to.second, 'event': event}
#         db3.child('trainCustomer').push(insert)
#         return make_response(event)
#
#
# @app.route('/letme', methods=['GET', 'POST'])
# def letme():
#     if request.method == 'POST':
#         event = request.form.to_dict()
#         to = TimeDate()
#         p = {'channel': 'LINE', 'tag': [''], 'day': to.day, 'month': to.month, 'year': to.year, 'hour': to.hour,
#              'min': to.minute, 'sec': to.second,
#              'event': event}
#         print(event)
#         with open('lineliff.json', 'w') as lineliff:
#             json.dump(event, lineliff)
#         firstname = event['firstname']
#         email = event['email']
#         company = event['company']
#         tel = event['tel']
#         product = event['product']
#         userId = event['userId']
#         picture = event['picture']
#         displayName = event['displayName']
#         comment = event['comment']
#         print(picture)
#         if email and tel:
#             flex_profile = flex_other(picture, displayName, firstname, email, company, tel, product, comment)
#             line_bot_api2.push_message(userId, flex_profile)
#             line_bot_api2.push_message(userId, TextSendMessage(
#                 text='ขอบคุณลูกค้ามากค่ะ ทางเราจะติดต่อกลับให้เร็วที่สุดค่ะ\nขอบคุณค่ะ'))
#             db2.child('LineLiff').push(p)
#         else:
#             line_bot_api2.push_message(userId, TextSendMessage(
#                 text='เนื่องจากคุณลูกค้าทำการกรอกข้อมูลไม่ครบถ้วน โปรดกรอกข้อมูลให้ครบถ้วยด้วยค่ะ\n\nขอบคุณค่ะ'))
#         return make_response(event)
#
#
# @app.route('/paint')
# def paint():
#     return render_template('main/painting.html')
#
#
# @app.route('/event/<string:event>', methods=['GET', 'POST'])
# def event(event):
#     if request.method == 'GET':
#         if event == 'event':
#             print('event')
#             lst = []
#             product = {'product': ['Construction', 'RealEstate', 'Project Planning', 'Other']}
#             lst.append(product)
#             return render_template('customers_new/event/event.html', lst=lst)
#     elif request.method == 'POST':
#         if event == 'event':
#             r = request.form.to_dict()
#             print(r)
#             to = TimeDate()
#             Inserted = {'channel': 'event Impact', 'tag': [''], 'day': to.day, 'month': to.month, 'year': to.year,
#                         'hour': to.hour, 'min': to.minute, 'sec': to.second,
#                         'event': r}
#             print(Inserted)
#             db2.child('LineLiff').push(Inserted)
#             firstname = r['firstname']
#             email = r['email']
#             company = r['company']
#             tel = r['tel']
#             userId = r['userId']
#             picture = r['picture']
#             displayName = r['displayName']
#             comment = r['comment']
#             product = r['product']
#             flex_profile = flex_pF(picture, displayName, firstname, email, company, tel, comment)
#             line_bot_api2.push_message(userId, flex_profile)
#             line_bot_api2.push_message(userId, TextSendMessage(
#                 text='ขอบคุณลูกค้ามากค่ะ 😁'))
#             return make_response(r)
#     return render_template('customers_new/event/event.html')
#
#
# @app.route('/saveimage', methods=['POST'])
# def saveimage():
#     if request.method == 'POST':
#         event = request.form.to_dict()
#         dir_name = 'static/img_paint'
#         img_name = uuid.uuid4().hex
#         if not os.path.exists(dir_name):
#             os.makedirs(dir_name)
#         with open(os.path.join(dir_name, '{}.jpg'.format(img_name)), 'wb') as img:
#             img.write(base64.b64decode(event['image'].split(",")[1]))
#         original = Image.open(os.path.join(dir_name, '{}.jpg'.format(img_name)))
#         if (original.format != 'JPEG'):
#             return make_response('Unsupported image type.', 400)
#         original.thumbnail((240, 240), Image.ANTIALIAS)
#         original.save(os.path.join(dir_name, '{}_240.jpg'.format(img_name)), 'JPEG')
#         return make_response(img_name, 200)
#
#
# @app.route('/admin_index')
# def index():
#     return render_template('main/index.html')
#
#
# @app.route('/index_new_customer')
# def index_newcustomer():
#     print(g.user)
#     if not g.user:
#         return redirect(url_for('welcome'))
#     return render_template('customers_new/index.html')
#
#
# @app.route('/index_customer')
# def index_customer():
#     print(g.user)
#     if not g.user:
#         return redirect(url_for('welcome'))
#     return render_template('customers_old/index.html')
#
#
# @app.route('/intent/<string:id>', methods=['GET', 'POST'])
# def intent(id):
#     data = {'id': id}
#     return render_template('main/intent.html', data=data)
#
#
# @app.route('/new_intent/<string:id>', methods=['GET', 'POST'])
# def new_intent(id):
#     if not g.user:
#         return redirect(url_for('welcome'))
#     data = {'id': id}
#     return render_template('customers_new/intent.html', data=data)
#
#
# @app.route('/c_intent/<string:id>', methods=['GET', 'POST'])
# def old_intent(id):
#     if not g.user:
#         return redirect(url_for('welcome'))
#     data = {'id': id}
#     return render_template('customers_old/intent.html', data=data)
#
#
# @app.route('/chart', methods=['GET', 'POST'])
# def chart():
#     if not g.user:
#         return redirect(url_for('welcome'))
#     if request.method == 'GET':
#         tag = ['CB010', 'CC010', 'CG010', 'CI010', 'CJ010', 'CM010',
#                'CF010', 'CP010', 'CE010', 'CH010', 'CK010', 'CN010', 'CD010',
#                'RC010', 'RA010', 'RB010']
#         fire = FirebaseCustomer(db=db3)
#         lst = fire.importCustomer()
#         amountImport = len(lst)
#         data = {
#             'tags': tag,
#             'import': lst,
#             'amountImport': amountImport
#         }
#         return render_template('customers_old/charts.html', data=data)
#
#
# @app.route('/new_chart', methods=['GET', 'POST'])
# def new_chart():
#     if not g.user:
#         return redirect(url_for('welcome'))
#     if request.method == 'GET':
#         tag = ['CB010', 'CC010', 'CG010', 'CI010', 'CJ010', 'CM010',
#                'CF010', 'CP010', 'CE010', 'CH010', 'CK010', 'CN010', 'CD010',
#                'RC010', 'RA010', 'RB010']
#         fire = FirebaseNewCustomer(db=db2)
#         lst = fire.restCustomer()
#         est = fire.liffCustomer()
#         _id = len(lst)
#         rMsg = len(est)
#         demo = fire.demoCustomer()
#         data = {
#             'tag': tag,
#             'users': lst,
#             'est': est,
#             'msg': _id,
#             'rmsg': rMsg,
#             'demo': str(demo[1])
#         }
#         return render_template('customers_new/charts.html', data=data, amount=len)
#     elif request.method == 'POST':
#         try:
#             broadcast = request.form['msg']
#             broadImg = request.form['bcImg']
#             image_message = ImageSendMessage(
#                 original_content_url=f'{broadImg}',
#                 preview_image_url=f'{broadImg}'
#             )
#             if broadcast or broadImg is None:
#                 line_bot_api2.broadcast(TextSendMessage(text=str(broadcast)))
#             elif broadImg or broadcast:
#                 line_bot_api2.broadcast(image_message)
#             else:
#                 line_bot_api2.broadcast(TextSendMessage(text=str(broadcast)))
#                 line_bot_api2.broadcast(image_message)
#             return redirect(url_for('new_chart'))
#         except:
#             tag = TagChart()
#             button = request.form['delete_button']
#             key = request.form.getlist('key')
#             excel = request.form.getlist('excel')
#             insert = request.form.getlist('insert')
#             tagIndex = request.form.getlist('tag')
#             jsonTag = request.get_json()
#             print(jsonTag)
#             print(tagIndex, 'tag')
#             print(insert, 'insert')
#             print(key, 'key')
#             print(excel, 'excel')
#             if button == 'Delete_button':
#                 print('Keep Delete')
#                 for k in key:
#                     db2.child('RestCustomer').child(k).remove()
#                 return redirect(url_for('new_chart'))
#             elif button == 'Excel_button':
#                 print('Keep Excel')
#                 lst = []
#                 for k in key:
#                     list_chart = tag.information_excel(k, db2)
#                     lst.append(list_chart)
#                 data = pd.DataFrame(lst)
#                 datatoexcel = pd.ExcelWriter('static/excel/Customers.xlsx', engine='xlsxwriter')
#                 data.to_excel(datatoexcel, sheet_name='Sheet1')
#                 datatoexcel.save()
#                 return send_from_directory('static/excel', 'Customers.xlsx')
#             elif button == 'Insert_button':
#                 _date = datetimeNow()
#                 diplayName = session['user_id']['displayName']
#                 if not tagIndex:
#                     for i in insert:
#                         group = tag.insert_to_information(i, diplayName, _date[0], _date[1], db2)
#                         db2.child('RestCustomer').push(group)
#                         db2.child('LineLiff').child(i).remove()
#                     return redirect(url_for('new_chart'))
#                 else:
#                     for i in insert:
#                         db2.child('LineLiff').child(i).update({'tag': tagIndex})
#                         group = tag.insert_to_information(i, diplayName, _date[0], _date[1], db2)
#                         db2.child('RestCustomer').push(group)
#                         db2.child('LineLiff').child(i).remove()
#             elif button == 'Excel_rest':
#                 print('Rest Excel')
#                 est = []
#                 for e in insert:
#                     list_chart = tag.import_excel(e, db2)
#                     est.append(list_chart)
#                 data = pd.DataFrame(est)
#                 datatoexcel = pd.ExcelWriter('static/excel/newCustomers.xlsx', engine='xlsxwriter')
#                 data.to_excel(datatoexcel, sheet_name='Sheet1')
#                 datatoexcel.save()
#                 return send_from_directory('static/excel', 'newCustomers.xlsx')
#             elif button == 'Delete_rest':
#                 print('Rest Delete')
#                 for i in insert:
#                     db2.child('LineLiff').child(i).remove()
#                 return redirect(url_for('new_chart'))
#             elif button == 'Tag':
#                 for i in insert:
#                     db2.child('LineLiff').child(i).update({'tag': tagIndex})
#                 return redirect(url_for('new_chart'))
#             elif button == 'RestTag':
#                 print('resttag')
#                 for k in key:
#                     data = db2.child('RestCustomer').child(k).update({'Tag': tagIndex})
#                     print(data)
#                 return redirect(url_for('new_chart'))
#         return redirect(url_for('new_chart'))
#
#
# @app.route('/getDemo', methods=['GET', 'POST'])
# def getDemo():
#     tag = ['CB010', 'CC010', 'CG010', 'CI010', 'CJ010', 'CM010',
#            'CF010',
#            'CP010', 'CE010', 'CH010', 'CK010', 'CN010', 'CD010', 'RC010',
#            'RA010', 'RB010']
#     if request.method == 'GET':
#         fire = FirebaseNewCustomer(db=db2)
#         lst = fire.restCustomer()
#         getDemo = fire.demoCustomer()
#         rest = len(lst)
#         data = {
#             'amountLiff': fire.lenLIFF(),
#             'amountRest': rest,
#             'tag': tag,
#             'rest': lst,
#             'amount': getDemo[1],
#             'demo': getDemo[0]
#         }
#         return render_template('customers_new/table/getDemo.html', data=data)
#     elif request.method == 'POST':
#         try:
#             broadcast = request.form['msg']
#             broadImg = request.form['bcImg']
#             image_message = ImageSendMessage(
#                 original_content_url=f'{broadImg}',
#                 preview_image_url=f'{broadImg}'
#             )
#             if broadcast or broadImg is None:
#                 line_bot_api2.broadcast(TextSendMessage(text=str(broadcast)))
#             elif broadImg or broadcast:
#                 line_bot_api2.broadcast(image_message)
#             else:
#                 line_bot_api2.broadcast(TextSendMessage(text=str(broadcast)))
#                 line_bot_api2.broadcast(image_message)
#             return redirect(url_for('getDemo'))
#         except:
#             gm = TagChart()
#             button = request.form['delete_button']
#             key = request.form.getlist('key')
#             excel = request.form.getlist('excel')
#             inserted = request.form.getlist('inserted')
#             tagIndex = request.form.getlist('tag')
#             print(f'button {button}, key {key}, excel {excel} inserted {inserted} tagIndex {tagIndex}')
#             if button == 'RestTag':
#                 for i in key:
#                     data = db2.child('requestDemo').child(i).update({'tag': tagIndex})
#                     print(data)
#             elif button == 'TagInformation':
#                 for i in inserted:
#                     data = db2.child('RestCustomer').child(i).update({'Tag': tagIndex})
#                     print(data)
#             elif button == 'Insert_button':
#                 _date = datetimeNow()
#                 diplayName = session['user_id']['displayName']
#                 if not tagIndex:
#                     for i in key:
#                         group = gm.chart_demo(i, diplayName, _date[0], _date[1], db2)
#                         db2.child('RestCustomer').push(group)
#                         db2.child('requestDemo').child(i).remove()
#             elif button == 'Excel_rest':
#                 lst = []
#                 for i in key:
#                     list_chart = gm.demo_excel(i, db2)
#                     lst.append(list_chart)
#                 data = pd.DataFrame(lst)
#                 datatoexcel = pd.ExcelWriter('static/excel/newCustomers.xlsx', engine='xlsxwriter')
#                 data.to_excel(datatoexcel, sheet_name='Sheet1')
#                 datatoexcel.save()
#                 return send_from_directory('static/excel', 'newCustomers.xlsx')
#             elif button == 'Excel_button':
#                 lst = []
#                 for k in inserted:
#                     list_chart = gm.information_excel(k, db2)
#                     lst.append(list_chart)
#                 data = pd.DataFrame(lst)
#                 datatoexcel = pd.ExcelWriter('static/excel/Customers.xlsx', engine='xlsxwriter')
#                 data.to_excel(datatoexcel, sheet_name='Sheet1')
#                 datatoexcel.save()
#                 return send_from_directory('static/excel', 'Customers.xlsx')
#             elif button == 'Delete_rest':
#                 for i in key:
#                     db2.child('requestDemo').child(i).remove()
#             elif button == 'Delete_button':
#                 for k in inserted:
#                     db2.child('RestCustomer').child(k).remove()
#             return redirect(url_for('getDemo'))
#
#
# @app.route('/tagliff/<string:lifftag>', methods=['GET', 'POST'])
# def lifftag(lifftag):
#     if request.method == 'GET':
#         ref = db2.child('LineLiff').get()
#         if lifftag == 'CB010':
#             data = req_path('CB010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'CC010':
#             data = req_path('CC010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'CG010':
#             data = req_path('CG010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'CI010':
#             data = req_path('CI010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'CJ010':
#             data = req_path('CJ010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'CM010':
#             data = req_path('CM010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'CF010':
#             data = req_path('CF010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'CP010':
#             data = req_path('CP010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'CE010':
#             data = req_path('CE010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'CH010':
#             data = req_path('CH010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'CK010':
#             data = req_path('CK010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'CN010':
#             data = req_path('CN010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'CD010':
#             data = req_path('CD010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'RC010':
#             data = req_path('RC010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'RA010':
#             data = req_path('RA010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#         elif lifftag == 'RB010':
#             data = req_path('RB010', ref, 'tag')
#             return render_template('customers_new/liff_tag.html', data=data)
#     elif request.method == 'POST':
#         tag = TagChart()
#         key = request.form.getlist('key')
#         excel = request.form.getlist('excel')
#         insert = request.form.getlist('insert')
#         tagIndex = request.form.getlist('tag')
#         jsontag = request.get_json()
#         button = request.form['delete_button']
#         print(jsontag)
#         print(tagIndex, 'tag')
#         print(insert, 'insert')
#         print(key, 'key')
#         print(excel, 'excel')
#         if button == 'Delete_button':
#             print('Keep Delete')
#             for k in key:
#                 k = str(k)
#                 db2.child('RestCustomer').child(k).remove()
#             return redirect(url_for('new_chart'))
#         elif button == 'Excel_button':
#             print('Keep Excel')
#             lst = []
#             for k in key:
#                 list_chart = tag.information_excel(k, db2)
#                 lst.append(list_chart)
#             data = pd.DataFrame(lst)
#             datatoexcel = pd.ExcelWriter('static/excel/Customers.xlsx', engine='xlsxwriter')
#             data.to_excel(datatoexcel, sheet_name='Sheet1')
#             datatoexcel.save()
#             return send_from_directory('static/excel', 'Customers.xlsx')
#         elif button == 'Insert_button':
#             print('Rest Insert')
#             _date = datetimeNow()
#             diplayName = session['user_id']['displayName']
#             if not tagIndex:
#                 print('ja')
#                 for i in insert:
#                     group = tag.insert_to_information(i, diplayName, _date[0], _date[1], db2)
#                     db2.child('RestCustomer').push(group)
#                     db2.child('LineLiff').child(i).remove()
#                 return redirect(url_for('new_chart'))
#             else:
#                 print('and')
#                 for i in insert:
#                     db2.child('LineLiff').child(i).update({'tag': tagIndex})
#                     group = tag.insert_to_information(i, diplayName, _date[0], _date[1], db2)
#                     db2.child('RestCustomer').push(group)
#                     db2.child('LineLiff').child(i).remove()
#         elif button == 'Excel_rest':
#             print('Rest Excel')
#             est = []
#             _date = datetimeNow()
#             eUser = session['user_id']['email']
#             diplayName = session['user_id']['displayName']
#             for e in insert:
#                 list_chart = tag.insert_to_information(e, diplayName, _date[0], _date[1], db2)
#                 est.append(list_chart)
#             data = pd.DataFrame(est)
#             datatoexcel = pd.ExcelWriter('static/excel/newCustomers.xlsx', engine='xlsxwriter')
#             data.to_excel(datatoexcel, sheet_name='Sheet1')
#             datatoexcel.save()
#             return send_from_directory('static/excel', 'newCustomers.xlsx')
#         elif button == 'Delete_rest':
#             print('Rest Delete')
#             for i in insert:
#                 db2.child('LineLiff').child(i).remove()
#             return redirect(url_for('new_chart'))
#         elif button == 'Tag':
#             print('tagIndex')
#             print(jsontag)
#             for i in insert:
#                 data = db2.child('LineLiff').child(i).update({'tag': tagIndex})
#                 print(data)
#             return redirect(url_for('new_chart'))
#         elif button == 'RestTag':
#             print('resttag')
#             for k in key:
#                 data = db2.child('RestCustomer').child(k).update({'Tag': tagIndex})
#                 print(data)
#             return redirect(url_for('new_chart'))
#         return redirect(url_for('new_chart'))
#
#
# @app.route('/tagrest/<string:lifftag>', methods=['GET', 'POST'])
# def tagrest(lifftag):
#     if request.method == 'GET':
#         tag = ['CB010', 'CC010', 'CG010', 'CI010', 'CJ010', 'CM010',
#                'CF010', 'CP010', 'CE010', 'CH010', 'CK010', 'CN010', 'CD010',
#                'RC010', 'RA010', 'RB010']
#         ref = db2.child('RestCustomer').get()
#         fire = FirebaseNewCustomer(db=db2)
#         lst = fire.restCustomer()
#         est = fire.liffCustomer()
#         _id = len(lst)
#         ee = len(est)
#         var = {
#             'tag': tag,
#             'users': lst,
#             'est': est,
#             'msg': _id,
#             'amount': ee
#         }
#         if lifftag == 'CB010':
#             data = req_path('CB010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'CC010':
#             data = req_path('CC010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'CG010':
#             data = req_path('CG010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'CI010':
#             data = req_path('CI010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'CJ010':
#             data = req_path('CJ010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'CM010':
#             data = req_path('CM010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'CF010':
#             data = req_path('CF010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'CP010':
#             data = req_path('CP010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'CE010':
#             data = req_path('CE010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'CH010':
#             data = req_path('CH010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'CK010':
#             data = req_path('CK010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'CN010':
#             data = req_path('CN010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'CD010':
#             data = req_path('CD010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'RC010':
#             data = req_path('RC010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'RA010':
#             data = req_path('RA010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#         elif lifftag == 'RB010':
#             data = req_path('RB010', ref, 'Tag')
#             return render_template('customers_new/tag_rest.html', data=data, index=var)
#     elif request.method == 'POST':
#         tag = TagChart()
#         key = request.form.getlist('key')
#         excel = request.form.getlist('excel')
#         insert = request.form.getlist('insert')
#         tagIndex = request.form.getlist('tag')
#         jsontag = request.get_json()
#         button = request.form['delete_button']
#         print(jsontag)
#         print(tagIndex, 'tag')
#         print(insert, 'insert')
#         print(key, 'key')
#         print(excel, 'excel')
#         if button == 'Delete_button':
#             print('Keep Delete')
#             for k in key:
#                 k = str(k)
#                 db2.child('RestCustomer').child(k).remove()
#             return redirect(url_for('new_chart'))
#         elif button == 'Excel_button':
#             print('Keep Excel')
#             lst = []
#             for k in key:
#                 list_chart = tag.information_excel(k, db2)
#                 lst.append(list_chart)
#             data = pd.DataFrame(lst)
#             datatoexcel = pd.ExcelWriter('static/excel/Customers.xlsx', engine='xlsxwriter')
#             data.to_excel(datatoexcel, sheet_name='Sheet1')
#             datatoexcel.save()
#             return send_from_directory('static/excel', 'Customers.xlsx')
#         elif button == 'Insert_button':
#             print('Rest Insert')
#             _date = datetimeNow()
#             diplayName = session['user_id']['displayName']
#             if not tagIndex:
#                 print('ja')
#                 for i in insert:
#                     group = tag.insert_to_information(i, diplayName, _date[0], _date[1], db2)
#                     db2.child('RestCustomer').push(group)
#                     db2.child('LineLiff').child(i).remove()
#                 return redirect(url_for('new_chart'))
#             else:
#                 print('and')
#                 for i in insert:
#                     db2.child('LineLiff').child(i).update({'tag': tagIndex})
#                     group = tag.insert_to_information(i, diplayName, _date[0], _date[1], db2)
#                     db2.child('RestCustomer').push(group)
#                     db2.child('LineLiff').child(i).remove()
#         elif button == 'Excel_rest':
#             print('Rest Excel')
#             est = []
#             _date = datetimeNow()
#             diplayName = session['user_id']['displayName']
#             for e in insert:
#                 list_chart = tag.insert_to_information(e, diplayName, _date[0], _date[1], db2)
#                 est.append(list_chart)
#             data = pd.DataFrame(est)
#             datatoexcel = pd.ExcelWriter('static/excel/newCustomers.xlsx', engine='xlsxwriter')
#             data.to_excel(datatoexcel, sheet_name='Sheet1')
#             datatoexcel.save()
#             return send_from_directory('static/excel', 'newCustomers.xlsx')
#         elif button == 'Delete_rest':
#             print('Rest Delete')
#             for i in insert:
#                 db2.child('LineLiff').child(i).remove()
#             return redirect(url_for('new_chart'))
#         elif button == 'Tag':
#             print('tagIndex')
#             print(jsontag)
#             for i in insert:
#                 data = db2.child('LineLiff').child(i).update({'tag': tagIndex})
#                 print(data)
#             return redirect(url_for('new_chart'))
#         elif button == 'RestTag':
#             print('resttag')
#             for k in key:
#                 data = db2.child('RestCustomer').child(k).update({'Tag': tagIndex})
#                 print(data)
#             return redirect(url_for('new_chart'))
#         return redirect(url_for('new_chart'))
#
#
# @app.route('/graph', methods=['GET', 'POST'])
# def graph():
#     if not g.user:
#         return redirect(url_for('welcome'))
#     if request.method == 'GET':
#         ref = db2.child('chat-flex').get()
#         count = 1
#         lst = []
#         stats = []
#         for i in ref.each()[1:]:
#             k = i.key()
#             msg = i.val()['reply']
#             stats.append(msg)
#             user = dict(i.val())
#             user.update({'index': count, 'key': k})
#             lst.append(user)
#             count += 1
#         Rental = [s for s in stats if 'Rental' in s]
#         CSM = [s for s in stats if 'Customer Service Management' in s]
#         QCM = [s for s in stats if 'Quality Control Management' in s]
#         Maintenance = [s for s in stats if 'Maintenance' in s]
#         MRP = [s for s in stats if 'MRP' in s]
#         Rent = [s for s in stats if 'เช่าสุดคุ้ม' in s]
#         PJ = [s for s in stats if 'Project Planning' in s]
#         Con = [s for s in stats if 'Construction' in s]
#         Real = [s for s in stats if 'Real Estate' in s]
#         Rental = len(Rental)
#         CSM = len(CSM)
#         QCM = len(QCM)
#         Maintenance = len(Maintenance)
#         MRP = len(MRP)
#         Rent = len(Rent)
#         PJ = len(PJ)
#         Con = len(Con)
#         Real = len(Real)
#         stf = datetime.today().strftime('%B')
#         key_erp = {'Rental': Rental, 'CSM': CSM,
#                    'QCM': QCM, 'Maintenance': Maintenance, 'MRP': MRP, 'เช่าสุดคุ้ม': Rent,
#                    'Project Planning': PJ, 'Construction': Con, 'Real Estate': Real}
#         value_erp = Rental, CSM, QCM, Maintenance, MRP, Rent, PJ, Con, Real
#         value_erp = list(value_erp)
#         key_erp = max(key_erp)
#         value_erp = max(value_erp)
#         data = {
#             'stff': stf,
#             'user': lst,
#             'rental': Rental,
#             'csm': CSM,
#             'qcm': QCM,
#             'main': Maintenance,
#             'mrp': MRP,
#             'rent': Rent,
#             'pj': PJ,
#             'con': Con,
#             'real': Real,
#             'key_erp': key_erp,
#             'value_erp': str(value_erp)
#         }
#         return render_template('customers_new/graph.html', data=data)
#     elif request.method == 'POST':
#         key = request.form.getlist('key')
#         print(key)
#         for k in key:
#             k = str(k)
#             db2.child('chat-flex').child(k).remove()
#         return redirect(url_for('graph'))
#     return render_template('customers_new/graph.html')
#
#
# def datetimeNow():
#     day = datetime.today().day
#     month = datetime.today().month
#     second = datetime.today().second
#     minute = datetime.today().minute
#     hour = datetime.today().hour
#     year = datetime.today().year
#     timeNow = f'{hour}:{minute}:{second}'
#     dateNow = f'{day}-{month}-{year}'
#     return dateNow, timeNow
#
#
# def req_path(tag, ref, upper):
#     tags = ['CB010', 'CC010', 'CG010', 'CI010', 'CJ010', 'CM010',
#             'CF010', 'CP010', 'CE010', 'CH010', 'CK010', 'CN010', 'CD010',
#             'RC010', 'RA010', 'RB010']
#     lst = []
#     eCount = 1
#     for i in ref.each()[1:]:
#         if tag in i.val()[upper]:
#             k = i.key()
#             user = dict(i.val())
#             user.update({'index': str(eCount), 'key': k})
#             lst.append(user)
#             eCount = eCount + 1
#     data = {
#         'lst': lst,
#         'tag': tags
#     }
#     return data
#
#
# @app.route('/download')
# def download():
#     if request.method == 'GET':
#         ref = db2.child('RestCustomer').get()
#         date_time = []
#         for i in ref.each()[1:]:
#             profile = i.val()['Profile']
#             cTime = i.val()['Time']
#             cDate = i.val()['Date']
#             company = i.val()['Company']
#             email = i.val()['Email']
#             pEmail = i.val()['EmailLiff']
#             message = i.val()['Message']
#             picture = i.val()['Picture']
#             product = i.val()['Product']
#             tag = i.val()['Tag']
#             tel = i.val()['Tel']
#             name = i.val()['Name']
#             username = i.val()['Username']
#             ImportDate = i.val()['DateInsert']
#             ImportTime = i.val()['TimeInsert']
#             group = {'Name': name, 'Product': product, 'Company': company, 'Tel': tel, 'Email': email,
#                      'EmailLiff': pEmail, 'Message': message, 'Profile': profile, 'Date': cDate, 'Time': cTime,
#                      'Picture': picture, 'Username': username, 'Tag': tag,
#                      'ImportDate/Time': f'{ImportDate} {ImportTime}',
#                      }
#             date_time.append(group)
#         dbDatetime = date_time
#         data = pd.DataFrame(dbDatetime)
#         datatoexcel = pd.ExcelWriter('static/excel/FromPython.xlsx', engine='xlsxwriter')
#         data.to_excel(datatoexcel, sheet_name='Sheet1')
#         datatoexcel.save()
#         return send_from_directory('static/excel', 'FromPython.xlsx')
#     return redirect(url_for('new_chart'))
#
#
# @app.route('/stats_download', methods=['GET'])
# def stats_download():
#     if request.method == 'GET':
#         date_time = []
#         ref = db2.child('chat-flex').get()
#         for e in ref.each():
#             # index = e['index']
#             profile = e.val()['profile']
#             erp = e.val()['message']
#             reply = e.val()['reply']
#             year = e.val()['year']
#             month = e.val()['month']
#             day = e.val()['day']
#             dbTime = {'profile': profile, 'question': erp, 'reply': reply, 'year': year, 'month': month, 'day': day}
#             date_time.append(dbTime)
#         dbDatetime = date_time
#         data = pd.DataFrame(dbDatetime)
#         datatoexcel = pd.ExcelWriter('static/excel/Stats.xlsx', engine='xlsxwriter')
#         data.to_excel(datatoexcel, sheet_name='Sheet1')
#         datatoexcel.save()
#         return send_from_directory('static/excel', 'Stats.xlsx')
#     return redirect(url_for('graph'))
#
#
# @app.route('/r_stat/<string:key>', methods=['GET'])
# def remove_stats(key):
#     db2.child('chat-flex').child(key).remove()
#     return redirect(url_for('graph'))
#
#
# @app.route('/api/upload', methods=['POST'])
# def upload():
#     image = cv2.imdecode(np.fromstring(request.files['image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
#     img_processed = detect_object(image, None, None, None)
#     print(img_processed)
#     print(type(img_processed))
#     return jsonify(img_processed)
#
#
# @app.route('/webhook', methods=['GET', 'POST'])
# def webhook():
#     if request.method == 'POST':
#         raw_json = request.get_json()
#         json_line = json.dumps(raw_json)
#         decoded = json.loads(json_line)
#         with open('dataline.json', 'w') as dataline:
#             json.dump(raw_json, dataline)
#         body = request.get_data(as_text=True)
#         signature = request.headers['X-Line-Signature']
#         try:
#             postback = decoded['events'][0]['type']
#             data = decoded['events'][0]['postback']['data']
#             if postback == 'postback':
#                 no_event = len(decoded['events'])
#                 for i in range(no_event):
#                     event = decoded['events'][i]
#                     event_handler(event)
#         except:
#             _type = decoded['events'][0]['message']['type']
#             if _type == 'text':
#                 try:
#                     handler1.handle(body, signature)
#                 except InvalidSignatureError:
#                     abort(400)
#             else:
#                 no_event = len(decoded['events'])
#                 for i in range(no_event):
#                     event = decoded['events'][i]
#                     event_handler(event)
#     return 'ok'
#
#
# @app.route('/webhookNew', methods=['GET', 'POST'])
# def webhookNew():
#     if request.method == 'POST':
#         raw_json = request.get_json()
#         json_line = json.dumps(raw_json)
#         decoded = json.loads(json_line)
#         with open('dataline.json', 'w') as dataline:
#             json.dump(raw_json, dataline)
#         body = request.get_data(as_text=True)
#         signature = request.headers['X-Line-Signature']
#         try:
#             postback = decoded['events'][0]['type']
#             data = decoded['events'][0]['postback']['data']
#             if postback == 'postback':
#                 no_event = len(decoded['events'])
#                 for i in range(no_event):
#                     event = decoded['events'][i]
#                     event_handler1(event)
#         except:
#             _type = decoded['events'][0]['message']['type']
#             if _type == 'text':
#                 txt = decoded['events'][0]['message']['text']
#                 try:
#                     handler2.handle(body, signature)
#                 except InvalidSignatureError:
#                     abort(400)
#             else:
#                 no_event = len(decoded['events'])
#                 for i in range(no_event):
#                     event = decoded['events'][i]
#                     event_handler1(event)
#     return ''
#
#
# @app.route('/webhookOld', methods=['GET', 'POST'])
# def webhookOld():
#     if request.method == 'POST':
#         raw_json = request.get_json()
#         json_line = json.dumps(raw_json)
#         decoded = json.loads(json_line)
#         with open('dataline.json', 'w') as dataline:
#             json.dump(raw_json, dataline)
#         body = request.get_data(as_text=True)
#         signature = request.headers['X-Line-Signature']
#         _type = decoded['events'][0]['message']['type']
#         print(_type)
#         print(signature)
#         if _type == 'text':
#             txt = decoded['events'][0]['message']['text']
#             print(txt)
#             try:
#                 handler3.handle(body, signature)
#             except InvalidSignatureError:
#                 abort(400)
#         else:
#             no_event = len(decoded['events'])
#             for i in range(no_event):
#                 event = decoded['events'][i]
#                 event_handler2(event)
#     return ''
#
#
# def event_handler(event):
#     postback = event['type']
#     rtoken = event['replyToken']
#     try:
#         data = event['postback']['data']
#         if postback == 'postback':
#             if data == 'quote':
#                 line_bot_api1.reply_message(rtoken, TextSendMessage(
#                     text='พิมพ์คำขึ้นต้นด้วย เช่าสุดคุ้ม ตามด้วย ชื่อ บริษัท เบอร์  อีเมลล์ จำนวน User ที่ต้องการใช้'))
#     except:
#         _type = event['message']['type']
#         img = event['message']['id']
#         user_id = event['source']['userId']
#         sk_id = randrange(51626494, 51626533)
#         if _type == 'sticker':
#             replyObj = StickerSendMessage(package_id=str(11538), sticker_id=str(sk_id))
#             line_bot_api1.reply_message(rtoken, replyObj)
#         else:
#             print(img)
#             message_content = line_bot_api1.get_message_content(img)
#             with open('static/images/line.png', 'wb') as fb:
#                 for chunk in message_content.iter_content():
#                     fb.write(chunk)
#             image = cv2.imread('static/images/line.png', cv2.IMREAD_UNCHANGED)
#             detect_object(image, rtoken, user_id, line_bot_api1)
#
#
# def event_handler1(event):
#     postback = event['type']
#     rtoken = event['replyToken']
#     try:
#         data = event['postback']['data']
#         userid = event['source']['userId']
#         if postback == 'postback':
#             print(data)
#             if data == 'CSM':
#                 x = 'Customer Service Management'
#                 line_bot_api2.reply_message(rtoken, TextSendMessage(
#                     text='ผลิตภัณฑ์นี้เหมาะสำหรับบริษัทฯ ที่ใช้ Software ERP Mango Anywhere '
#                          'เท่านั้น\nหากท่านสนใจใช้ สามารถติดต่อเจ้าหน้าที่ฝ่ายขาย\nได้ที่เบอร์ 063 565 4594 ค่ะ'))
#                 Insert = get_postback(x, line_bot_api2)
#                 showDB = db2.child('chat-flex').push(Insert)
#                 print('show: ', showDB)
#             elif data == 'QCM':
#                 x = 'Quality Control Management'
#                 line_bot_api2.reply_message(rtoken, TextSendMessage(
#                     text='ผลิตภัณฑ์นี้เหมาะสำหรับบริษัทฯ ที่ใช้ Software ERP Mango Anywhere '
#                          'เท่านั้น\nหากท่านสนใจใช้ สามารถติดต่อเจ้าหน้าที่ฝ่ายขาย\nได้ที่เบอร์ 063 565 4594 ค่ะ'))
#                 Insert = get_postback(x, line_bot_api2)
#                 showDB = db2.child('chat-flex').push(Insert)
#                 print('show: ', showDB)
#             elif data == 'maintenance':
#                 x = 'Maintenance'
#                 line_bot_api2.reply_message(rtoken, TextSendMessage(
#                     text='ผลิตภัณฑ์นี้เหมาะสำหรับบริษัทฯ ที่ใช้ Software ERP Mango Anywhere '
#                          'เท่านั้น\nหากท่านสนใจใช้ สามารถติดต่อเจ้าหน้าที่ฝ่ายขาย\nได้ที่เบอร์ 063 565 4594 ค่ะ'))
#                 Insert = get_postback(x, line_bot_api2)
#                 showDB = db2.child('chat-flex').push(Insert)
#                 print('show: ', showDB)
#             elif data == 'rental':
#                 x = 'Rental'
#                 line_bot_api2.reply_message(rtoken, TextSendMessage(
#                     text='ผลิตภัณฑ์นี้เหมาะสำหรับบริษัทฯ ที่ใช้ Software ERP Mango Anywhere '
#                          'เท่านั้น\nหากท่านสนใจใช้ สามารถติดต่อเจ้าหน้าที่ฝ่ายขาย\nได้ที่เบอร์ 063 565 4594 ค่ะ'))
#                 Insert = get_postback(x, line_bot_api2)
#                 showDB = db2.child('chat-flex').push(Insert)
#                 print('show: ', showDB)
#             elif data == 'mrp':
#                 x = 'MRP'
#                 line_bot_api2.reply_message(rtoken, TextSendMessage(
#                     text='ผลิตภัณฑ์นี้เหมาะสำหรับบริษัทฯ ที่ใช้ Software ERP Mango Anywhere '
#                          'เท่านั้น\nหากท่านสนใจใช้ สามารถติดต่อเจ้าหน้าที่ฝ่ายขาย\nได้ที่เบอร์ 063 565 4594 ค่ะ'))
#                 Insert = get_postback(x, line_bot_api2)
#                 showDB = db2.child('chat-flex').push(Insert)
#                 print('show: ', showDB)
#     except:
#         _type = event['message']['type']
#         img = event['message']['id']
#         user_id = event['source']['userId']
#         sk_id = randrange(51626494, 51626533)
#         if _type == 'sticker':
#             replyObj = StickerSendMessage(package_id=str(11538), sticker_id=str(sk_id))
#             line_bot_api2.reply_message(rtoken, replyObj)
#         else:
#             print(img)
#             message_content = line_bot_api2.get_message_content(img)
#             with open('static/images/line.png', 'wb') as fb:
#                 for chunk in message_content.iter_content():
#                     fb.write(chunk)
#             image = cv2.imread('static/images/line.png', cv2.IMREAD_UNCHANGED)
#             detect_object(image, rtoken, user_id, line_bot_api2)
#
#
# def event_handler2(event):
#     rtoken = event['replyToken']
#     _type = event['message']['type']
#     img = event['message']['id']
#     sk_id = randrange(51626494, 51626533)
#     if _type == 'sticker':
#         replyObj = StickerSendMessage(package_id=str(11538), sticker_id=str(sk_id))
#         line_bot_api3.reply_message(rtoken, replyObj)
#     else:
#         print(img)
#         message_content = line_bot_api3.get_message_content(img)
#         with open('img/file_path.png', 'wb') as fb:
#             for chunk in message_content.iter_content():
#                 fb.write(chunk)
#
#
# def detect_object(img, rtoken, user_id, line_bot_api):
#     scale = 0.5
#     img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
#     height, width, channels = img.shape
#     name_app = []
#     # Detecting objects
#     blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
#     net.setInput(blob)
#     outs = net.forward(output_layers)
#
#     class_ids = []
#     confidences = []
#     boxes = []
#     stff = time.time()
#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             # print(confidence)
#             if confidence > 0.5:
#                 # Object detected
#                 center_x = int(detection[0] * width)
#                 center_y = int(detection[1] * height)
#                 w = int(detection[2] * width)
#                 h = int(detection[3] * height)
#                 # Rectangle coordinates
#                 x = int(center_x - w / 2)
#                 y = int(center_y - h / 2)
#                 boxes.append([x, y, w, h])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)
#     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     label_str = []
#     for i in range(len(boxes)):
#         if i in indexes:
#             print(i, indexes)
#             x, y, w, h = boxes[i]
#             label = str(classes[class_ids[i]])
#             label_str.append(label)
#             color = colors[i]
#             cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
#             cv2.putText(img, label, (x, y - 5), font, .7, color, 2)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     dets = detector(gray, 1)
#     for d in dets:
#         xy = d.left(), d.top()
#         wh = d.right(), d.bottom()
#         shape = sp(img, d)
#         face_desc0 = model.compute_face_descriptor(img, shape, 1)  # output deeplearning
#         d = []
#         for face_desc in FACE_DESC:
#             d.append(np.linalg.norm(np.array(face_desc) - np.array(face_desc0)))
#         d = np.array(d)  # compare picture
#         idx = np.argmin(d)  # ระบุลาเบล
#         print(d[idx])
#         if d[idx] <= 0.45:
#             name = FACE_NAME[idx]
#             name = str(name)
#             print(name)
#             name_app.append(name)
#             cv2.putText(img, name, (xy[0], xy[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#             cv2.rectangle(img, xy, wh, (0, 255, 0), 2)
#         else:
#             name = 'Unknown'
#             print(name)
#             name_app.append(name)
#             cv2.putText(img, name, (xy[0], xy[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
#             cv2.rectangle(img, xy, wh, (0, 0, 255), 2)
#     str_name = ''
#     str_object = ''
#     for n in name_app:
#         str_name = str_name + n.ljust(8)
#     for l in label_str:
#         str_object = str_object + l.ljust(8)
#     img_item = 'static/images/predict_rec.png'
#     cv2.imwrite(img_item, img)
#     image_name = 'static/images/predict_rec.png'
#     dir_name = 'static/images/face_people'
#     img_name = uuid.uuid4().hex
#
#     if not os.path.exists(dir_name):
#         os.makedirs(dir_name)
#     with open(image_name, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     with open(os.path.join(dir_name, '{}.jpg'.format(img_name)), 'wb') as image_base:
#         image_base.write(base64.b64decode(encoded_string))
#     original = Image.open(os.path.join(dir_name, '{}.jpg'.format(img_name)))
#     original.thumbnail((240, 240), Image.ANTIALIAS)
#     original.save(os.path.join(dir_name, '{}_240.jpg'.format(img_name)), 'JPEG')
#     img_origin = 'https://www.mangoconsultant.net' + '/' + dir_name + '/' + img_name + '.jpg'
#     img_240 = 'https://www.mangoconsultant.net' + '/' + dir_name + '/' + img_name + '_240.jpg'
#     print(img_origin)
#     print(img_240)
#     image_message = ImageSendMessage(
#         original_content_url=img_origin,
#         preview_image_url=img_240
#     )
#     if not str_name and not str_object:
#         line_bot_api.push_message(user_id, TextSendMessage(
#             text='รูปที่คุณถ่าย ไม่สามารถระบุได้ โปรดถ่ายรูปหน้าคน หรือ รถสิ่งของต่าง ๆ'))
#     else:
#         line_bot_api.reply_message(rtoken, image_message)
#         line_bot_api.push_message(user_id, TextSendMessage(text=f'นี้อาจจะเป็น {str(str_name)}รูปแบบ {str_object}'))
#     return str(str_name)
#
#
# def model_linebot():
#     raw_json = request.get_json()
#     json_line = json.dumps(raw_json)
#     decoded = json.loads(json_line)
#     messsage = decoded['events'][0]['message']['text']
#     userId = decoded['events'][0]['source']['userId']
#     embedding = []
#     answers = []
#     xtrain = []
#     datasets = db1.child('transaction_mango').child('datasets').get()
#     count = 0
#     for d in datasets.each():
#         if d.val():
#             txt = ''
#             answers.append(d.val()['answers'])
#             if d.val()['questions']:
#                 for i in d.val()['questions']:
#                     txt = txt + i
#                 xtrain.append(txt)
#                 embedding.append(count)
#                 count += 1
#     idx_answer = []
#     for a in answers:
#         idx = list(a)
#         sli = idx[1:]
#         idx_answer.append(sli)
#     # print(idx_answer)
#     count_vect = CountVectorizer(tokenizer=tokenize)
#     Xtrain_count = count_vect.fit_transform(xtrain)
#     tf_transformer = TfidfTransformer(use_idf=False)
#     tf_transformer.fit(Xtrain_count)
#     Xtrain_tf = tf_transformer.transform(Xtrain_count)
#     SVM = svm.SVC(C=1.0, kernel='linear', degree=3,
#                   gamma='auto', probability=True)
#     SVM.fit(Xtrain_tf, embedding)
#     msg = []
#     msg.append(messsage)
#     Xtest_count = count_vect.transform(msg)
#     Xtest_tf = tf_transformer.transform(Xtest_count)
#     label = SVM.predict(Xtest_tf)
#     prop = SVM.predict_proba(Xtest_tf)[0][label]
#     confidence = (0.3565152559 / ((len(embedding) * float(prop)) ** 0.5)) ** 2
#     print(label)
#     if label == [4]:
#         db1.child('customer_email').push(get_datetime(None, line_bot_api1))
#     return confidence, idx_answer, label, msg, userId
#
#
# def model_linebot_new():
#     raw_json = request.get_json()
#     json_line = json.dumps(raw_json)
#     decoded = json.loads(json_line)
#     messsage = decoded['events'][0]['message']['text']
#     userId = decoded['events'][0]['source']['userId']
#     replyToken = decoded['events'][0]['replyToken']
#     embedding = []
#     answers = []
#     xtrain = []
#     datasets = db2.child('transaction_mango').child('datasets').get()
#     count = 0
#     for d in datasets.each():
#         if d.val():
#             txt = ''
#             answers.append(d.val()['answers'])
#             if d.val()['questions']:
#                 for i in d.val()['questions']:
#                     txt = txt + i
#                 xtrain.append(txt)
#                 embedding.append(count)
#                 count += 1
#     idx_answer = []
#     for a in answers:
#         idx = list(a)
#         sli = idx[1:]
#         idx_answer.append(sli)
#     # print(idx_answer)
#     count_vect = CountVectorizer(tokenizer=tokenize)
#     Xtrain_count = count_vect.fit_transform(xtrain)
#     tf_transformer = TfidfTransformer(use_idf=False)
#     tf_transformer.fit(Xtrain_count)
#     Xtrain_tf = tf_transformer.transform(Xtrain_count)
#     SVM = svm.SVC(C=1.0, kernel='linear', degree=3,
#                   gamma='auto', probability=True)
#     SVM.fit(Xtrain_tf, embedding)
#     msg = []
#     msg.append(messsage)
#     Xtest_count = count_vect.transform(msg)
#     Xtest_tf = tf_transformer.transform(Xtest_count)
#     label = SVM.predict(Xtest_tf)
#     prop = SVM.predict_proba(Xtest_tf)[0][label]
#     p = float(prop)
#     print(label)
#     confidence = (0.3565152559 / ((len(embedding) * p) ** 0.5)) ** 2
#     return confidence, idx_answer, label, msg, userId
#
#
# def model_linebot_old():
#     raw_json = request.get_json()
#     json_line = json.dumps(raw_json)
#     decoded = json.loads(json_line)
#     messsage = decoded['events'][0]['message']['text']
#     userId = decoded['events'][0]['source']['userId']
#     embedding = []
#     answers = []
#     xtrain = []
#     datasets = db3.child('transaction_mango').child('datasets').get()
#     count = 0
#     for d in datasets.each():
#         if d.val():
#             txt = ''
#             answers.append(d.val()['answers'])
#             if d.val()['questions']:
#                 for i in d.val()['questions']:
#                     txt = txt + i
#                 xtrain.append(txt)
#                 embedding.append(count)
#                 count += 1
#     idx_answer = []
#     for a in answers:
#         idx = list(a)
#         sli = idx[1:]
#         idx_answer.append(sli)
#     count_vect = CountVectorizer(tokenizer=tokenize)
#     Xtrain_count = count_vect.fit_transform(xtrain)
#     tf_transformer = TfidfTransformer(use_idf=False)
#     tf_transformer.fit(Xtrain_count)
#     Xtrain_tf = tf_transformer.transform(Xtrain_count)
#     SVM = svm.SVC(C=1.0, kernel='linear', degree=3,
#                   gamma='auto', probability=True)
#     SVM.fit(Xtrain_tf, embedding)
#     msg = []
#     msg.append(messsage)
#     Xtest_count = count_vect.transform(msg)
#     Xtest_tf = tf_transformer.transform(Xtest_count)
#     label = SVM.predict(Xtest_tf)
#     prop = SVM.predict_proba(Xtest_tf)[0][label]
#     p = float(prop)
#     confidence = (0.3565152559 / ((len(embedding) * p) ** 0.5)) ** 2
#     print('value3')
#     return confidence, idx_answer, label, msg, userId
#
#
# def get_link(x):
#     message = 'link'
#     profile = '[ตัวลิงค์จะไม่สามารถได้ชื่อคน]'
#     stf = datetime.today()
#     stff = stf.strftime('%B')
#     day = datetime.today().day
#     month = datetime.today().month
#     second = datetime.today().second
#     minute = datetime.today().minute
#     hour = datetime.today().hour
#     year = datetime.today().year
#     result = {'profile': profile, 'message': message, 'reply': x, 'hour': hour, 'min': minute,
#               'sec': second, 'day': day, 'month': month, 'year': year, 'now': stff}
#     return result
#
#
# def get_postback(x, line_bot_api):
#     raw_json = request.get_json()
#     json_line = json.dumps(raw_json)
#     decoded = json.loads(json_line)
#     message = 'postback'
#     userId = decoded['events'][0]['source']['userId']
#     day = datetime.today().day
#     month = datetime.today().month
#     second = datetime.today().second
#     minute = datetime.today().minute
#     hour = datetime.today().hour
#     year = datetime.today().year
#     profile = line_bot_api.get_profile(userId)
#     profile = profile.display_name
#     profile = str(profile)
#     result = {'userid': userId, 'message': message, 'reply': x, 'profile': profile, 'hour': hour, 'min': minute,
#               'sec': second, 'day': day, 'month': month, 'year': year}
#     return result
#
#
# def get_datetime(x, line_bot_api):
#     raw_json = request.get_json()
#     json_line = json.dumps(raw_json)
#     decoded = json.loads(json_line)
#     message = decoded['events'][0]['message']['text']
#     userId = decoded['events'][0]['source']['userId']
#     day = datetime.today().day
#     month = datetime.today().month
#     second = datetime.today().second
#     minute = datetime.today().minute
#     hour = datetime.today().hour
#     year = datetime.today().year
#     profile = line_bot_api.get_profile(userId)
#     img = profile.picture_url
#     profile = profile.display_name
#     profile = str(profile)
#     result = {'userid': userId, 'message': message, 'reply': x, 'profile': profile, 'img': img, 'hour': hour,
#               'min': minute,
#               'sec': second, 'day': day, 'month': month, 'year': year}
#     return result
#
#
# def questionFor(question, resule):
#     pre = [x for x in question if resule == [x]]
#     return pre
#
#
# def quick_reply(event, x, QuickReply):
#     line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=x, quick_reply=QuickReply))
#
#
# def integrate_send(model_linebot, event, pack, stick, line_bot_api):
#     result = model_linebot
#     stick = random.choice(stick)
#     x = random.choice(result[1][int(result[2])])
#     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
#     line_bot_api.push_message(result[4], StickerSendMessage(package_id=str(pack), sticker_id=str(stick)))
#
#
# @handler1.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     result = model_linebot()
#     print(result[0])
#     try:
#         print('Result 1')
#         if result[0] >= 0.14367:
#             if ['ขอข้อมูลผลิตภัณฑ์'] == result[3]:
#                 x = 'card'
#                 line_bot_api1.reply_message(event.reply_token, product_action())
#                 inserted = get_datetime(x, line_bot_api1)
#                 db1.child('chatbot_transactions').push(inserted)
#             elif ['ขอดู'] == result[3]:
#                 x = 'https://liff.line.me/1655104822-k5dRGJez'
#                 line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
#             elif ['@mango'] == result[3]:
#                 line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'{result[4]}'))
#             elif ['ฉันชื่ออะไร'] == result[3]:
#                 profile = line_bot_api1.get_profile(result[4])
#                 user_profile = profile.display_name
#                 user_profile = str(user_profile)
#                 line_bot_api1.reply_message(event.reply_token,
#                                             TextSendMessage(text=f'เอ้า! ลืมชื่อตัวเองแล้วหรอ ก็ {user_profile} ไง'))
#             else:
#                 if result[2] == [1]:
#                     stick = ['52114110', '52114115', '52114129', '52114122']
#                     pack = 11539
#                     integrate_send(model_linebot(), event, pack, stick, line_bot_api1)
#                 elif result[2] == [6]:
#                     stick = ['52114116', '52114117', '52114125']
#                     pack = 11539
#                     integrate_send(model_linebot(), event, pack, stick, line_bot_api1)
#                 elif result[2] == [5]:
#                     stick = ['52114111', '52114119', '52114130']
#                     pack = 11539
#                     integrate_send(model_linebot(), event, pack, stick, line_bot_api1)
#                 else:
#                     x = random.choice(result[1][int(result[2])])
#                     line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
#                     q_a = get_datetime(x, line_bot_api1)
#                     inserted = db1.child('chatbot_transactions').push(q_a)
#                     print(f'Inserted : {inserted}')
#         else:
#             if ['เปิดไฟ'] == result[3]:
#                 line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'โอเคจ้า ทำการเปิดไฟ'))
#                 db1.child('Node1').update({'Relay1': 0})
#             elif ['ปิดไฟ'] == result[3]:
#                 line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'โอเคจ้า ทำการปิดไฟ'))
#                 db1.child('Node1').update({'Relay1': 1})
#             elif ['temp'] == result[3]:
#                 temp = db1.child('Sensor Ultrasonic').get()
#                 temp = temp.val()
#                 line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'Temperature {temp} C'))
#             elif ['@Construction'] == result[3]:
#                 line_bot_api1.reply_message(event.reply_token, flex_product())
#             elif ['test'] == result[3]:
#                 line_bot_api1.reply_message(event.reply_token, flex_erp())
#     except LineBotApiError:
#         abort(400)
#
#
# @handler2.add(MessageEvent, message=TextMessage)
# def handle_message_new(event):
#     result = model_linebot_new()
#     print(result[0])
#     whatever = FAQ().whatever
#     whatever = questionFor(whatever, result[3])
#     areSure = FAQ().areSure
#     areSure = questionFor(areSure, result[3])
#     mango = FAQ().mango
#     mango = questionFor(mango, result[3])
#     try:
#         if result[0] >= 0.14:
#             if ['ขอข้อมูลผลิตภัณฑ์'] == result[3]:
#                 x = 'ขอผลิตภัณฑ์รวม'
#                 line_bot_api2.reply_message(event.reply_token, productR4())
#                 inserted = get_datetime(x, line_bot_api2)
#                 db2.child('chatbot_transactions').push(inserted)
#             elif ['@mango'] == result[3]:
#                 line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{result[4]}'))
#             elif ['ฉันชื่ออะไร'] == result[3]:
#                 profile = line_bot_api2.get_profile(result[4])
#                 user_profile = profile.display_name
#                 user_profile = str(user_profile)
#                 line_bot_api2.reply_message(event.reply_token,
#                                             TextSendMessage(text=f'เอ้า! ลืมชื่อตัวเองแล้วหรอ ก็ {user_profile} ไง'))
#             elif ['ขอ Demo'] == result[3]:
#                 line_bot_api2.reply_message(event.reply_token,
#                                             TextSendMessage(text='สวัสดีค่ะ แอดมินขออภัยในความไม่สะดวกนะคะ '
#                                                                  'ทางบริษัทจะไม่มีตัว Demo ให้ทดลองใช้ แต่จะเป็นการนัดเข้าไป '
#                                                                  'Demo เพื่อพรีเซนต์รายละเอียดโปรแกรมค่ะ หากต้องการให้ทีมงานเข้าไป '
#                                                                  'Demo โปรแกรม กรุณาโทร. 063-565-4594 ติดต่อคุณเมทิกา นะคะขอบคุณค่ะ'))
#             elif ['มาก'] == result[3]:
#                 x = 'มาก'
#                 line_bot_api2.reply_message(event.reply_token, TextSendMessage(text='น้อย'))
#                 inserted = get_datetime(x, line_bot_api2)
#                 db2.child('chatbot_transactions').push(inserted)
#             elif ['น้อย'] == result[3]:
#                 x = 'น้อย'
#                 line_bot_api2.reply_message(event.reply_token, TextSendMessage(text='มาก'))
#                 inserted = get_datetime(x, line_bot_api2)
#                 db2.child('chatbot_transactions').push(inserted)
#             elif whatever:
#                 x = ['นั้นสินะ', 'อิหยังวะ', 'ว่า']
#                 z = random.choice(x)
#                 line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{z}'))
#             elif ['ชื่อไร'] == result[3]:
#                 x = ['แมงโก้ค่ะ', 'น้องแมงโก้']
#                 z = random.choice(x)
#                 line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{z}'))
#                 inserted = get_datetime(z, line_bot_api2)
#                 db2.child('chatbot_transactions').push(inserted)
#             elif ['เบอร์ติดต่อ Info'] == result[3]:
#                 x = ["สามารถติต่อ Call Center : 02-123-3900\nหรือ Email : info@mangoconsultant.com 😉"]
#                 z = random.choice(x)
#                 line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{z}'))
#             else:
#                 if result[2] == [3]:
#                     profile = line_bot_api2.get_profile(result[4])
#                     displayName = profile.display_name
#                     x = f'สวัสดีค่ะ น้องแมงโก้เป็นระบบโต้ตอบอัตโนมัติ\nคุณ {displayName} สามารถเลือกเมนูด้านล่างหรือพิมพ์สอบถามได้เลยนะคะ'
#                     quick_reply(event, x, QuickReply=QuickReply(items=[
#                         QuickReplyButton(action=MessageAction(label='ผลิตภัณฑ์แมงโก้', text='ผลิภัณฑ์แมงโก้')),
#                         QuickReplyButton(action=MessageAction(label='โปรโมชั่น', text='โปรโมชั่น')),
#                         QuickReplyButton(action=MessageAction(label='ขอใบเสนอราคา', text='ขอใบเสนอราคา')),
#                         QuickReplyButton(action=MessageAction(label='สอบถามการอบรม', text='สอบถามการอบรม')),
#                         QuickReplyButton(action=MessageAction(label='สอบถามการใช้งาน', text='สอบถามการใช้งาน'))
#                     ]))
#                 elif result[2] == [5]:
#                     x = random.choice(result[1][int(result[2])])
#                     quick_reply(event, x, QuickReply=QuickReply(items=[
#                         QuickReplyButton(action=MessageAction(label='ขอข้อมูลผลิตภัณฑ์', text='ขอข้อมูลผลิตภัณฑ์')),
#                         QuickReplyButton(action=MessageAction(label='ขอใบเสนอราคา', text='ขอใบเสนอราคา')),
#                         QuickReplyButton(action=MessageAction(label='สอบถามปัญหาโปรแกรม', text='สอบถามปัญหาโปรแกรม')),
#                         QuickReplyButton(action=MessageAction(label='เบอร์ติดต่อ Info', text='เบอร์ติดต่อ Info'))
#                     ]))
#                     inserted = get_datetime(x, line_bot_api2)
#                     db2.child('chatbot_transactions').push(inserted)
#                 elif result[2] == [6]:
#                     x = random.choice(result[1][int(result[2])])
#                     quick_reply(event, x, QuickReply=QuickReply(items=[
#                         QuickReplyButton(action=MessageAction(label='โปรโมชั่น', text='โปรโมชั่น'))
#                     ]))
#                     inserted = get_datetime(x, line_bot_api2)
#                     db2.child('chatbot_transactions').push(inserted)
#                 elif result[2] == [12]:
#                     x = 'ดูดวง'
#                     line_bot_api2.push_message(result[4], flex_destiny())
#                     line_bot_api2.push_message(result[4], destiny())
#                     inserted = get_datetime(x, line_bot_api2)
#                     db2.child('chatbot_transactions').push(inserted)
#                 elif result[2] == [13]:
#                     x = random.choice(result[1][int(result[2])])
#                     quick_reply(event, x, QuickReply=QuickReply(items=[
#                         QuickReplyButton(action=MessageAction(label="ชื่ออะไร", text="ชื่ออะไร")),
#                         QuickReplyButton(action=MessageAction(label="ดูดวง", text="ดูดวง")),
#                         QuickReplyButton(action=MessageAction(label="ข่าว ทั่วไป", text="ข่าว ทั่วไป")),
#                         QuickReplyButton(action=MessageAction(label="ข่าว บันเทิง", text="ข่าว บันเทิง")),
#                         QuickReplyButton(action=MessageAction(label="ข่าว กีฬา", text="ข่าว กีฬา")),
#                         QuickReplyButton(action=CameraAction(label="Camera"))
#                     ]))
#                 elif result[2] == [7]:
#                     stick = ['51626520', '51626526']
#                     pack = 11538
#                     integrate_send(model_linebot_new(), event, pack, stick, line_bot_api2)
#                 elif result[2] == [2]:
#                     x = 'flex โปรแกรม'
#                     line_bot_api2.push_message(result[4], flex_product())
#                     get_datetime(x, line_bot_api2)
#                 elif result[2] == [1]:
#                     x = random.choice(result[1][int(result[2])])
#                     line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
#                     image_message = ImageSendMessage(
#                         original_content_url='https://sv1.picz.in.th/images/2020/10/21/bBc4NI.png',
#                         preview_image_url='https://sv1.picz.in.th/images/2020/10/21/bBc4NI.png'
#                     )
#                     line_bot_api2.push_message(result[4], image_message)
#                     inserted = get_datetime(x, line_bot_api2)
#                     db2.child('chatbot_transactions').push(inserted)
#                 elif result[2] == [10]:
#                     x = 'ขออภัยในความไม่สะดวกนะคะ\n\nช่องทางนี้สำหรับแนะนำผลิตภัณฑ์และประชาสัมพันธ์ข่าวสาร ค่ะ\n' \
#                         'กรณีที่ลูกค้าติดปัญหาการใช้งานแนะนำให้ติดต่อฝ่าย Customer Service\n' \
#                         'โทร. 02-937-1601-9 ต่อ 603 Call Center 02-123-3900\n' \
#                         'มีทีมงานผู้เชี่ยวชาญคอยให้คำปรึกษาเฉพาะด้าน มีระบบบันทึกเสียงและเก็บบันทึกข้อมูลปัญหาของลูกค้าค่ะ\n' \
#                         'หากต้องการส่งรูปภาพ สามารถส่งได้ทาง Email : info@mangoconsultant.com\n\n' \
#                         'นอกจากนี้ยังสามารถ เข้าตรวจสอบหน้าจอการทำงาน ของลูกค้าผ่าน TeamViewer ได้อีกด้วย\nขออภัยในความไม่สะดวกนะคะ ขอบคุณค่ะ'
#                     quick_reply(event, x, QuickReply=QuickReply(items=[
#                         QuickReplyButton(action=MessageAction(label='ขอข้อมูลผลิตภัณฑ์', text='ขอข้อมูลผลิตภัณฑ์')),
#                         QuickReplyButton(action=MessageAction(label='โปรโมชั่น', text='โปรโมชั่น'))
#                     ]))
#                     inserted = get_datetime(x, line_bot_api2)
#                     db2.child('chatbot_transactions').push(inserted)
#                 elif result[2] == [11]:
#                     x = 'Template Image'
#                     line_bot_api2.push_message(result[4], productR7())
#                     inserted = get_datetime(x, line_bot_api2)
#                     db2.child('chatbot_transactions').push(inserted)
#                 elif result[2] == [18]:
#                     x = random.choice(result[1][int(result[2])])
#                     quick_reply(event=event, x=x, QuickReply=QuickReply(items=[
#                         QuickReplyButton(action=MessageAction(label='ขอข้อมูลผลิตภัณฑ์', text='ขอข้อมูลผลิตภัณฑ์')),
#                         QuickReplyButton(action=MessageAction(label='โปรโมชั่น', text='โปรโมชั่น')),
#                         QuickReplyButton(action=MessageAction(label='ขอใบเสนอราคา', text="ขอใบเสนอราคา"))
#                     ]))
#                     inserted = get_datetime(x, line_bot_api2)
#                     db2.child('chatbot_transactions').push(inserted)
#                 elif result[2] == [19]:
#                     day = datetime.today().day
#                     month = datetime.today().month
#                     second = datetime.today().second
#                     minute = datetime.today().minute
#                     hour = datetime.today().hour
#                     year = datetime.today().year
#                     x = 'วันนี้วันที่ {}/{}/{} เวลา {}:{}:{}'.format(day, month, year, hour, minute, second)
#                     line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
#                     inserted = get_datetime(x, line_bot_api2)
#                     db2.child('chatbot_transactions').push(inserted)
#                 elif result[2] == [20]:
#                     x = WebScraping.humility()
#                     quick_reply(event=event, x=x, QuickReply=QuickReply(items=[
#                         QuickReplyButton(action=MessageAction(label='ข่าวทั่วไป', text='ข่าว ทั่วไป')),
#                         QuickReplyButton(action=MessageAction(label='ข่าวบันเทิง', text='ข่าว บันเทิง')),
#                         QuickReplyButton(action=MessageAction(label='ข่าวกีฬา', text='ข่าว กีฬา'))
#                     ]))
#                     inserted = get_datetime(x, line_bot_api2)
#                     db2.child('chatbot_transactions').push(inserted)
#                 elif result[2] == [21]:
#                     if result[3] == ['ข่าว']:
#                         x = WebScraping.new_common()
#                         line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
#                         line_bot_api2.push_message(result[4], TextSendMessage(
#                             text='ดูข่าวเพิ่มเติมลิงค์นี้เลย\nhttps://www.thairath.co.th/news/local'))
#                         line_bot_api2.push_message(result[4], TextSendMessage(
#                             text='และยังสามารถพิมพ์ ข่าว เว้นวรรค ตามด้วยข่าวที่ต้องการได้ค่ะ\nเช่น ข่าว ทั่วไป, ข่าว กีฬา, ข่าว บันเทิง'))
#                     else:
#                         i = ''
#                         k = result[3]
#                         p = i.join(k)
#                         x = p.split('ข่าว')
#                         tranform = ''
#                         ans = tranform.join(x)
#                         print('string >: ', ans)
#                         if ans == ' ทั่วไป':
#                             x = WebScraping.new_common()
#                             line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
#                             line_bot_api2.push_message(result[4], TextSendMessage(
#                                 text='ดูข่าวเพิ่มเติมลิงค์นี้เลย\nhttps://www.thairath.co.th/news/local'))
#                             line_bot_api2.push_message(result[4], TextSendMessage(
#                                 text='และยังสามารถพิมพ์ ข่าว เว้นวรรค ตามด้วยข่าวที่ต้องการได้ค่ะ\nเช่น ข่าว ทั่วไป, ข่าว กีฬา, ข่าว บันเทิง'))
#                             inserted = get_datetime(x, line_bot_api2)
#                             db2.child('chatbot_transactions').push(inserted)
#                         elif ans == ' กีฬา':
#                             x = WebScraping.new_sport()
#                             line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
#                             line_bot_api2.push_message(result[4], TextSendMessage(
#                                 text='ดูข่าวเพิ่มเติมลิงค์นี้เลย\nhttps://www.thairath.co.th/sport'))
#                             line_bot_api2.push_message(result[4], TextSendMessage(
#                                 text='และยังสามารถพิมพ์ ข่าว เว้นวรรค ตามด้วยข่าวที่ต้องการได้ค่ะ\nเช่น ข่าว ทั่วไป, ข่าว กีฬา, ข่าว บันเทิง'))
#                             inserted = get_datetime(x, line_bot_api2)
#                             db2.child('chatbot_transactions').push(inserted)
#                         elif ans == ' บันเทิง':
#                             x = WebScraping.new_entertain()
#                             line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
#                             line_bot_api2.push_message(result[4], TextSendMessage(
#                                 text='ดูข่าวเพิ่มเติมลิงค์นี้เลย\nhttps://www.thairath.co.th/entertain'))
#                             line_bot_api2.push_message(result[4], TextSendMessage(
#                                 text='และยังสามารถพิมพ์ ข่าว เว้นวรรค ตามด้วยข่าวที่ต้องการได้ค่ะ\nเช่น ข่าว ทั่วไป, ข่าว กีฬา, ข่าว บันเทิง'))
#                             inserted = get_datetime(x, line_bot_api2)
#                             db2.child('chatbot_transactions').push(inserted)
#                 elif result[2] == [22]:
#                     x = 'Software ERP Mango Anywhere จะทำงานอยู่บน 3 platform\n\n' \
#                         '1.Window\n2.On Web\n3.Application\n\nในส่วนของ Application จะไม่ได้ครอบคลุมการทำงานทั้งหมดโดยเราได้พัฒนา' \
#                         'Application เพื่อตอบสนองการทำงานของลูกค้าในบางส่วนสามารถดูตัวอย่าง Application ได้จากลิงค์นี้ค่ะ https://youtu.be/0e-bm5UMlL4'
#                     quick_reply(event, x, QuickReply=QuickReply(items=[
#                         QuickReplyButton(action=MessageAction(label='ผลิตภัณฑ์แมงโก้', text='ผลิตภัณฑ์แมงโก้'))
#                     ]))
#                     inserted = get_datetime(x, line_bot_api2)
#                     db2.child('chatbot_transactions').push(inserted)
#                 elif result[2] == [23]:
#                     x = 'flex โปรโมชั่น'
#                     line_bot_api2.reply_message(event.reply_token, promotion())
#                     inserted = get_datetime(x, line_bot_api2)
#                     db2.child('chatbot_transactions').push(inserted)
#                 elif areSure:
#                     x = ['จ้า', 'ใช่จ้า', 'จริงสิ']
#                     y = random.choice(x)
#                     line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{y}'))
#                 else:
#                     x = random.choice(result[1][int(result[2])])
#                     line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
#                     q_a = get_datetime(x, line_bot_api2)
#                     inserted = db2.child('chatbot_transactions').push(q_a)
#                     print(f'Inserted : {inserted}')
#         else:
#             if ['สวัสดีจ่ะ'] == result[3]:
#                 profile = line_bot_api2.get_profile(result[4])
#                 displayName = profile.display_name
#                 x = f'สวัสดีค่ะ น้องแมงโก้เป็นระบบโต้ตอบอัตโนมัติ\nคุณ {displayName} สามารถเลือกเมนูด้านล่างหรือพิมพ์สอบถามได้เลยนะคะ'
#                 quick_reply(event, x, QuickReply=QuickReply(items=[
#                     QuickReplyButton(action=MessageAction(label="ผลิตภัณฑ์แมงโก้", text="ผลิภัณฑ์แมงโก้")),
#                     QuickReplyButton(action=MessageAction(label="โปรโมชั่น", text="โปรโมชั่น")),
#                     QuickReplyButton(action=MessageAction(label="ขอใบเสนอราคา", text="ขอใบเสนอราคา")),
#                     QuickReplyButton(action=MessageAction(label="สอบถามการอบรม", text="สอบถามการอบรม")),
#                     QuickReplyButton(action=MessageAction(label="สอบถามการใช้งาน", text="สอบถามการใช้งาน"))
#                 ]))
#             elif ['temp'] == result[3]:
#                 temp = db2.child('Sensor Ultrasonic').get()
#                 temp = temp.val()
#                 line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'Temperature {temp} C'))
#             elif mango:
#                 z = ['ยินดีให้บิรการค่า', 'อาการมันเป็นยังไงไหนบอกแมงโก้สิ', 'ว่าไงจ๊ะ']
#                 x = random.choice(z)
#                 line_bot_api2.reply_message(event.reply_token, TextSendMessage(text='{}'.format(x)))
#                 inserted = get_datetime(x, line_bot_api2)
#                 db2.child('chatbot_transactions').push(inserted)
#             elif ['น้อย'] == result[3]:
#                 line_bot_api2.reply_message(event.reply_token, TextSendMessage(text='มาก'))
#             elif ['ผลิตภัณฑ์แมงโก้'] == result[3]:
#                 x = 'ผลิตภัณฑ์แมงโก้'
#                 line_bot_api2.reply_message(event.reply_token, productR7())
#                 inserted = get_datetime(x, line_bot_api2)
#                 db2.child('chatbot_transactions').push(inserted)
#             elif ['event'] == result[3]:
#                 profile = line_bot_api2.get_profile(result[4])
#                 displayName = profile.display_name
#                 img = profile.picture_url
#                 line_bot_api2.reply_message(event.reply_token, flex_event(img, displayName))
#                 x = 'Event'
#                 inserted = get_datetime(x, line_bot_api2)
#                 db2.child('chatbot_transactions').push(inserted)
#             elif ['Event'] == result[3]:
#                 profile = line_bot_api2.get_profile(result[4])
#                 displayName = profile.display_name
#                 img = profile.picture_url
#                 line_bot_api2.reply_message(event.reply_token, flex_event(img, displayName))
#                 x = 'Event'
#                 inserted = get_datetime(x, line_bot_api2)
#                 db2.child('chatbot_transactions').push(inserted)
#             elif ['@Promotion'] == result[3]:
#                 x = '@Promotion'
#                 line_bot_api2.reply_message(event.reply_token, promotion())
#                 inserted = get_datetime(x, line_bot_api2)
#                 db2.child('chatbot_transactions').push(inserted)
#             elif ['@ERPSoftware'] == result[3]:
#                 x = '@ERPSoftware'
#                 line_bot_api2.reply_message(event.reply_token, flex_product())
#                 inserted = get_datetime(x, line_bot_api2)
#                 db2.child('chatbot_transactions').push(inserted)
#             elif ['@NewFeature'] == result[3]:
#                 x = '@NewFeature'
#                 line_bot_api2.reply_message(event.reply_token, flex_newfeature())
#                 inserted = get_datetime(x, line_bot_api2)
#                 db2.child('chatbot_transactions').push(inserted)
#             elif ['@Optional'] == result[3]:
#                 x = '@optional'
#                 line_bot_api2.reply_message(event.reply_token, flex_optional())
#                 inserted = get_datetime(x, line_bot_api2)
#                 db2.child('chatbot_transactions').push(inserted)
#             elif ['@Business'] == result[3]:
#                 x = '@Business'
#                 line_bot_api2.reply_message(event.reply_token, flex_bus())
#                 inserted = get_datetime(x, line_bot_api2)
#                 db2.child('chatbot_transactions').push(inserted)
#             elif ['วาดรูป'] == result[3]:
#                 line_bot_api2.reply_message(event.reply_token,
#                                             TextSendMessage(text='https://liff.line.me/1655104822-L5Ob5XdD'))
#             elif ['promotion'] == result[3]:
#                 line_bot_api2.reply_message(event.reply_token, promotion())
#             elif ['profile'] == result[3]:
#                 profile = line_bot_api2.get_profile(result[4])
#                 displayName = profile.display_name
#                 picture_url = profile.picture_url
#                 user_id = profile.user_id
#                 status = profile.status_message
#                 print(displayName, picture_url, user_id, status)
#                 line_bot_api2.push_message(result[4], flex_profile_erp(picture_url, displayName, status))
#             else:
#                 profile = line_bot_api2.get_profile(result[4])
#                 displayName = profile.display_name
#                 text_message = TextSendMessage(
#                     text=f'น้องแมงโก้ไม่แน่ใจ คุณ {displayName} ลองถามคำถามใหม่ อีกครั้ง เช่น ขอใบเสนอราคายังไง\n\n'
#                          'หรือเลือกเรื่องที่ต้องการสอบถาม เจ้าหน้าที่จะมาดูแลต่อนะคะ',
#                     quick_reply=QuickReply(items=[
#                         QuickReplyButton(action=MessageAction(label="ขอข้อมูลผลิตภัณฑ์", text="ขอข้อมูลผลิตภัณฑ์")),
#                         QuickReplyButton(action=MessageAction(label='ขอใบเสนอราคา', text='ขอใบเสนอราคาทำอย่างไร')),
#                         QuickReplyButton(
#                             action=MessageAction(label='ลูกค้าที่ใช้งานโปรแกรม', text='ลูกค้าที่ใช้งานโปรแกรม')),
#                         QuickReplyButton(action=MessageAction(label='ราคาโปรแกรม', text='ราคาโปรแกรม')),
#                         QuickReplyButton(action=MessageAction(label='ติดปัญหาการใช้งาน', text='ติดปัญหาการใช้งาน')),
#                         QuickReplyButton(
#                             action=MessageAction(label='ติดต่ออบรมประจำเดือน', text='ติดต่ออบรมประจำเดือน')),
#                         QuickReplyButton(action=MessageAction(label='ติดต่อขอฝึกงาน', text='ติดต่อขอฝึกงาน')),
#                     ]))
#                 line_bot_api2.push_message(result[4], text_message)
#                 x = 'ไม่เข้าใจ'
#                 inserted = get_datetime(x, line_bot_api2)
#                 db2.child('chatbot_transactions').push(inserted)
#     except LineBotApiError:
#         abort(400)
#
#
# @handler3.add(MessageEvent, message=TextMessage)
# def handle_message_old(event):
#     result = model_linebot_old()
#     print(result[0])
#     try:
#         if result[0] >= 0.14367:
#             if ['ขอข้อมูลผลิตภัณฑ์'] == result[3]:
#                 x = 'card'
#                 line_bot_api3.reply_message(event.reply_token, mangoerp())
#                 inserted = get_datetime(x, line_bot_api3)
#                 db3.child('chatbot_transactions').push(inserted)
#             elif ['@mango'] == result[3]:
#                 line_bot_api3.reply_message(event.reply_token, TextSendMessage(text=f'{result[4]}'))
#             elif ['ฉันชื่ออะไร'] == result[3]:
#                 profile = line_bot_api3.get_profile(result[4])
#                 user_profile = profile.display_name
#                 user_profile = str(user_profile)
#                 line_bot_api3.reply_message(event.reply_token,
#                                             TextSendMessage(text=f'เอ้า! ลืมชื่อตัวเองแล้วหรอ ก็ {user_profile} ไง'))
#             else:
#                 x = random.choice(result[1][int(result[2])])
#                 line_bot_api3.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
#                 q_a = get_datetime(x, line_bot_api3)
#                 inserted = db3.child('chatbot_transactions').push(q_a)
#                 print(f'Inserted : {inserted}')
#         else:
#             if ['เปิดไฟ'] == result[3]:
#                 line_bot_api3.reply_message(event.reply_token, TextSendMessage(text=f'โอเคจ้า ทำการเปิดไฟ'))
#                 db3.child('Node1').update({'Relay1': 0})
#             elif ['ปิดไฟ'] == result[3]:
#                 line_bot_api3.reply_message(event.reply_token, TextSendMessage(text=f'โอเคจ้า ทำการปิดไฟ'))
#                 db3.child('Node1').update({'Relay1': 1})
#             elif ['temp'] == result[3]:
#                 temp = db3.child('Sensor Ultrasonic').get()
#                 temp = temp.val()
#                 line_bot_api3.reply_message(event.reply_token, TextSendMessage(text=f'Temperature {temp} C'))
#     except LineBotApiError:
#         abort(400)
#
#
# @app.route('/api/richmenu/<string:rich>', methods=['GET', 'POST'])
# def richmenu(rich):
#     with open('richmenu.json', encoding='utf8') as w:
#         data = json.load(w)
#         rich_id = data['id']
#     if rich == 'create':
#         rich_menu_to_create = RichMenu(
#             size=RichMenuSize(width=2500, height=1686),
#             selected=False,
#             name="Nice richmenu",
#             chat_bar_text="Tap here",
#             areas=[RichMenuArea(
#                 bounds=RichMenuBounds(x=853, y=164, width=1615, height=232),
#                 action=URIAction(label='Go to line.me', uri='https://line.me')),
#                 RichMenuArea(
#                     bounds=RichMenuBounds(x=155, y=353, width=598, height=414),
#                     action=MessageAction(label='text', text='hey')
#                 )
#             ]
#         )
#         rich_menu_id = line_bot_api1.create_rich_menu(rich_menu=rich_menu_to_create)
#         txt = {'id': rich_menu_id}
#         print(txt)
#         with open('richmenu.json', 'w') as r:
#             json.dump(txt, r)
#         return jsonify(txt)
#     elif rich == 'uploadimg':
#         with open('ProductThumb_45569_67700481_resize.jpg', 'rb') as f:
#             line_bot_api1.set_rich_menu_image('richmenu-455e1d928c3b906515a05598ba745772', 'image/jpeg', f)
#             print(f'rich_id : {rich_id}')
#         return 'ok'
#     elif rich == 'set':
#         line_bot_api1.set_default_rich_menu('richmenu-455e1d928c3b906515a05598ba745772')
#         return 'ok'
#     elif rich == 'get_id':
#         pass
#     elif rich == 'deleteall':
#         rich_menu_list = line_bot_api1.get_rich_menu_list()
#         for rich_menu in rich_menu_list:
#             richz = rich_menu.rich_menu_id
#             line_bot_api1.delete_rich_menu(str(richz))
#             print(richz)
#         return str('ok')
#     elif rich == 'list':
#         tx = []
#         rich_menu_list = line_bot_api1.get_rich_menu_list()
#         for rich_menu in rich_menu_list:
#             richz = rich_menu.rich_menu_id
#             tx.append(richz)
#         print(tx)
#         return str(tx)
#     elif rich == 'link_rich':
#         line_bot_api1.delete_rich_menu('richmenu-3202e3f39315170a26bf8deca4703e95')
#         return 'ok'
#
#
# if __name__ == '__main__':
#     app.run(debug=True, port=5005)


