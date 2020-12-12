from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn import svm
from attacut import tokenize
from numpy import random
import firebase_admin  # authen Firebase
from firebase_admin import credentials, auth  # authen Firebase,
import pyrebase
import json
from flask import Flask, request, abort, render_template, jsonify, session, g
import pandas as pd

cred = credentials.Certificate("model/config/database_test/authen_firebase.json")
firebase_auth = firebase_admin.initialize_app(cred)

with open('model/config/database_new/firebase.json', encoding='utf8') as json_file:
    data = json.load(json_file)
    config = data['firebase']
    firebase = pyrebase.initialize_app(config)
    pb = pyrebase.initialize_app(config)
    db = firebase.database()

app = Flask(__name__)


# ref = db.child('requestContract').get()
# for i in ref.each()[1:]:
#     if '' in i.val()['tag']:
#         print(i.val()['tag'])
#         # print(i.key())
#         db.child('requestContract').child(i.key()).update({'tag': ''})



#
# @app.before_request
# def before_request():
#     try:
#         if 'user_id' in session:
#             user = session['user_id']
#             g.user = user
#     except:
#         print("error login")
#
#
# @app.route('/signup', methods=['POST'])
# def register():
#     email = request.form['email']
#     pwd = request.form['password']
#     displayName = request.form['username']
#     try:
#         auth.create_user(email=email, password=pwd, displayName=displayName)
#         return jsonify({'signup': 'success'})
#     except:
#         return jsonify({'signup': 'error'})
#
#
# @app.route('/lg', methods=['POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         print(request.form.to_dict())
#         session.pop('user_id', None)
#         user = pb.auth().sign_in_with_email_and_password(email=email, password=password)
#         print(user)
#         session['user_id'] = user
#         return jsonify({'login': 'success'})
#
#
# @app.route('/logout', methods=['GET', 'POST'])
# def logout():
#     if request.method == 'GET':
#         session.clear()
#         print(session)
#         return jsonify({'logout': dict(session)})
#
#
# @app.route('/index')
# def index():
#     if not g.user:
#         return jsonify({'session': 'Not User'})
#     print(g.user)
#     return jsonify({'session': g.user['displayName']})
#
#
# if __name__ == '__main__':
#     app.run(port=5555, debug=True)

# def popChip(transaction, id, tag, value):
#     ref = db.child(transaction).child(id).get().val()[tag]
#     x = value
#     txt = ''
#     y = txt.join(x)
#     count = 0
#     for i in ref:
#         toCount = ref[count]
#         if y == toCount:
#             ref.pop(count)
#         count += 1
#     final = db.child(transaction).child(id).update({'Tag': ref})
#     return print(final)
# ref = db.child('requestDemo').get()
# lst = []
# products = []
# for i in ref.each()[1:]:
#     key = i.key()
#     date = i.val()['Date']
#     time = i.val()['Time']
#     tag = i.val()['tag']
#     event = i.val()['event']
#     company = event['company']
#     email = event['email']
#     name = event['fname']
#     product = event['product']
#     products.append(product)
#     message = event['message']
#     tel = event['tel']
#     group = {'id': key, 'name': name, 'product': product, 'company': company, 'email': email,
#              'message': message, 'tel': tel, 'date_time': f'{date} {time}', 'tag': tag}
#     lst.append(group)


# construction = [x for x in products if 'Mango ERP (Real Estate)' in x]
# print(construction)


# count = 1
# demolist = []
# contractlist = []
# companys = []
# group = {}
# for demo in ref.each()[1:]:
#     key = demo.key()
#     company = demo.val()['event']['company']
#     companys.append(company)
#     email = demo.val()['event']['email']
#     fname = demo.val()['event']['fname']
#     product = demo.val()['event']['product']
#     message = demo.val()['event']['message']
#     tel = demo.val()['event']['tel']
#     date = demo.val()['Date']
#     time = demo.val()['Time']
#     tag = demo.val()['tag']
#     apiDemo = {'Index': count, 'key': key, 'Name': fname, 'Company': company, 'Email': email,
#                'Product': product, 'Message': message, 'tel': tel, 'tag': tag, 'Time': time,
#                'Date': date, 'Channel': 'web mango'}
#     demolist.append(apiDemo)

# lst = []
# contracts = db.child('requestContract').get()
# for contract in contracts.each()[1:]:
#     key = contract.key()
#     event = contract.val()['event']
#     contact_email = event['contact_email']
#     contact_email_div = event['contact_email_div']
#     contact_message = event['contact_message']
#     contact_name = event['contact_name']
#     contact_name_company = event['contact_name_company']
#     contact_subject = event['contact_subject']
#     contact_tel = event['contact_tel']
#     date = contract.val()['Date']
#     time = contract.val()['Time']
#     tag = contract.val()['tag']
#     apiContract = {'key': key, 'email': contact_email, 'email_div': contact_email_div,
#                    'message': contact_message, 'name': contact_name, 'company': contact_name_company,
#                    'product': contact_subject, 'tel': contact_tel, 'date_time': f'{date} {time}'}
#     lst.append(apiContract)
# print(lst)


# print(test)


# ref = db.child('trainCustomer').get()

# for i in ref.each():
#     key = i.key()
#     print(key)
#     event = i.val()['event']
#     channel = event['channel']
#     comment = event['comment']
#     company = event['company']
#     displayName = event['displayName']
#     email = event['email']
#     firstname = event['firstname']
#     news = event['news']
#     picture = event['picture']
#     tel = event['tel']
#     token = event['token']
#     userId = event['userId']
#     group = {
#         'channel': channel, 'comment': comment, 'company': company, 'displayName': displayName, 'email': email,
#         'firstname': firstname, 'news': news, 'picture': picture, 'tel': tel, 'token': token, 'userId': userId,
#         'position': ''
#     }
#     print(group)
#     db.child('trainCustomer').child(key).update({'event': group})

# for i in ref.each():
#     key = i.key()
#     db.child('trainCustomer').child(key).update()


# @app.route('/json_information/<id>', methods=['PUT', 'DELETE'])
# def return_information_update(id):
#     response_object = {'status': 'success'}
#     if request.method == 'PUT':
#         post_data = request.get_json()
#         print(id)
#         d = dict(post_data)
#         fire = FirebaseAPI(None)
#         if d['tag']:
#             group = fire.groupToInsert(d, d['tag'])
#             db2.child('RestCustomer').child(id).update(group)
#             response_object['message'] = 'Data updated!'
#             return make_response({response_object})
#         else:
#             group = fire.groupToInsert(d, '')
#             db2.child('RestCustomer').child(id).update(group)
#             response_object['message'] = 'Data updated!'
#             return make_response({response_object})
#     if request.method == 'DELETE':
#         db2.child('RestCustomer').child(id).remove()
#         return make_response({'delete': 'success'})
#     return jsonify(response_object)