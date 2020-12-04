from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn import svm
from attacut import tokenize
from numpy import random
import pyrebase
import json

with open('model/config/database_new/firebase.json', encoding='utf8') as json_file:
    data = json.load(json_file)
    config = data['firebase']
    firebase = pyrebase.initialize_app(config)
    pb = pyrebase.initialize_app(config)
    db = firebase.database()



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
ref = db.child('requestDemo').get()
contracts = db.child('requestContract').get()
count = 1
demolist = []
contractlist = []
companys = []
group = {}
for demo in ref.each()[1:]:
    key = demo.key()
    company = demo.val()['event']['company']
    companys.append(company)
    email = demo.val()['event']['email']
    fname = demo.val()['event']['fname']
    product = demo.val()['event']['product']
    message = demo.val()['event']['message']
    tel = demo.val()['event']['tel']
    date = demo.val()['Date']
    time = demo.val()['Time']
    tag = demo.val()['tag']
    apiDemo = {'Index': count, 'key': key, 'Name': fname, 'Company': company, 'Email': email,
               'Product': product, 'Message': message, 'tel': tel, 'tag': tag, 'Time': time,
               'Date': date, 'Channel': 'web mango'}
    demolist.append(apiDemo)



# for contract in contracts.each()[1:]:
#     event = contract.val()['event']
#     contact_email = event['contact_email']
#     contact_email_div = event['contact_email_div']
#     contact_message = event['contact_message']
#     contact_name = event['contact_name']
#     contact_name_company = event['contact_name_company']
#     contact_subject = event['contact_subject']
#     contact_tel = event['contact_tel']
#     apiContract = {'key': }




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
