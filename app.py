from flask import Flask, request, abort, render_template, jsonify, json, redirect, url_for, session, flash, g
import pyrebase
from datetime import datetime, timedelta
import firebase_admin
from firebase_admin import credentials, auth
import json
import time
from random import randrange
from numpy import random
from mangoerp.mangoerp_card import mangoerp
from mangoerp.flex_message import *
from model.model_linebot import model_linebot, model_linebot_old, model_linebot_new, get_datetime1, get_datetime2, get_datetime3
import numpy as np
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError, LineBotApiError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            ImageSendMessage, StickerSendMessage, AudioSendMessage, FlexSendMessage,
                            ImagemapSendMessage,
                            BaseSize, URIImagemapAction, ImagemapArea, QuickReply, QuickReplyButton, MessageAction)

cred = credentials.Certificate('config/database_test/authen_firebase.json')
firebase_auth = firebase_admin.initialize_app(cred)

def database_test():
    with open('config/database_test/firebase.json', encoding='utf8') as json_file:
        data = json.load(json_file)
        config = data['firebase']
        firebase = pyrebase.initialize_app(config)
        pb = pyrebase.initialize_app(config)
        db = firebase.database()
        line_bot_api = LineBotApi(data['Channel_access_token'])
        handler = WebhookHandler(data['Channel_secret'])
    return db, line_bot_api, handler, pb


def database_new():
    with open('config/database_new/firebase.json', encoding='utf8') as json_file:
        data = json.load(json_file)
        config = data['firebase']
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        line_bot_api = LineBotApi(data['Channel_access_token'])
        handler = WebhookHandler(data['Channel_secret'])
    return db, line_bot_api, handler


def database_older():
    with open('config/database_older/firebase.json', encoding='utf8') as json_file:
        data = json.load(json_file)
        config = data['firebase']
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        line_bot_api = LineBotApi(data['Channel_access_token'])
        handler = WebhookHandler(data['Channel_secret'])
    return db, line_bot_api, handler


data_test = database_test()
db1 = data_test[0]
line_bot_api1 = data_test[1]
handler1 = data_test[2]
pb = data_test[3]

data_new = database_new()
db2 = data_new[0]
line_bot_api2 = data_new[1]
handler2 = data_new[2]

data_older = database_older()
db3 = data_older[0]
line_bot_api3 = data_older[1]
handler3 = data_older[2]


app = Flask(__name__)
app.secret_key = 'watcharaponweeraborirakz'


@app.before_request
def before_request():
    try:
        login = db1.child('id').get()
        for l in login.each():
            id = l.val()['email']
            if 'user_id' in session:
                user = session['user_id'] == id
                g.user = id
            else:
                g.user = None
    except:
        print("error login")


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=13)


@app.route('/test')
def test():
    resp = make_session_permanent(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp


@app.route('/lg/<string:customer>', methods=['GET', 'POST'])
def login(customer):
    error = 'Invalid credentials. Please try again. '
    if request.path == '/lg/new':
        if g.user:
            return redirect(url_for('index_newcustomer'))
    elif request.path == '/lg/old':
        if g.user:
            return redirect(url_for('index_customer'))
    user = None
    new_customer = {'customer': 'new'}
    old_customer = {'customer': 'old'}
    c_result = [new_customer, old_customer]
    if request.method == 'GET':
        for i in c_result:
            if i['customer'] == customer:
                print(f'found: {i}')
                user = i
                break
        if request.path == '/lg/new':
            data = {
                'user': user,
                'customer': 'New Customer'
            }
            return render_template('/sbadmin/login.html', data=data)
        elif request.path == '/lg/old':
            data = {
                'user': user,
                'customer': 'Customer',
            }
            return render_template('/sbadmin/login.html', data=data)
    if request.method == 'POST':
        error = 'Invalid credentials. Please try again. '
        if request.path == '/lg/new':
            session.pop('user_id', None)
            user = request.form['username']
            password = request.form['password']
            login = db1.child('id').get()
            for l in login.each():
                id = l.val()['email']
                try:
                    login = pb.auth().sign_in_with_email_and_password(user, password)
                    with open('login_json.json', 'w') as json_login:
                        json.dump(login, json_login)
                    session['user_id'] = id
                    flash('You were successfully logged in')
                    print('ok')
                    return redirect(url_for('index_newcustomer'))
                except:
                    data = {
                        'user': user,
                        'customer': 'Customer',
                        'error': error
                    }
                    return render_template('/sbadmin/login.html', data=data)
        elif request.path == '/lg/old':
            session.pop('user_id', None)
            user = request.form['username']
            password = request.form['password']
            login = db1.child('id').get()
            for l in login.each():
                id = l.val()['email']
                try:
                    login = pb.auth().sign_in_with_email_and_password(user, password)
                    with open('login_json.json', 'w') as json_login:
                        json.dump(login, json_login)
                    session['user_id'] = id
                    flash('You were successfully logged in')
                    print('ok')
                    return redirect(url_for('index_customer'))
                except:
                    data = {
                        'user': user,
                        'customer': 'Customer',
                        'error': error
                    }
                    return render_template('/sbadmin/login.html', data=data)
    return render_template('/sbadmin/login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('welcome'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        error = 'Please fill in all information.'
        confirm_error = 'Passwords do not match.'
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        confirm_pwd = request.form['confirmpwd']
        if password != confirm_pwd:
            return render_template('/sbadmin/signup.html', error=confirm_error)
        if email is None or password is None or first_name is None or last_name is None:
            return render_template('/sbadmin/signup.html', error=error)
        try:
            user = auth.create_user(email=email, password=password)
            day = datetime.today().day
            month = datetime.today().month
            second = datetime.today().second
            minute = datetime.today().minute
            hour = datetime.today().hour
            year = datetime.today().year
            data = {'firstname': first_name, 'lastname': last_name, 'email': user.email, 'userToken': user.uid,
                    'Datetime': {'day': day, 'month': month, 'year': year, 'hour': hour, 'minute': minute, 'second': second}}
            db1.child('id').push(data)
            return redirect(url_for('welcome'))
        except:
            return render_template('/sbadmin/signup.html', error=error)
        return render_template('/sbadmin/signup.html')
    return render_template('/sbadmin/signup.html')


@app.route('/setting')
def settingPage():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('/sbadmin/setting.html')


@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'POST':
        forgot = request.form['email']
        try:
            pb.auth().send_password_reset_email(forgot)
            return render_template('/sbadmin/forgot.html', error='Please check your email verify reset password.')
        except:
            return render_template('/sbadmin/forgot.html', error='error')
    return render_template('/sbadmin/forgot.html')


@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template('/sbadmin/welcome.html')


@app.route('/admin_index')
def index():
    return render_template('/sbadmin/index.html')


@app.route('/index_new_customer')
def index_newcustomer():
    if not g.user:
        return redirect(url_for('welcome'))
    user = g.user
    return render_template('/customers_new/index.html', user=user)


@app.route('/index_customer')
def index_customer():
    if not g.user:
        return redirect(url_for('welcome'))
    return render_template('/customers_old/index.html')


@app.route('/intent/<string:id>', methods=['GET', 'POST'])
def intent(id):
    data = {
        'id': id,
    }
    return render_template('/sbadmin/intent.html', data=data)


@app.route('/new_intent/<string:id>', methods=['GET', 'POST'])
def new_intent(id):
    if not g.user:
        return redirect(url_for('login'))
    data = {
        'id': id,
    }
    return render_template('/customers_new/intent.html', data=data)


@app.route('/c_intent/<string:id>', methods=['GET', 'POST'])
def old_intent(id):
    if not g.user:
        return redirect(url_for('login'))
    data = {
        'id': id,
    }
    return render_template('/customers_old/intent.html', data=data)

@app.route('/chart', methods=['GET', 'POST'])
def chart():
    ref = db1.child('customer_email').get()
    lst = []
    count = 0
    for r in ref.each():
        users = r.val()
        users = dict(users)
        users.update({'index': str(count)})
        lst.append(users)
        count = count + 1
    _id = len(lst)
    data = {
        'users': lst,
        'msg': _id
    }
    if request.method == 'POST':
        broadcast = request.form['msg']
        line_bot_api1.broadcast(TextSendMessage(text=str(broadcast)))
        return redirect(url_for('chart'))
    return render_template('/sbadmin/charts.html', data=data)



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
        try:
            postback = decoded['events'][0]['type']
            data = decoded['events'][0]['postback']['data']
            if postback == 'postback':
                no_event = len(decoded['events'])
                for i in range(no_event):
                    event = decoded['events'][i]
                    event_handler(event)
        except:
            _type = decoded['events'][0]['message']['type']
            if _type == 'text':
                txt = decoded['events'][0]['message']['text']
                print(txt)
                try:
                    handler1.handle(body, signature)
                except InvalidSignatureError:
                    abort(400)
            else:
                no_event = len(decoded['events'])
                for i in range(no_event):
                    event = decoded['events'][i]
                    event_handler(event)
    return 'ok'


@app.route('/webhookNew', methods=['GET', 'POST'])
def webhookNew():
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
                handler2.handle(body, signature)
            except InvalidSignatureError:
                abort(400)
        else:
            no_event = len(decoded['events'])
            for i in range(no_event):
                event = decoded['events'][i]
                event_handler1(event)
        return ''


@app.route('/webhookOld', methods=['GET', 'POST'])
def webhookOld():
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
                handler3.handle(body, signature)
            except InvalidSignatureError:
                abort(400)
        else:
            no_event = len(decoded['events'])
            for i in range(no_event):
                event = decoded['events'][i]
                event_handler2(event)
        return ''


def event_handler(event):
    postback = event['type']
    rtoken = event['replyToken']
    try:
        data = event['postback']['data']
        if postback == 'postback':
            if data == 'more':
                print('...........')
                line_bot_api1.reply_message(rtoken, flex_msg())
            else:
                pass
    except:
        _type = event['message']['type']
        img = event['message']['id']
        sk_id = randrange(51626494, 51626533)
        if _type == 'sticker':
            replyObj = StickerSendMessage(package_id=str(11538), sticker_id=str(sk_id))
            line_bot_api1.reply_message(rtoken, replyObj)
        else:
            print(img)
            message_content = line_bot_api1.get_message_content(img)
            with open('img/file_path.png', 'wb') as fb:
                for chunk in message_content.iter_content():
                    fb.write(chunk)


def event_handler1(event):
    rtoken = event['replyToken']
    _type = event['message']['type']
    img = event['message']['id']
    sk_id = randrange(51626494, 51626533)
    if _type == 'sticker':
        replyObj = StickerSendMessage(package_id=str(11538), sticker_id=str(sk_id))
        line_bot_api2.reply_message(rtoken, replyObj)
    else:
        print(img)
        message_content = line_bot_api2.get_message_content(img)
        with open('img/file_path.png', 'wb') as fb:
            for chunk in message_content.iter_content():
                fb.write(chunk)


def event_handler2(event):
    rtoken = event['replyToken']
    _type = event['message']['type']
    img = event['message']['id']
    sk_id = randrange(51626494, 51626533)
    if _type == 'sticker':
        replyObj = StickerSendMessage(package_id=str(11538), sticker_id=str(sk_id))
        line_bot_api3.reply_message(rtoken, replyObj)
    else:
        print(img)
        message_content = line_bot_api3.get_message_content(img)
        with open('img/file_path.png', 'wb') as fb:
            for chunk in message_content.iter_content():
                fb.write(chunk)



@handler1.add(MessageEvent, message=TextMessage)
def handle_message(event):
    result = model_linebot()
    print(result[0])
    try:
        print('Result 1')
        if result[0] >= 0.14367:
            if ['ขอข้อมูลผลิตภัณฑ์'] == result[3]:
                x = 'card'
                line_bot_api1.reply_message(event.reply_token, mangoerp())
                inserted = get_datetime1(x)
                db1.child('chatbot_transactions').push(inserted)
            elif ['@mango'] == result[3]:
                line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'{result[4]}'))
            elif ['ฉันชื่ออะไร'] == result[3]:
                profile = line_bot_api1.get_profile(result[4])
                user_profile = profile.display_name
                img = profile.picture_url
                status = profile.status_message
                s = profile.language
                profile = str(profile)
                line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'เอ้า! ลืมชื่อตัวเองแล้วหรอ ก็ {user_profile} ไง'))
            else:
                x = random.choice(result[1][int(result[2])])
                line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
                q_a = get_datetime1(x)
                inserted = db1.child('chatbot_transactions').push(q_a)
                print(f'Inserted : {inserted}')
        else:
            if ['เปิดไฟ'] == result[3]:
                line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'โอเคจ้า ทำการเปิดไฟ'))
                db1.child('Node1').update({'Relay1': 0})
            elif ['ปิดไฟ'] == result[3]:
                line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'โอเคจ้า ทำการปิดไฟ'))
                db1.child('Node1').update({'Relay1': 1})
            elif ['ขอdemo'] == result[3]:
                line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'พิมพ์อีเมลของท่านเช่น email admin@user.com เป็นต้น\n เจ้าหน้าที่จะทำการติดต่อกลับไป'))
            elif ['@quote'] == result[3]:
                line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'พิมพ์คำว่า ใบเสนอราคา ตามด้วย ชื่อ,จำนวนผู้ใช้,เบอร์โทร หรือ อีเมล\nเช่น ใบเสนอราคา บอทแมงโก้  จำนวนผู้ใช้ 5 คน เบอร์ 08X-XXX-XXXX อีเมล info@mangoconsultant.com นะครับ'))
            elif ['temp'] == result[3]:
                temp = db1.child('Sensor Ultrasonic').get()
                temp = temp.val()
                line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'Temperature {temp} C'))
            elif ['test'] == result[3]:
                line_bot_api1.reply_message(event.reply_token, flex_erp())
    except LineBotApiError:
        abort(400)


@handler2.add(MessageEvent, message=TextMessage)
def handle_message(event):
    result = model_linebot_new()
    print(result[0])
    try:
        print('Result 2')
        if result[0] >= 0.14367:
            if ['ขอข้อมูลผลิตภัณฑ์'] == result[3]:
                x = 'card'
                line_bot_api2.reply_message(event.reply_token, mangoerp())
                inserted = get_datetime2(x)
                db2.child('chatbot_transactions').push(inserted)
            elif ['@mango'] == result[3]:
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{result[4]}'))
            elif ['ฉันชื่ออะไร'] == result[3]:
                profile = line_bot_api2.get_profile(result[4])
                user_profile = profile.display_name
                img = profile.picture_url
                status = profile.status_message
                s = profile.language
                profile = str(profile)
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'เอ้า! ลืมชื่อตัวเองแล้วหรอ ก็ {user_profile} ไง'))
            else:
                x = random.choice(result[1][int(result[2])])
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
                q_a = get_datetime2(x)
                inserted = db2.child('chatbot_transactions').push(q_a)
                print(f'Inserted : {inserted}')
        else:
            if ['เปิดไฟ'] == result[3]:
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'โอเคจ้า ทำการเปิดไฟ'))
                db2.child('Node1').update({'Relay1': 0})
            elif ['ปิดไฟ'] == result[3]:
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'โอเคจ้า ทำการปิดไฟ'))
                db2.child('Node1').update({'Relay1': 1})
            elif ['temp'] == result[3]:
                temp = db2.child('Sensor Ultrasonic').get()
                temp = temp.val()
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'Temperature {temp} C'))
            elif ['Intent'] == result[3]:
                x = 'flex message'
                line_bot_api2.reply_message(event.reply_token, flex_ans())
                inserted = get_datetime3(x)
                db3.child('chatbot_transactions').push(inserted)
            elif ['question?'] == result[3]:
                x = 'flex message'
                line_bot_api2.reply_message(event.reply_token, flex_msg())
                inserted = get_datetime3(x)
                db3.child('chatbot_transactions').push(inserted)
    except LineBotApiError:
        abort(400)


@handler3.add(MessageEvent, message=TextMessage)
def handle_message_old(event):
    result = model_linebot_old()
    print(result[0])
    try:
        print('Result 3')
        if result[0] >= 0.14367:
            if ['ขอข้อมูลผลิตภัณฑ์'] == result[3]:
                x = 'card'
                line_bot_api3.reply_message(event.reply_token, mangoerp())
                inserted = get_datetime3(x)
                db3.child('chatbot_transactions').push(inserted)
            elif ['@mango'] == result[3]:
                line_bot_api3.reply_message(event.reply_token, TextSendMessage(text=f'{result[4]}'))
            elif ['ฉันชื่ออะไร'] == result[3]:
                profile = line_bot_api3.get_profile(result[4])
                user_profile = profile.display_name
                img = profile.picture_url
                status = profile.status_message
                s = profile.language
                profile = str(profile)
                line_bot_api3.reply_message(event.reply_token, TextSendMessage(text=f'เอ้า! ลืมชื่อตัวเองแล้วหรอ ก็ {user_profile} ไง'))
            else:
                x = random.choice(result[1][int(result[2])])
                line_bot_api3.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
                q_a = get_datetime3(x)
                inserted = db3.child('chatbot_transactions').push(q_a)
                print(f'Inserted : {inserted}')
        else:
            if ['เปิดไฟ'] == result[3]:
                line_bot_api3.reply_message(event.reply_token, TextSendMessage(text=f'โอเคจ้า ทำการเปิดไฟ'))
                db3.child('Node1').update({'Relay1': 0})
            elif ['ปิดไฟ'] == result[3]:
                line_bot_api3.reply_message(event.reply_token, TextSendMessage(text=f'โอเคจ้า ทำการปิดไฟ'))
                db3.child('Node1').update({'Relay1': 1})
            elif ['temp'] == result[3]:
                temp = db3.child('Sensor Ultrasonic').get()
                temp = temp.val()
                line_bot_api3.reply_message(event.reply_token, TextSendMessage(text=f'Temperature {temp} C'))
            elif ['Intent'] == result[3]:
                x = 'flex message'
                line_bot_api3.reply_message(event.reply_token, flex_ans())
                inserted = get_datetime3(x)
                db3.child('chatbot_transactions').push(inserted)
            elif ['question?'] == result[3]:
                x = 'flex message'
                line_bot_api3.reply_message(event.reply_token, flex_msg())
                inserted = get_datetime3(x)
                db3.child('chatbot_transactions').push(inserted)

    except LineBotApiError:
        abort(400)


@app.route('/api/message/<string:msg>', methods=['GET', 'POST'])
def msg_message(msg):
    if request.method == 'POST':
        if msg == 'broadcast':
            try:
                raw_json = request.args['message']
                line_bot_api1.broadcast(TextSendMessage(text=str(raw_json)))
                return jsonify(f'Sending success : {raw_json}'), 200
            except:
                return jsonify(f'error'), 400



if __name__ == '__main__':
    app.run(debug=True, port=5005)
