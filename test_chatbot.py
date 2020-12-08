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



d = {'Authorized': '123', 'Channel': 'LINE', 'Company': 'หจก.ยูงทองการโยธา', 'Date': '27-11-2020', 'DateInsert': '27-11-2020', 'Email': 'blacfatman101@gmail.com', 'EmailLiff': 'blacfatman101@gmail.com ', 'Message': 'None', 'Name': 'อมรเทพ', 'Other': '', 'Picture': 'https://profile.line-scdn.net/0hcExnuSbmPGpFFxW7u7ZDPXlSMgcyOToiPXZ7CmASN1w_Iy5vcCEmWGlFZFtpJH87fCIgDGQQYA9t', 'Position': 'วิศวกร', 'Product': 'แบ่งชำระ เบา เบา', 'Profile': 'Amornthep Riyaphan', 'Tax': 'test1', 'Tel': '0822970797', 'Time': '3:8:11', 'TimeInsert': '9:1:49', 'Username': 'tongta', 'datetime': '27-11-2020 3:8:11', 'datetime_insert': '27-11-2020 9:1:49', 'id': '-MN6TcOeSDhCZNuq9byO', 'tag': ['CJ010']}

print(d['Authorized'])

group = {'Authorized': d['Authorized'], 'Channel': d['Channel'], 'Company': d['Company'], 'Date': d['Date'], 'DateInsert': d['DateInsert'], 'Email': d['Email'], 'EmailLiff': d['EmailLiff'], 'Message': d['Message'], 'Name': d['Name'], 'Other': d['Other'], 'Picture': d['Picture'], 'Position': d['Position'], 'Product': d['Product'], 'Profile': d['Profile'], 'Tax': d['Tax'], 'Tel': d['Tel'], 'Time': d['Time'], 'TimeInsert': d['TimeInsert'], 'Username': d['Username'], 'datetime': d['datetime'], 'datetime_insert': d['datetime_insert'], 'id': d['id'], 'Tag': d['tag']}


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
