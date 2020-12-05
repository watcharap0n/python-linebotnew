import firebase_admin
import pyrebase
import json, webbrowser
from linebot import LineBotApi, WebhookHandler
from mangoerp.myClass import *
import pandas as pd
from linebot.models import TextSendMessage, ImageSendMessage
from attacut import tokenize
from flask import Flask, request, abort, jsonify, render_template, send_from_directory, redirect, url_for
from linebot import LineBotApi
from firebase_admin import credentials, auth

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


class FirebaseAPI:
    def __init__(self, db):
        self.db = db

    def information(self, transaction):
        lst = []
        ref = db.child(transaction).get()
        for i in ref.each()[1:]:
            key = i.key()
            name = i.val()['Name']
            tag = i.val()['Tag']
            profile = i.val()['Profile']
            channel = i.val()['Channel']
            company = i.val()['Company']
            other = i.val()['Other']
            email = i.val()['Email']
            liff = i.val()['EmailLiff']
            position = i.val()['Position']
            tax = i.val()['Tax']
            tel = i.val()['Tel']
            time = i.val()['Time']
            date = i.val()['Date']
            message = i.val()['Message']
            authorized = i.val()['Authorized']
            date_insert = i.val()['DateInsert']
            time_insert = i.val()['TimeInsert']
            username = i.val()['Username']
            product = i.val()['Product']
            group = {
                'id': key, 'Name': name, 'Tag': tag, 'Product': product, 'Email': email, 'Other': other,
                'EmailLiff': liff, 'Company': company, 'Tel': tel, 'Channel': channel, 'Message': message,
                'Profile': profile, 'Username': username, 'Time': time, 'Date': date, 'DateInsert': date_insert,
                'TimeInsert': time_insert, 'datetime': f'{date} {time}', 'Position': position, 'Tax': tax,
                'Authorized': authorized, 'datetime_insert': f'{date_insert} {time_insert}'
            }
            lst.append(group)
        return lst

    def requestDemo(self, transaction):
        ref = db.child(transaction).get()
        lst = []
        products = []
        for i in ref.each()[1:]:
            key = i.key()
            date = i.val()['Date']
            time = i.val()['Time']
            tag = i.val()['tag']
            event = i.val()['event']
            company = event['company']
            email = event['email']
            name = event['fname']
            product = event['product']
            products.append(product)
            message = event['message']
            tel = event['tel']
            group = {'id': key, 'name': name, 'product': product, 'company': company, 'email': email,
                     'message': message, 'tel': tel, 'date_time': f'{date} {time}', 'tag': tag}
            lst.append(group)
        return lst, products


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        lst = []
        ref = db.child('id').get()
        for i in ref.each():
            key = i.key()
            channel = i.val()['channel']
            message = i.val()['comment']
            group = {'index': key, 'channel': channel, 'message': message}
            lst.append(group)
        status = {'status': 'success'}
        status['firebase'] = lst
        return jsonify(status)
    elif request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        return jsonify('ok')


@app.route('/index/<index>', methods=['PUT', 'DELETE'])
def single_book(index):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        print(index)
        post_data = request.get_json()
        print(post_data)
        response_object['message'] = 'Data updated!'
    if request.method == 'DELETE':
        print(index)
    return jsonify(response_object)


@app.route('/api')
def api():
    return render_template('test_api/api/backup_table.html')


@app.route('/information_test')
def information():
    return render_template('test_api/api/information_backup.html')


@app.route('/requestDemo_test')
def requestDemo():
    return render_template('test_api/test/request_demo.html')


@app.route('/')
@app.route('/information')
def page_info():
    return render_template('test_api/test/testTable.html')


@app.route('/return_information', methods=['GET', 'POST'])
def return_information():
    tag = ['CB010', 'CC010', 'CG010', 'CI010', 'CJ010', 'CM010',
           'CF010', 'CP010', 'CE010', 'CH010', 'CK010', 'CN010', 'CD010',
           'RC010', 'RA010', 'RB010']
    if request.method == 'GET':
        transaction = FirebaseAPI(db)
        marketing_infomation = transaction.information('RestCustomer')
        len_transaction = len(marketing_infomation)
        status = {'transaction': marketing_infomation, 'status': 'success', 'tags': tag,
                  'amount_info': len_transaction}
        return jsonify(status)
    elif request.method == 'POST':
        post_data = request.get_json()
        db.child('RestCustomer').push(post_data)
        print(post_data)
        return jsonify(post_data)


@app.route('/excel_information', methods=['POST'])
def excel_information():
    if request.method == 'POST':
        post_data = request.get_json()
        button_event = ButtonEvent(loop=post_data, db=db, tag_insert=None)
        print(post_data)
        button_event.button_excel_information()
        return send_from_directory('static/excel', 'Customers.xlsx')


@app.route('/sort_information', methods=['POST'])
def sort_information():
    if request.method == 'POST':
        post_data = request.get_json()
        tags = post_data['tags']
        key = post_data['key']
        for i in key:
            db.child('RestCustomer').child(i).update({'Tag': tags})
        print(post_data)
        return jsonify(post_data)


@app.route('/return_information/<id>', methods=['PUT', 'DELETE'])
def return_information_update(id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(id)
        print(post_data)
        db.child('RestCustomer').child(id).update(post_data)
        response_object['message'] = 'Data updated!'
    if request.method == 'DELETE':
        print(id)
        db.child('RestCustomer').child(id).remove()
    return jsonify(response_object)


@app.route('/demo_test', methods=['GET', 'POST'])
def demo():
    tags = ['CB010', 'CC010', 'CG010', 'CI010', 'CJ010', 'CM010',
            'CF010', 'CP010', 'CE010', 'CH010', 'CK010', 'CN010', 'CD010',
            'RC010', 'RA010', 'RB010']
    if request.method == 'GET':
        transaction = FirebaseAPI(db).requestDemo('requestDemo')[0]
        products = FirebaseAPI(db).requestDemo('requestDemo')[1]
        construction = [x for x in products if 'Mango ERP (Real Estate)' in x]
        print(construction)
        status = {'transaction': transaction, 'status': 'success', 'tags': tags}
        return jsonify(status)


@app.route('/return_info', methods=['GET', 'POST'])
def info():
    tag = ['CB010', 'CC010', 'CG010', 'CI010', 'CJ010', 'CM010',
           'CF010', 'CP010', 'CE010', 'CH010', 'CK010', 'CN010', 'CD010',
           'RC010', 'RA010', 'RB010']
    if request.method == 'GET':
        transaction = FirebaseAPI(db).information('requestDemo')
        status = {'transaction': transaction, 'status': 'success', 'tags': tag}
        print(status)
        return jsonify(status)
    elif request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        return jsonify('ok')


@app.route('/return_info/<id>', methods=['PUT', 'DELETE'])
def single_info(id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(id)
        print(post_data)
        ref = db.child('RestCustomer').child(id).update(post_data)
        print(ref)
        response_object['message'] = 'Data updated!'
    if request.method == 'DELETE':
        print(id)
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(debug=True, port=5005)
#
