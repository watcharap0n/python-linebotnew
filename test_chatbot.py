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


ref = db.child('requestDemo').get()
lst = []
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
    message = event['message']
    tel = event['tel']
    group = {'id': key, 'name': name, 'product': product, 'company': company, 'email': email,
             'message': message, 'tel': tel, 'date_time': f'{date} {time}', 'tag': tag}
    lst.append(group)

print(lst)











