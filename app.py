from flask import Flask, request, abort, render_template, jsonify, json, redirect, url_for, session, flash, g, \
    make_response, send_from_directory, send_file
import requests, json, uuid, cv2, time, os, warnings, pyrebase, firebase_admin, base64, xlsxwriter
from flask_bootstrap import Bootstrap
from datetime import datetime, timedelta
from random import randrange
from numpy import random
from bs4 import BeautifulSoup
import pandas as pd
from model_image import *
from PIL import Image
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn import svm
from attacut import tokenize
from datetime import datetime
from firebase_admin import credentials, auth
from mangoerp.mangoerp_card import *
from mangoerp.flex_message import *
from linebot.exceptions import (InvalidSignatureError, LineBotApiError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            StickerSendMessage, RichMenu, RichMenuArea, RichMenuBounds, RichMenuSize, RichMenuResponse)

warnings.simplefilter('error', Image.DecompressionBombWarning)

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'watcharaponweeraborirakz'

cred = credentials.Certificate('model/config/database_test/authen_firebase.json')
firebase_auth = firebase_admin.initialize_app(cred)


def database_test():
    with open('model/config/database_test/firebase.json', encoding='utf8') as json_file:
        data = json.load(json_file)
        config = data['firebase']
        firebase = pyrebase.initialize_app(config)
        pb = pyrebase.initialize_app(config)
        db = firebase.database()
        line_bot_api = LineBotApi(data['Channel_access_token'])
        handler = WebhookHandler(data['Channel_secret'])
    return db, line_bot_api, handler, pb


def database_new():
    with open('model/config/database_new/firebase.json', encoding='utf8') as json_file:
        data = json.load(json_file)
        config = data['firebase']
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        line_bot_api = LineBotApi(data['Channel_access_token'])
        handler = WebhookHandler(data['Channel_secret'])
    return db, line_bot_api, handler


def database_older():
    with open('model/config/database_older/firebase.json', encoding='utf8') as json_file:
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
    app.permanent_session_lifetime = timedelta(minutes=60)


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
                    'Datetime': {'day': day, 'month': month, 'year': year, 'hour': hour, 'minute': minute,
                                 'second': second}}
            db1.child('id').push(data)
            return redirect(url_for('welcome'))
        except:
            return render_template('/sbadmin/signup.html', error=error)

    return render_template('/sbadmin/signup.html')


@app.route('/setting')
def settingPage():
    if not g.user:
        return redirect(url_for('welcome'))
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


@app.route('/mango/<string:site>', methods=['GET', 'POST'])
def test(site):
    if request.path == '/mango/anywhere':
        lst = []
        product = {'product': ['Construction', 'RealEstate', 'Project Planning']}
        lst.append(product)
        return render_template('/sbadmin/testing.html', lst=lst)
    elif request.path == '/mango/rent':
        lst = []
        product = {'product': ['เช่าสุดคุ้ม']}
        lst.append(product)
        return render_template('/sbadmin/rent.html', lst=lst)
    return render_template('/sbadmin/testing.html')


@app.route('/letme', methods=['GET', 'POST'])
def letme():
    if request.method == 'POST':
        event = request.form.to_dict()
        day = datetime.today().day
        month = datetime.today().month
        second = datetime.today().second
        minute = datetime.today().minute
        hour = datetime.today().hour
        year = datetime.today().year
        p = {'day': day, 'month': month, 'year': year, 'hour': hour, 'min': minute, 'sec': second, 'event': event}
        db2.child('LineLiff').push(p)
        print(event)
        with open('lineliff.json', 'w') as lineliff:
            json.dump(event, lineliff)
        firstname = event['firstname']
        email = event['email']
        company = event['company']
        tel = event['tel']
        product = event['product']
        userId = event['userId']
        token = event['token']
        picture = event['picture']
        displayName = event['displayName']
        print(picture)
        x = f'คุณ: {displayName}\n\n{firstname}\n{email}\n{company}\n{tel}\n{product}\n\nขอบคุณที่ทำรายการค่ะ'
        line_bot_api2.push_message(userId, TextSendMessage(text=f'{x}'))
        line_bot_api2.push_message(userId, TextSendMessage(
            text='ขอบคุณลูกค้ามากค่ะ ทางเราจะติดต่อกลับให้เร็วที่สุดค่ะขอบคุณค่ะ'))
        return make_response(event)


@app.route('/paint')
def paint():
    return render_template('/sbadmin/painting.html')


@app.route('/saveimage', methods=['POST'])
def saveimage():
    if request.method == 'POST':
        event = request.form.to_dict()
        dir_name = 'static/img_paint'
        img_name = uuid.uuid4().hex
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        with open(os.path.join(dir_name, '{}.jpg'.format(img_name)), 'wb') as img:
            img.write(base64.b64decode(event['image'].split(",")[1]))
        original = Image.open(os.path.join(dir_name, '{}.jpg'.format(img_name)))
        if (original.format != 'JPEG'):
            return make_response('Unsupported image type.', 400)
        original.thumbnail((240, 240), Image.ANTIALIAS)
        original.save(os.path.join(dir_name, '{}_240.jpg'.format(img_name)), 'JPEG')
        return make_response(img_name, 200)


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
        return redirect(url_for('welcome'))
    data = {
        'id': id,
    }
    return render_template('/customers_new/intent.html', data=data)


@app.route('/c_intent/<string:id>', methods=['GET', 'POST'])
def old_intent(id):
    if not g.user:
        return redirect(url_for('welcome'))
    data = {
        'id': id,
    }
    return render_template('/customers_old/intent.html', data=data)


@app.route('/chart', methods=['GET', 'POST'])
def chart():
    if not g.user:
        return redirect(url_for('welcome'))
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


@app.route('/new_chart', methods=['GET', 'POST'])
def new_chart():
    if not g.user:
        return redirect(url_for('welcome'))
    ref = db2.child('LineLiff').get()
    lst = []
    count = 1
    for r in ref.each():
        k = r.key()
        users = r.val()
        users = dict(users)
        users.update({'index': str(count), 'key': k})
        lst.append(users)
        count = count + 1
    _id = len(lst)
    data = {
        'users': lst,
        'msg': _id
    }
    if request.method == 'POST':
        broadcast = request.form['msg']
        line_bot_api2.broadcast(TextSendMessage(text=str(broadcast)))
        return redirect(url_for('new_chart'))
    return render_template('/customers_new/charts.html', data=data)


@app.route('/download', methods=['GET'])
def download():
    if request.method == 'GET':
        ref = db2.child('LineLiff').get()
        date_time = []
        for i in ref.each():
            # print(i.val())
            days = i.val()['day']
            months = i.val()['month']
            years = i.val()['year']
            hour = i.val()['hour']
            min = i.val()['min']
            sec = i.val()['sec']
            displayName = i.val()['event']['displayName']
            email = i.val()['event']['email']
            firstname = i.val()['event']['firstname']
            picture = i.val()['event']['picture']
            product = i.val()['event']['product']
            tel = i.val()['event']['tel']
            token = i.val()['event']['token']
            dbTime = {'Name': firstname, 'Product': product, 'Email': email, 'Tel': tel, 'displayName': displayName,
                      'Email(Permisstion)': token, 'Day': days, 'Month': months, 'Year': years, 'Picture': picture}
            date_time.append(dbTime)
        dbDatetime = date_time
        data = pd.DataFrame(dbDatetime)
        datatoexcel = pd.ExcelWriter('static/excel/FromPython.xlsx', engine='xlsxwriter')
        data.to_excel(datatoexcel, sheet_name='Sheet1')
        datatoexcel.save()
        return send_from_directory('static/excel', 'FromPython.xlsx')
    return redirect(url_for('new_chart'))


@app.route('/remove/<string:key>', methods=['GET'])
def remove(key):
    db2.child('LineLiff').child(key).remove()
    return redirect(url_for('new_chart'))


@app.route('/api/upload', methods=['POST'])
def upload():
    image = cv2.imdecode(np.fromstring(request.files['image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
    img_processed = detect_object(image, None, None)
    print(img_processed)
    print(type(img_processed))
    return jsonify(img_processed)


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
        try:
            postback = decoded['events'][0]['type']
            data = decoded['events'][0]['postback']['data']
            if postback == 'postback':
                no_event = len(decoded['events'])
                for i in range(no_event):
                    event = decoded['events'][i]
                    event_handler1(event)
        except:
            _type = decoded['events'][0]['message']['type']
            if _type == 'text':
                txt = decoded['events'][0]['message']['text']
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
            if data == 'quote':
                line_bot_api1.reply_message(rtoken, TextSendMessage(
                    text='พิมพ์คำขึ้นต้นด้วย เช่าสุดคุ้ม ตามด้วย ชื่อ บริษัท เบอร์  อีเมลล์ จำนวน User ที่ต้องการใช้'))
    except:
        _type = event['message']['type']
        img = event['message']['id']
        user_id = event['source']['userId']
        sk_id = randrange(51626494, 51626533)
        if _type == 'sticker':
            replyObj = StickerSendMessage(package_id=str(11538), sticker_id=str(sk_id))
            line_bot_api1.reply_message(rtoken, replyObj)
        else:
            print(img)
            message_content = line_bot_api1.get_message_content(img)
            with open('static/images/line.png', 'wb') as fb:
                for chunk in message_content.iter_content():
                    fb.write(chunk)
            image = cv2.imread('static/images/line.png', cv2.IMREAD_UNCHANGED)
            detect_object(image, rtoken, user_id, line_bot_api1)


def event_handler1(event):
    postback = event['type']
    rtoken = event['replyToken']
    try:
        data = event['postback']['data']
        userid = event['source']['userId']
        if postback == 'postback':
            if data == 'product':
                line_bot_api2.reply_message(rtoken, productR4())
            elif data == '@ERPSoftware':
                line_bot_api2.reply_message(rtoken, flex_product())
            elif data == '@Business':
                line_bot_api2.reply_message(rtoken, flex_bus())
            elif data == '@NewFeature':
                line_bot_api2.reply_message(rtoken, flex_newfeature())
            elif data == '@Optional':
                line_bot_api2.reply_message(rtoken, flex_optional())
            # elif data == 'quote':
            #     # line_bot_api2.reply_message(rtoken, TextSendMessage(text='พิมพ์คำขึ้นต้นด้วย เช่าสุดคุ้ม ตามด้วย ชื่อ บริษัท เบอร์  อีเมลล์ จำนวน User ที่ต้องการใช้'))
            #     line_bot_api2.push_message(userid, TextSendMessage(text='พิมพ์คำขึ้นต้นด้วย เช่าสุดคุ้ม ตามด้วย ชื่อ บริษัท เบอร์ อีเมลล์ และจำนวน User ที่ต้องการใช้'))
            #     line_bot_api2.push_message(userid, TextSendMessage(text='เช่น เช่าสุดคุ้ม ชื่อ สำลี บริษัท MangoConsultant เบอร์ 09-999-XXXX อีเมลล์ user@admin.com จำนวน 5 user'))
            # if data == 'quoteq':
            #     line_bot_api2.reply_message(rtoken, TextSendMessage(
            #         text='พิมพ์คำขึ้นต้น ขอใบเสนอราคา ตามด้วย ชื่อ บริษัท เบอร์ อีเมลล์ จำนวน User และ Product ที่ต้องการ'))
            #     line_bot_api2.push_message(userid, TextSendMessage(
            #         text='เช่น ใบเสนอราคา ชื่อ สำลี บริษัท MangoConsultant เบอร์ 09-999-XXXX อีเมลล์ user@admin.com จำนวน 5 user Product Project Planning'))
            if data == 'business':
                line_bot_api2.reply_message(rtoken, TextSendMessage(
                    text='ในกรณีที่คุณลูกค้าต้องการสอบถามข้อมูลการ Power BI คุณลูกค้า แจ้งชื่อ เบอร์ติดต่อ เพื่อให้เจ้าหน้าที่ติดต่อกลับให้ข้อมูลเพิ่มเติมค่ะ'))
    except:
        _type = event['message']['type']
        img = event['message']['id']
        user_id = event['source']['userId']
        sk_id = randrange(51626494, 51626533)
        if _type == 'sticker':
            replyObj = StickerSendMessage(package_id=str(11538), sticker_id=str(sk_id))
            line_bot_api2.reply_message(rtoken, replyObj)
        else:
            print(img)
            message_content = line_bot_api2.get_message_content(img)
            with open('static/images/line.png', 'wb') as fb:
                for chunk in message_content.iter_content():
                    fb.write(chunk)
            image = cv2.imread('static/images/line.png', cv2.IMREAD_UNCHANGED)
            detect_object(image, rtoken, user_id, line_bot_api2)


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


def detect_object(img, rtoken, user_id, line_bot_api):
    scale = 0.5
    img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    height, width, channels = img.shape
    name_app = []
    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    stff = time.time()
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            # print(confidence)
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    label_str = []
    for i in range(len(boxes)):
        if i in indexes:
            print(i, indexes)
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            label_str.append(label)
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y - 5), font, .7, color, 2)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = detector(gray, 1)
    for d in dets:
        xy = d.left(), d.top()
        wh = d.right(), d.bottom()
        shape = sp(img, d)
        face_desc0 = model.compute_face_descriptor(img, shape, 1)  # output deeplearning
        d = []
        for face_desc in FACE_DESC:
            d.append(np.linalg.norm(np.array(face_desc) - np.array(face_desc0)))
        d = np.array(d)  # compare picture
        idx = np.argmin(d)  # ระบุลาเบล
        print(d[idx])
        if d[idx] <= 0.45:
            name = FACE_NAME[idx]
            name = str(name)
            print(name)
            # print(name_api)
            name_app.append(name)
            cv2.putText(img, name, (xy[0], xy[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.rectangle(img, xy, wh, (0, 255, 0), 2)
        else:
            name = 'Unknown'
            print(name)
            name_app.append(name)
            cv2.putText(img, name, (xy[0], xy[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.rectangle(img, xy, wh, (0, 0, 255), 2)
    str_name = ''
    str_object = ''
    for n in name_app:
        str_name = str_name + n.ljust(8)
    for l in label_str:
        str_object = str_object + l.ljust(8)
    img_item = 'static/images/predict_rec.png'
    cv2.imwrite(img_item, img)
    image_name = 'static/images/predict_rec.png'
    dir_name = 'static/images/face_people'
    img_name = uuid.uuid4().hex

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(image_name, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    with open(os.path.join(dir_name, '{}.jpg'.format(img_name)), 'wb') as image_base:
        image_base.write(base64.b64decode(encoded_string))
    original = Image.open(os.path.join(dir_name, '{}.jpg'.format(img_name)))
    original.thumbnail((240, 240), Image.ANTIALIAS)
    original.save(os.path.join(dir_name, '{}_240.jpg'.format(img_name)), 'JPEG')
    img_origin = 'https://www.mangoconsultant.net' + '/' + dir_name + '/' + img_name + '.jpg'
    img_240 = 'https://www.mangoconsultant.net' + '/' + dir_name + '/' + img_name + '_240.jpg'
    print(img_origin)
    print(img_240)
    image_message = ImageSendMessage(
        original_content_url=img_origin,
        preview_image_url=img_240
    )
    if not str_name and not str_object:
        line_bot_api.push_message(user_id, TextSendMessage(
            text='รูปที่คุณถ่าย ไม่สามารถระบุได้ โปรดถ่ายรูปหน้าคน หรือ รถสิ่งของต่าง ๆ'))
    else:
        line_bot_api.reply_message(rtoken, image_message)
        line_bot_api.push_message(user_id, TextSendMessage(text=f'นี้อาจจะเป็น {str(str_name)}รูปแบบ {str_object}'))
    return str(str_name)


def model_linebot():
    raw_json = request.get_json()
    json_line = json.dumps(raw_json)
    decoded = json.loads(json_line)
    messsage = decoded['events'][0]['message']['text']
    userId = decoded['events'][0]['source']['userId']
    embedding = []
    answers = []
    xtrain = []
    datasets = db1.child('transaction_mango').child('datasets').get()
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
    idx_answer = []
    for a in answers:
        idx = list(a)
        sli = idx[1:]
        idx_answer.append(sli)
    # print(idx_answer)
    count_vect = CountVectorizer(tokenizer=tokenize)
    Xtrain_count = count_vect.fit_transform(xtrain)
    tf_transformer = TfidfTransformer(use_idf=False)
    tf_transformer.fit(Xtrain_count)
    Xtrain_tf = tf_transformer.transform(Xtrain_count)
    SVM = svm.SVC(C=1.0, kernel='linear', degree=3,
                  gamma='auto', probability=True)
    SVM.fit(Xtrain_tf, embedding)
    msg = []
    msg.append(messsage)
    Xtest_count = count_vect.transform(msg)
    Xtest_tf = tf_transformer.transform(Xtest_count)
    label = SVM.predict(Xtest_tf)
    prop = SVM.predict_proba(Xtest_tf)[0][label]
    confidence = (0.3565152559 / ((len(embedding) * float(prop)) ** 0.5)) ** 2
    print(label)
    if label == [4]:
        db1.child('customer_email').push(get_datetime(None, line_bot_api1))
    return confidence, idx_answer, label, msg, userId


def model_linebot_new():
    raw_json = request.get_json()
    json_line = json.dumps(raw_json)
    decoded = json.loads(json_line)
    messsage = decoded['events'][0]['message']['text']
    userId = decoded['events'][0]['source']['userId']
    replyToken = decoded['events'][0]['replyToken']
    embedding = []
    answers = []
    xtrain = []
    datasets = db2.child('transaction_mango').child('datasets').get()
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
    idx_answer = []
    for a in answers:
        idx = list(a)
        sli = idx[1:]
        idx_answer.append(sli)
    # print(idx_answer)
    count_vect = CountVectorizer(tokenizer=tokenize)
    Xtrain_count = count_vect.fit_transform(xtrain)
    tf_transformer = TfidfTransformer(use_idf=False)
    tf_transformer.fit(Xtrain_count)
    Xtrain_tf = tf_transformer.transform(Xtrain_count)
    SVM = svm.SVC(C=1.0, kernel='linear', degree=3,
                  gamma='auto', probability=True)
    SVM.fit(Xtrain_tf, embedding)
    msg = []
    msg.append(messsage)
    Xtest_count = count_vect.transform(msg)
    Xtest_tf = tf_transformer.transform(Xtest_count)
    label = SVM.predict(Xtest_tf)
    prop = SVM.predict_proba(Xtest_tf)[0][label]
    p = float(prop)
    confidence = (0.3565152559 / ((len(embedding) * p) ** 0.5)) ** 2
    print(label)
    return confidence, idx_answer, label, msg, userId


def model_linebot_old():
    raw_json = request.get_json()
    json_line = json.dumps(raw_json)
    decoded = json.loads(json_line)
    messsage = decoded['events'][0]['message']['text']
    userId = decoded['events'][0]['source']['userId']
    embedding = []
    answers = []
    xtrain = []
    datasets = db3.child('transaction_mango').child('datasets').get()
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
    idx_answer = []
    for a in answers:
        idx = list(a)
        sli = idx[1:]
        idx_answer.append(sli)
    count_vect = CountVectorizer(tokenizer=tokenize)
    Xtrain_count = count_vect.fit_transform(xtrain)
    tf_transformer = TfidfTransformer(use_idf=False)
    tf_transformer.fit(Xtrain_count)
    Xtrain_tf = tf_transformer.transform(Xtrain_count)
    SVM = svm.SVC(C=1.0, kernel='linear', degree=3,
                  gamma='auto', probability=True)
    SVM.fit(Xtrain_tf, embedding)
    msg = []
    msg.append(messsage)
    Xtest_count = count_vect.transform(msg)
    Xtest_tf = tf_transformer.transform(Xtest_count)
    label = SVM.predict(Xtest_tf)
    prop = SVM.predict_proba(Xtest_tf)[0][label]
    p = float(prop)
    confidence = (0.3565152559 / ((len(embedding) * p) ** 0.5)) ** 2
    print('value3')
    return confidence, idx_answer, label, msg, userId


def get_datetime(x, line_bot_api):
    raw_json = request.get_json()
    json_line = json.dumps(raw_json)
    decoded = json.loads(json_line)
    message = decoded['events'][0]['message']['text']
    userId = decoded['events'][0]['source']['userId']
    day = datetime.today().day
    month = datetime.today().month
    second = datetime.today().second
    minute = datetime.today().minute
    hour = datetime.today().hour
    year = datetime.today().year
    profile = line_bot_api.get_profile(userId)
    profile = profile.display_name
    profile = str(profile)
    result = {'userid': userId, 'message': message, 'reply': x, 'profile': profile, 'hour': hour, 'min': minute,
              'sec': second, 'day': day, 'month': month, 'year': year}
    return result


def web_scraping_temp():
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

    @staticmethod
    def new_entertain():
        r = requests.get("https://www.thairath.co.th/entertain")
        soup = BeautifulSoup(r.content, "html.parser")
        newother = soup.find('div', {'class': 'col-md-8'})
        txt = ''
        for d in newother:
            txt = txt + '\n' + d.text
        return txt


def integrate_send(model_linebot, event, pack, stick, line_bot_api):
    result = model_linebot
    stick = random.choice(stick)
    x = random.choice(result[1][int(result[2])])
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
    line_bot_api.push_message(result[4], StickerSendMessage(package_id=str(pack), sticker_id=str(stick)))


@handler1.add(MessageEvent, message=TextMessage)
def handle_message(event):
    result = model_linebot()
    print(result[0])
    try:
        print('Result 1')
        if result[0] >= 0.14367:
            if ['ขอข้อมูลผลิตภัณฑ์'] == result[3]:
                x = 'card'
                line_bot_api1.reply_message(event.reply_token, product_action())
                inserted = get_datetime(x, line_bot_api1)
                db1.child('chatbot_transactions').push(inserted)
            elif ['ขอดู'] == result[3]:
                x = 'https://liff.line.me/1655104822-k5dRGJez'
                line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
            elif ['@mango'] == result[3]:
                line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'{result[4]}'))
            elif ['ฉันชื่ออะไร'] == result[3]:
                profile = line_bot_api1.get_profile(result[4])
                user_profile = profile.display_name
                user_profile = str(user_profile)
                line_bot_api1.reply_message(event.reply_token,
                                            TextSendMessage(text=f'เอ้า! ลืมชื่อตัวเองแล้วหรอ ก็ {user_profile} ไง'))
            else:
                if result[2] == [1]:
                    stick = ['52114110', '52114115', '52114129', '52114122']
                    pack = 11539
                    integrate_send(model_linebot(), event, pack, stick, line_bot_api1)
                elif result[2] == [6]:
                    stick = ['52114116', '52114117', '52114125']
                    pack = 11539
                    integrate_send(model_linebot(), event, pack, stick, line_bot_api1)
                elif result[2] == [5]:
                    stick = ['52114111', '52114119', '52114130']
                    pack = 11539
                    integrate_send(model_linebot(), event, pack, stick, line_bot_api1)
                else:
                    x = random.choice(result[1][int(result[2])])
                    line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
                    q_a = get_datetime(x, line_bot_api1)
                    inserted = db1.child('chatbot_transactions').push(q_a)
                    print(f'Inserted : {inserted}')
        else:
            if ['เปิดไฟ'] == result[3]:
                line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'โอเคจ้า ทำการเปิดไฟ'))
                db1.child('Node1').update({'Relay1': 0})
            elif ['ปิดไฟ'] == result[3]:
                line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'โอเคจ้า ทำการปิดไฟ'))
                db1.child('Node1').update({'Relay1': 1})
            elif ['temp'] == result[3]:
                temp = db1.child('Sensor Ultrasonic').get()
                temp = temp.val()
                line_bot_api1.reply_message(event.reply_token, TextSendMessage(text=f'Temperature {temp} C'))
            elif ['@Construction'] == result[3]:
                line_bot_api1.reply_message(event.reply_token, flex_product())
            elif ['test'] == result[3]:
                line_bot_api1.reply_message(event.reply_token, flex_erp())
    except LineBotApiError:
        abort(400)


@handler2.add(MessageEvent, message=TextMessage)
def handle_message_new(event):
    result = model_linebot_new()
    print(result[0])
    try:
        if result[0] >= 0.14:
            if ['ขอข้อมูลผลิตภัณฑ์'] == result[3]:
                x = 'card'
                line_bot_api2.reply_message(event.reply_token, productR4())
                inserted = get_datetime(x, line_bot_api2)
                db2.child('chatbot_transactions').push(inserted)
            elif ['@mango'] == result[3]:
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{result[4]}'))
            elif ['ฉันชื่ออะไร'] == result[3]:
                profile = line_bot_api2.get_profile(result[4])
                user_profile = profile.display_name
                user_profile = str(user_profile)
                line_bot_api2.reply_message(event.reply_token,
                                            TextSendMessage(text=f'เอ้า! ลืมชื่อตัวเองแล้วหรอ ก็ {user_profile} ไง'))
            elif ['มาก'] == result[3]:
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text='น้อย'))
            elif ['น้อย'] == result[3]:
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text='มาก'))
            elif ['คือ'] == result[3]:
                x = ['นั้นสินะ', 'อิหยังวะ', 'ว่า']
                z = random.choice(x)
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{z}'))
            elif ['คืออะไร'] == result[3]:
                x = ['นั้นสินะ', 'อิหยังวะ', 'ว่า']
                z = random.choice(x)
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{z}'))
            elif ['คือไร'] == result[3]:
                x = ['นั้นสินะ', 'อิหยังวะ', 'ว่า']
                z = random.choice(x)
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{z}'))
            elif ['คือไง'] == result[3]:
                x = ['นั้นสินะ', 'อิหยังวะ', 'ว่า']
                z = random.choice(x)
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{z}'))
            else:
                if result[2] == [3]:
                    sticker = ['52114110', '52114115', '52114129', '52114122']
                    pack = 11539
                    integrate_send(model_linebot_new(), event, pack, sticker, line_bot_api2)
                elif result[2] == [12]:
                    line_bot_api2.push_message(result[4], flex_destiny())
                    line_bot_api2.push_message(result[4], destiny())
                elif result[2] == [7]:
                    stick = ['51626520', '51626526']
                    pack = 11538
                    integrate_send(model_linebot_new(), event, pack, stick, line_bot_api2)
                elif result[2] == [2]:
                    line_bot_api2.push_message(result[4], flex_product())
                elif result[2] == [1]:
                    inserted = db2.child('customer_email').push(get_datetime(None, line_bot_api2))
                    # print(f'Inserted {inserted}')
                    x = random.choice(result[1][int(result[2])])
                    line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
                    image_message = ImageSendMessage(
                        original_content_url='https://sv1.picz.in.th/images/2020/10/21/bBc4NI.png',
                        preview_image_url='https://sv1.picz.in.th/images/2020/10/21/bBc4NI.png'
                    )
                    line_bot_api2.push_message(result[4], image_message)
                elif result[2] == [11]:
                    profile = line_bot_api2.get_profile(result[4])
                    displayName = profile.display_name
                    picture_url = profile.picture_url
                    user_id = profile.user_id
                    status = profile.status_message
                    # print(displayName, picture_url, user_id, status)
                    # line_bot_api2.push_message(result[4], flex_profile_erp(picture_url, displayName, status))
                    line_bot_api2.push_message(result[4], productR7())
                elif result[2] == [22]:
                    stick = ['51626503', '51626509']
                    pack = 11538
                    integrate_send(model_linebot_new(), event, pack, stick, line_bot_api2)
                elif result[2] == [23]:
                    day = datetime.today().day
                    month = datetime.today().month
                    second = datetime.today().second
                    minute = datetime.today().minute
                    hour = datetime.today().hour
                    year = datetime.today().year
                    x = 'วันนี้วันที่ {}/{}/{} เวลา {}:{}:{}'.format(day, month, year, hour, minute, second)
                    line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
                elif result[2] == [24]:
                    x = web_scraping_temp()
                    line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{str(x)}'))
                elif result[2] == [25]:
                    if result[3] == ['ข่าว']:
                        x = News.new_common()
                        line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
                        line_bot_api2.push_message(result[4], TextSendMessage(
                            text='ดูข่าวเพิ่มเติมลิงค์นี้เลย\nhttps://www.thairath.co.th/news/local'))
                        line_bot_api2.push_message(result[4], TextSendMessage(
                            text='และยังสามารถพิมพ์ ข่าว เว้นวรรค ตามด้วยข่าวที่ต้องการได้ค่ะ\nเช่น ข่าว ทั่วไป, ข่าว กีฬา, ข่าว การเมือง'))
                    else:
                        i = ''
                        k = result[3]
                        p = i.join(k)
                        print(p)
                        x = p.split('ข่าว')
                        print(x)
                        tranform = ''
                        ans = tranform.join(x)
                        print('string >: ', ans)
                        if ans == ' ทั่วไป':
                            x = News.new_common()
                            line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
                            line_bot_api2.push_message(result[4], TextSendMessage(text='ดูข่าวเพิ่มเติมลิงค์นี้เลย\nhttps://www.thairath.co.th/news/local'))
                            line_bot_api2.push_message(result[4], TextSendMessage(text='และยังสามารถพิมพ์ ข่าว เว้นวรรค ตามด้วยข่าวที่ต้องการได้ค่ะ\nเช่น ข่าว ทั่วไป, ข่าว กีฬา, ข่าว บันเทิง'))
                        elif ans == ' กีฬา':
                            x = News.new_sport()
                            line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
                            line_bot_api2.push_message(result[4], TextSendMessage(
                                text='ดูข่าวเพิ่มเติมลิงค์นี้เลย\nhttps://www.thairath.co.th/sport'))
                            line_bot_api2.push_message(result[4], TextSendMessage(
                                text='และยังสามารถพิมพ์ ข่าว เว้นวรรค ตามด้วยข่าวที่ต้องการได้ค่ะ\nเช่น ข่าว ทั่วไป, ข่าว กีฬา, ข่าว บันเทิง'))
                        elif ans == ' บังเทิง':
                            x = News.new_entertain()
                            line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
                            line_bot_api2.push_message(result[4], TextSendMessage(
                                text='ดูข่าวเพิ่มเติมลิงค์นี้เลย\nhttps://www.thairath.co.th/entertain'))
                            line_bot_api2.push_message(result[4], TextSendMessage(
                                text='และยังสามารถพิมพ์ ข่าว เว้นวรรค ตามด้วยข่าวที่ต้องการได้ค่ะ\nเช่น ข่าว ทั่วไป, ข่าว กีฬา, ข่าว บันเทิง'))

                elif ['ไรงะ'] == result[3]:
                    line_bot_api2.reply_message(event.reply_token, TextSendMessage(text='อะไรงะ'))
                elif ['งะ'] == result[3]:
                    line_bot_api2.reply_message(event.reply_token, TextSendMessage(text='ง้าววววว'))
                elif ['หรอ'] == result[3]:
                    x = ['จ้า', 'ใช่จ้า', 'จริงสิ']
                    y = random.choice(x)
                    line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{y}'))
                elif ['ใช่หรอ'] == result[3]:
                    x = ['จ้า', 'ใช่จ้า', 'จริงสิ']
                    y = random.choice(x)
                    line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{y}'))
                elif ['งั้นหรอ'] == result[3]:
                    x = ['จ้า', 'ใช่จ้า', 'จริงสิ']
                    y = random.choice(x)
                    line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{y}'))
                else:
                    x = random.choice(result[1][int(result[2])])
                    line_bot_api2.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
                    q_a = get_datetime(x, line_bot_api2)
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
            elif ['mango'] == result[3]:
                z = ['ยินดีให้บิรการค่า', 'อาการมันเป็นยังไงไหนบอกแมงโก้สิ', 'ว่าไงจ๊ะ']
                x = random.choice(z)
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text='{}'.format(x)))
                get_datetime(x, line_bot_api2)
            elif ['แมงโก้'] == result[3]:
                z = ['ยินดีให้บิรการค่า', 'อาการมันเป็นยังไงไหนบอกแมงโก้สิ', 'ว่าไงจ๊ะ']
                x = random.choice(z)
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text='{}'.format(x)))
                get_datetime(x, line_bot_api2)
            elif ['น้อย'] == result[3]:
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text='มาก'))
            elif ['@Product'] == result[3]:
                x = 'flex message'
                line_bot_api2.reply_message(event.reply_token, flex_erp())
                # line_bot_api2.push_message(result[4], TextSendMessage(
                #     text='หากต้องการใบเสนอราคา พิมพ์คำขึ้นต้นด้วย เช่าสุดคุ้ม ตามด้วย ชื่อ บริษัท เบอร์ อีเมลล์ และจำนวน User ที่ต้องการใช้'))
                # line_bot_api2.push_message(result[4], TextSendMessage(
                #     text='เช่น เช่าสุดคุ้ม ชื่อ สำลี บริษัท MangoConsultant เบอร์ 09-999-XXXX อีเมลล์ user@admin.com จำนวน 5 user'))
                inserted = get_datetime(x, line_bot_api2)
                db2.child('chatbot_transactions').push(inserted)
            elif ['@ERPSoftware'] == result[3]:
                line_bot_api2.reply_message(event.reply_token, flex_product())
            elif ['ขอqrcode'] == result[3]:
                image_message = ImageSendMessage(
                    original_content_url='https://sv1.picz.in.th/images/2020/10/09/OeiUj9.png',
                    preview_image_url='https://sv1.picz.in.th/images/2020/10/09/OeiUj9.png'
                )
                line_bot_api2.reply_message(event.reply_token, image_message)
            elif ['@NewFeature'] == result[3]:
                line_bot_api2.reply_message(event.reply_token, flex_newfeature())
            elif ['@Optional'] == result[3]:
                line_bot_api2.reply_message(event.reply_token, flex_optional())
            elif ['@Business'] == result[3]:
                line_bot_api2.reply_message(event.reply_token, flex_bus())
            elif ['วาดรูป'] == result[3]:
                line_bot_api2.reply_message(event.reply_token,
                                            TextSendMessage(text='https://liff.line.me/1655104822-L5Ob5XdD'))
            else:
                line_bot_api2.reply_message(event.reply_token, TextSendMessage(text='แอดมินอาจจะให้ข้อมูลได้ไม่ครบถ้วน '
                                                                                    'คุณลูกค้าพอจะสะดวกจะแจ้งเบอร์โทรศัทพ์ไหมคะ '
                                                                                    'แอดมินจะดำเนินการผสานงานให้ผู้ที่เกี่ยวข้อง '
                                                                                    'ให้คำแนะนำอย่างครบถ้วนค่ะ'))
                line_bot_api2.push_message(result[4], TextSendMessage(
                    text='หากต้องการให้ทีมมงาน เข้าไป Demo โปรแกรม กรุณาโทร. 063-565-4594 ติดต่อคุณเมทิกานะคะ\nขอบคุณค่ะ'))
                line_bot_api2.push_message(result[4],
                                           StickerSendMessage(package_id=str(11538), sticker_id=str(51626499)))
    except LineBotApiError:
        abort(400)


@handler3.add(MessageEvent, message=TextMessage)
def handle_message_old(event):
    result = model_linebot_old()
    print(result[0])
    try:
        if result[0] >= 0.14367:
            if ['ขอข้อมูลผลิตภัณฑ์'] == result[3]:
                x = 'card'
                line_bot_api3.reply_message(event.reply_token, mangoerp())
                inserted = get_datetime(x, line_bot_api3)
                db3.child('chatbot_transactions').push(inserted)
            elif ['@mango'] == result[3]:
                line_bot_api3.reply_message(event.reply_token, TextSendMessage(text=f'{result[4]}'))
            elif ['ฉันชื่ออะไร'] == result[3]:
                profile = line_bot_api3.get_profile(result[4])
                user_profile = profile.display_name
                user_profile = str(user_profile)
                line_bot_api3.reply_message(event.reply_token,
                                            TextSendMessage(text=f'เอ้า! ลืมชื่อตัวเองแล้วหรอ ก็ {user_profile} ไง'))
            else:
                x = random.choice(result[1][int(result[2])])
                line_bot_api3.reply_message(event.reply_token, TextSendMessage(text=f'{x}'))
                q_a = get_datetime(x, line_bot_api3)
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


@app.route('/api/richmenu/<string:rich>', methods=['GET', 'POST'])
def richmenu(rich):
    with open('richmenu.json', encoding='utf8') as w:
        data = json.load(w)
        rich_id = data['id']
    if rich == 'create':
        rich_menu_to_create = RichMenu(
            size=RichMenuSize(width=2500, height=1686),
            selected=False,
            name="Nice richmenu",
            chat_bar_text="Tap here",
            areas=[RichMenuArea(
                bounds=RichMenuBounds(x=853, y=164, width=1615, height=232),
                action=URIAction(label='Go to line.me', uri='https://line.me')),
                RichMenuArea(
                    bounds=RichMenuBounds(x=155, y=353, width=598, height=414),
                    action=MessageAction(label='text', text='hey')
                )
            ]
        )
        rich_menu_id = line_bot_api1.create_rich_menu(rich_menu=rich_menu_to_create)
        txt = {'id': rich_menu_id}
        print(txt)
        with open('richmenu.json', 'w') as r:
            json.dump(txt, r)
        return jsonify(txt)
    elif rich == 'uploadimg':
        with open('ProductThumb_45569_67700481_resize.jpg', 'rb') as f:
            line_bot_api1.set_rich_menu_image('richmenu-455e1d928c3b906515a05598ba745772', 'image/jpeg', f)
            print(f'rich_id : {rich_id}')
        return 'ok'
    elif rich == 'set':
        line_bot_api1.set_default_rich_menu('richmenu-455e1d928c3b906515a05598ba745772')
        return 'ok'
    elif rich == 'get_id':
        pass
        # rich_menu = line_bot_api1.get_rich_menu(str(rich_Tranform))
        # print(rich_menu.rich_menu_id)
        # return jsonify(str(rich_menu))
    elif rich == 'deleteall':
        rich_menu_list = line_bot_api1.get_rich_menu_list()
        for rich_menu in rich_menu_list:
            richz = rich_menu.rich_menu_id
            line_bot_api1.delete_rich_menu(str(richz))
            print(richz)
        return str('ok')
    elif rich == 'list':
        tx = []
        rich_menu_list = line_bot_api1.get_rich_menu_list()
        for rich_menu in rich_menu_list:
            richz = rich_menu.rich_menu_id
            tx.append(richz)
        print(tx)
        return str(tx)
    elif rich == 'link_rich':
        line_bot_api1.delete_rich_menu('richmenu-3202e3f39315170a26bf8deca4703e95')
        return 'ok'


if __name__ == '__main__':
    app.run(debug=True, port=5005)
