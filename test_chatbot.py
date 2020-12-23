from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn import svm
from attacut import tokenize
from numpy import random
from collections import OrderedDict
import firebase_admin  # authen Firebase
from firebase_admin import credentials, auth  # authen Firebase,
import pyrebase
import datetime as tim
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
#             group = fire.grouptoinsert(d, d['tag'])
#             db2.child('restcustomer').child(id).update(group)
#             response_object['message'] = 'data updated!'
#             return make_response({response_object})
#         else:
#             group = fire.grouptoinsert(d, '')
#             db2.child('restcustomer').child(id).update(group)
#             response_object['message'] = 'data updated!'
#             return make_response({response_object})
#     if request.method == 'delete':
#         db2.child('restcustomer').child(id).remove()
#         return make_response({'delete': 'success'})
#     return jsonify(response_object)


# test = {'company': 'google', 'date/time': '5-12-2020 11:12:47', 'email': 'sldale2004@yahoo.com',
#         'fname': 'HenryFap', 'index': 217, 'key': '-MNly6U1o2_3NDomkjrZ',
#         'message': 'Invest $1 today to make $1000 tomorrow. \r\nLink - https://is.gd/eVGXkc', 'product': 'Mango Application on Mobile', 'tag': [''], 'tel': '89035069608'}
#
# del test['key']
# del test['index']
# d = datetime.datetime.strptime(test['date/time'], "%d-%m-%Y  %H:%M:%S")
# day, month, year, hour, minute, sec = d.day, d.month, d.year, d.hour, d.minute, d.second
# test['Date'] = test.pop('date/time')
# test.update({'Date': f'{day}-{month}-{year}'})
# test['Time'] = test
# test.update({'Time': f'{hour}:{minute}:{sec}'})
# event = {'Date': test['Date'], 'Time': test['Time'],'tag': test['tag'] ,'event': {test['company'], test['email'], test['fname'], test['product'], test['tel'], test['message']}}
# print(event)


class GetDateTime:
    def __init__(self, value, db):
        self.value = value
        self.db = db

    @classmethod
    def todo_date(cls, value):
        return cls(value, db=db)

    def get_date(self, user):
        return user.get(self.value)

    @staticmethod
    def dynamic_date(lst, value, condition):
        return [i for i in lst if i[value] == condition]

    # def data_datetime(self, transaction):
    #     foo = []
    #     ref = self.db.child(transaction).get()
    #     for i in ref.each():
    #         v = i.val()
    #         date = v['Date']
    #         time = v['Time']
    #         fname = v['Name']
    #         company = v['Company']
    #         product = v['Product']
    #         channel = v['Channel']
    #         d = tim.datetime.strptime(date, '%d-%m-%Y')
    #         t = tim.datetime.strptime(time, '%H:%M:%S')
    #         mapProduct = {'fname': fname, 'company': company, 'product': product, 'channel': channel, 'day': d.day,
    #                       'month': d.month, 'year': d.year}
    #         foo.append(mapProduct)
    #     return foo


# foo = []
# ref = db.child('RestCustomer').get()
# cut_channel = []
# cut_product = []
# for i in ref.each():
#     v = i.val()
#     date = v['Date']
#     time = v['Time']
#     fname = v['Name']
#     company = v['Company']
#     product = v['Product']
#     cut_product.append(product)
#     channel = v['Channel']
#     cut_channel.append(channel)
#     d = tim.datetime.strptime(date, '%d-%m-%Y')
#     t = tim.datetime.strptime(time, '%H:%M:%S')
#     mapProduct = {'fname': fname, 'company': company, 'product': product, 'channel': channel, 'day': d.day,
#                   'month': d.month, 'year': d.year, 'date': f'{date}', 'time': f'{time}', 'month_check': f'{d.year}-{d.month}'}
#     foo.append(mapProduct)




# count = 0
# for i in range(1, len(cut_channel)):
#     count += 1
#     while count < len(cut_channel):
#         if cut_channel[i] == cut_channel[count]:
#             del cut_channel[count]
#         else:
#             count += 1
#     i += 1
#
# print(cut_channel)


ref = db.child('RestCustomer').get()
for i in ref.each()[1:]:
    if i.val()['Product'] == 'Pusit (Consulting)':
        db.child('RestCustomer').child(i.key()).update({'Product': 'Consulting'})
        print(i.val())

# get_data = GetDateTime(value=None, db=db)
# month = get_data.todo_date('month')
# foo.sort(key=month.get_date)
#
# x = ['2020-11', '2020-12']
# lst = []
# for i in foo:
#     for e in x:
#         if i['month_check'] == e:
#             lst.append(i)
#
# for i in lst:
#     if i['channel'] != 'LINE' and i['channel'] != 'web mango':
#         print(i)


# product = str(input('Product: '))
# channel = str(input('Channel: '))
# print(product, type(product))
# print(channel, type(channel))
# date = '2020-12-18'
# d = tim.datetime.strptime(date, '%Y-%m-%d')
# print(f'{d.day}-{d.month}-{d.year}')

# x = ['2020-11-11', '2020-11-5', '2020-11-13']
# for i in x:
#     d = tim.datetime.strptime(i, '%Y-%m-%d')
#     d = f'{d.day}-{d.month}-{d.year}'
#     for e in foo:
#         if d == e['date'] and e['product'] == 'Construction':
#             print(e)
#

#

# ref = db.child('set_sort_date').get()
# ref = dict(ref.val())
# print()
# ms = [result for date in dates for result in foo if date == result['date'] and result['product'] == 'Construction']






    # if i['day'] == :
    #     print()

    # if i['date'] == f'{d.day}-{d.month}-{d.year}':
    #     pass

# y = next(x for x in foo if x['month'] > 12)

#
# test = {y['month']: foo}
# print(test)

# m10 = get_data.dynamic_date(foo, 'month', 10)
# m11 = get_data.dynamic_date(foo, 'product', 'RealEstate')
# m12 = get_data.dynamic_date(foo, 'month', 12)
# print(m11)


# print(m11)
# def get_dict_key(mydict, val):
#     for key, value in mydict.items():
#         if val == value:
#             return key
#
# s = {'ok': 'ja'}
# if s.get('jj'):
#     print(s)
# else:
#     print('ok')


# {#                      <v-expansion-panels popout>#}
# {#                        <v-expansion-panel#}
# {#                            v-for="(x, z) in m"#}
# {#                            :key="z"#}
# {#                        >#}
# {#                          <v-expansion-panel-header>#}
# {#                            <v-col cols="3">#}
# {#                              <v-menu#}
# {#                                  bottom#}
# {#                                  right#}
# {#                                  transition="scale-transition"#}
# {#                                  origin="top left"#}
# {#                              >#}
# {#                                <template v-slot:activator="{ on }">#}
# {#                                  <v-chip#}
# {#                                      pill#}
# {#                                      v-on="on"#}
# {#                                  >#}
# {#                                    <v-avatar left>#}
# {#                                      <v-img :src="x.img"></v-img>#}
# {#                                    </v-avatar>#}
# {#                                    บริษัท: [[x.company]]#}
# {#                                  </v-chip>#}
# {#                                </template>#}
# {#                                <v-card width="300">#}
# {#                                  <v-list dark>#}
# {#                                    <v-list-item>#}
# {#                                      <v-list-item-avatar>#}
# {#                                        <v-img :src="x.img"></v-img>#}
# {#                                      </v-list-item-avatar>#}
# {#                                      <v-list-item-content>#}
# {#                                        <v-list-item-title>[[x.fname]]</v-list-item-title>#}
# {#                                        <v-list-item-subtitle>[[x.company]]</v-list-item-subtitle>#}
# {#                                      </v-list-item-content>#}
# {#                                      <v-list-item-action>#}
# {#                                        <v-btn#}
# {#                                            icon#}
# {#                                            @click="menu = false"#}
# {#                                        >#}
# {#                                          <v-icon>mdi-close-circle</v-icon>#}
# {#                                        </v-btn>#}
# {#                                      </v-list-item-action>#}
# {#                                    </v-list-item>#}
# {#                                  </v-list>#}
# {#                                  <v-list>#}
# {#                                    <v-list-item @click="() => {}">#}
# {#                                      <v-list-item-action>#}
# {#                                        <v-icon>mdi-briefcase</v-icon>#}
# {#                                      </v-list-item-action>#}
# {#                                      <v-list-item-subtitle>[[x.email]]</v-list-item-subtitle>#}
# {#                                    </v-list-item>#}
# {#                                  </v-list>#}
# {#                                </v-card>#}
# {#                              </v-menu>#}
# {#                            </v-col>#}
# {#                            <v-col cols="3">#}
# {#                              <v-chip#}
# {#                                  class="ma-2"#}
# {#                                  color="red"#}
# {#                                  outlined#}
# {#                              >#}
# {#                                <v-icon left>#}
# {#                                  mdi-office-building#}
# {#                                </v-icon>#}
# {#                                [[x.product]]#}
# {#                              </v-chip>#}
# {#                            </v-col>#}
# {#                            <v-col cols="3">#}
# {#                              <v-chip#}
# {#                                  class="ma-2"#}
# {#                                  color="success"#}
# {#                                  outlined#}
# {#                              >#}
# {#                                <v-icon left>#}
# {#                                  mdi-server-plus#}
# {#                                </v-icon>#}
# {#                                [[x.channel]]#}
# {#                              </v-chip>#}
# {#                            </v-col>#}
# {#                            <v-col cols="2" class="grey--text text-truncate hidden-sm-and-down">#}
# {#                              [[x.datetime]]#}
# {#                            </v-col>#}
# {##}
# {#                          </v-expansion-panel-header>#}
# {#                          <v-expansion-panel-content>#}
# {#                            <v-row>#}
# {#                              <v-col cols="4" v-if="x.message">#}
# {#                                ข้อความ: [[x.message]]#}
# {#                              </v-col>#}
# {#                            </v-row>#}
# {#                          </v-expansion-panel-content>#}
# {##}
# {#                        </v-expansion-panel>#}
# {#                      </v-expansion-panels>#}
