from datetime import datetime
import datetime as tim
from bs4 import BeautifulSoup
import requests
import pandas as pd


class TimeDate:
    day = datetime.today().day
    month = datetime.today().month
    second = datetime.today().second
    minute = datetime.today().minute
    hour = datetime.today().hour
    year = datetime.today().year


class ButtonEvent:
    def __init__(self, loop, db, tag_insert):
        self.loop = loop
        self.db = db
        self.tag_insert = tag_insert
        self.tagChart = TagChart()

    def button_add(self, transaction, i, dict_key):
        self.db.child(transaction).child(i).update(dict_key)

    def button_tag(self, transaction, dict_key):
        for i in self.loop:
            self.db.child(transaction).child(i).update({dict_key: self.tag_insert})

    def button_tagInfo(self, transaction, dict_key, request_tag):
        for i in self.loop:
            self.db.child(transaction).child(i).update({dict_key: request_tag})

    def button_clean_tag(self, transaction, dict_key):
        for i in self.loop:
            self.db.child(transaction).child(i).update({dict_key: ''})

    def button_excel_import(self):
        toList = []
        for i in self.loop:
            list_excel = self.tagChart.import_excel(i, self.db)
            toList.append(list_excel)
        data = pd.DataFrame(toList)
        datatoexcel = pd.ExcelWriter('static/excel/newCustomers.xlsx', engine='xlsxwriter')
        data.to_excel(datatoexcel, sheet_name='Sheet1')
        datatoexcel.save()

    def button_excel_import_train(self):
        toList = []
        for i in self.loop:
            list_excel = self.tagChart.import_excel_train(i, self.db)
            toList.append(list_excel)
        data = pd.DataFrame(toList)
        datatoexcel = pd.ExcelWriter('static/excel/newCustomers.xlsx', engine='xlsxwriter')
        data.to_excel(datatoexcel, sheet_name='Sheet1')
        datatoexcel.save()

    def button_delete(self, transaction):
        for i in self.loop:
            self.db.child(transaction).child(i).remove()

    def button_excel_information(self):
        lst = []
        for i in self.loop:
            list_chart = self.tagChart.information_excel(i, self.db)
            lst.append(list_chart)
        data = pd.DataFrame(lst)
        datatoexcel = pd.ExcelWriter('static/excel/Customers.xlsx', engine='xlsxwriter')
        data.to_excel(datatoexcel, sheet_name='Sheet1')
        datatoexcel.save()

    def button_insert_import(self, displayName, date, time, db):
        for i in self.loop:
            group = self.tagChart.insert_to_information(i, displayName, date, time, db)
            self.db.child('RestCustomer').push(group)
            self.db.child('LineLiff').child(i).remove()

    def button_insert_getDemo(self, displayName, date, time, db):
        for i in self.loop:
            group = self.tagChart.chart_demo(i, displayName, date, time, db)
            self.db.child('RestCustomer').push(group)
            self.db.child('requestDemo').child(i).remove()

    def button_insert_getContract(self, displayName, date, time, db):
        for i in self.loop:
            group = self.tagChart.chart_contract(i, displayName, date, time, db)
            self.db.child('RestCustomer').push(group)
            self.db.child('requestContract').child(i).remove()

    def button_excel_getDemo(self):
        lst = []
        for i in self.loop:
            list_chart = self.tagChart.demo_excel(i, self.db)
            lst.append(list_chart)
        data = pd.DataFrame(lst)
        datatoexcel = pd.ExcelWriter('static/excel/Customers.xlsx', engine='xlsxwriter')
        data.to_excel(datatoexcel, sheet_name='Sheet1')
        datatoexcel.save()

    def button_excel_getContract(self):
        lst = []
        for i in self.loop:
            list_chart = self.tagChart.contract_excel(i, self.db)
            lst.append(list_chart)
        data = pd.DataFrame(lst)
        datatoexcel = pd.ExcelWriter('static/excel/Customers.xlsx', engine='xlsxwriter')
        data.to_excel(datatoexcel, sheet_name='Sheet1')
        datatoexcel.save()


class GetDateTime:
    def __init__(self, value, db):
        self.value = value
        self.db = db

    @classmethod
    def todo_date(cls, value, db):
        return cls(value, db)

    def get_date(self, user):
        return user.get(self.value)

    def get_dict_key(self, mydict, val):
        for key, value in mydict.items():
            if val == value:
                return key

    @staticmethod
    def len_amount(lst, key, value):
        return [x for x in lst if x[key] == value]

    @staticmethod
    def len_amount_other(lst):
        return [x for x in lst if x['channel'] != 'LINE' and x['channel'] != 'GetDemo']

    @staticmethod
    def dynamic_month(foo, months):
        return [i for i in foo for month in months if i['month_check'] == month]

    @staticmethod
    def dynamic(lst, value, condition):
        return [i for i in lst if i[value] == condition]

    @staticmethod
    def dynamic_tag(lst, value):
        return [i for i in lst for e in i['tag'] for v in value if e == v]

    @staticmethod
    def dynamic_product_channel(lst, condition_channel, condition_product):
        return [i for i in lst if i['channel'] == condition_channel and i['product'] == condition_product]

    @staticmethod
    def dynamic_product_dates(dates, foo, condition):
        return [result for date in dates for result in foo if date == result['date'] and result['product'] == condition]

    @staticmethod
    def dynamic_product_dates_channel(dates, foo, condition_product, condition_channel):
        return [result for date in dates for result in foo if
                date == result['date'] and result['product'] == condition_product and result[
                    'channel'] == condition_channel]

    @staticmethod
    def dynamic_date_channel(dates, foo, condition_channel):
        return [result for date in dates for result in foo if
                date == result['date'] and result['channel'] == condition_channel]

    @staticmethod
    def dynamic_dates(dates, foo):
        return [result for date in dates for result in foo if date == result['date']]

    def data_datetime(self, transaction):
        foo = []
        cut_channels = []
        cut_products = []
        cut_tags = []
        ref = self.db.child(transaction).get()
        for i in ref.each()[1:]:
            v = i.val()
            date = v['date']
            time = v['time']
            fname = v['name']
            company = v['company']
            product = v['product']
            channel = v['channel']
            message = v['message']
            Img = v['picture']
            email = v['email']
            tel = v['tel']
            tag = v['tag']
            emailliff = v['emailliff']
            username = v['username']
            time_insert = v['time_insert']
            date_insert = v['date_insert']
            profile = v['profile']
            for t in tag:
                cut_tags.append(t)
            cut_channels.append(channel)
            cut_products.append(product)
            d = tim.datetime.strptime(date, '%d-%m-%Y')
            t = tim.datetime.strptime(time, '%H:%M:%S')
            mapProduct = {'name': fname, 'tag': tag, 'company': company, 'product': product, 'channel': channel,
                          'day': d.day, 'month': d.month, 'year': d.year, 'date': date, 'time': time,
                          'message': message, 'img': Img, 'id': i.key(), 'email': email, 'profile': profile,
                          'datetime_insert': f'{date_insert} {time_insert}', 'month_check': f'{d.year}-{d.month}',
                          'tel': tel, 'emailliff': emailliff, 'username': username, 'datetime': f'{date} {time}'}
            foo.append(mapProduct)
        return foo, cut_products, cut_channels, cut_tags


class TagChart:
    @staticmethod
    def information_excel(key, db2):
        i = db2.child('RestCustomer').child(key).get()
        profile = i.val()['profile']
        cTime = i.val()['time']
        cDate = i.val()['date']
        company = i.val()['company']
        email = i.val()['email']
        pEmail = i.val()['emailliff']
        message = i.val()['message']
        picture = i.val()['picture']
        product = i.val()['product']
        other = i.val()['other']
        tel = i.val()['tel']
        tag = i.val()['tag']
        name = i.val()['name']
        channel = i.val()['channel']
        username = i.val()['username']
        date = i.val()['date_insert']
        time = i.val()['time_insert']
        authorized = i.val()['authorized']
        position = i.val()['position']
        tax = i.val()['tax']
        group = {'Name': name, 'Product': product, 'Other': other, 'Company': company, 'Tel': tel, 'Email': email,
                 'EmailLiff': pEmail, 'Message': message, 'Profile': profile, 'Date': cDate, 'Time': cTime,
                 'Picture': picture, 'Username': username, 'DateInsert': date, 'TimeInsert': time, 'Tag': tag,
                 'Channel': channel, 'Tax': tax, 'Authorized': authorized, 'Position': position}
        return group

    @staticmethod
    def import_excel(e, db2):
        py = db2.child('LineLiff').child(e).get()
        day = py.val()['day']
        month = py.val()['month']
        year = py.val()['year']
        hour = py.val()['hour']
        minn = py.val()['min']
        sec = py.val()['sec']
        tag = py.val()['tag']
        event = py.val()['event']
        channel = py.val()['channel']
        comment = event['comment']
        company = event['company']
        displayName = event['displayName']
        email = event['email']
        name = event['firstname']
        picture = event['picture']
        product = event['product']
        tel = event['tel']
        other = event['other']
        token = event['token']
        group = {'Name': name, 'Product': product, 'Other': other, 'Company': company,
                 'Tel': tel, 'Email': email, 'EmailLiff': token, 'Message': comment,
                 'Profile': displayName, 'Date': (f'{day}-{month}-{year}'), 'Time': (f'{hour}:{minn}:{sec}'),
                 'Picture': picture, 'Tag': tag,
                 'Channel': channel}
        return group

    @staticmethod
    def import_excel_train(e, db):
        py = db.child('trainCustomer').child(e).get()
        day = py.val()['day']
        month = py.val()['month']
        year = py.val()['year']
        hour = py.val()['hour']
        minn = py.val()['min']
        sec = py.val()['sec']
        tag = py.val()['tag']
        event = py.val()['event']
        channel = py.val()['channel']
        comment = event['comment']
        company = event['company']
        displayName = event['displayName']
        email = event['email']
        name = event['firstname']
        picture = event['picture']
        tel = event['tel']
        token = event['token']
        new = event['news']
        position = event['position']
        group = {'Name': name, 'Company': company,
                 'Tel': tel, 'Email': email, 'EmailLiff': token, 'Message': comment, 'New': new,
                 'Profile': displayName, 'Date': (f'{day}-{month}-{year}'), 'Time': (f'{hour}:{minn}:{sec}'),
                 'Picture': picture, 'Tag': tag, 'Position': position,
                 'Channel': channel}
        return group

    @staticmethod
    def import_excel_all(db2):
        ref = db2.child('LineLiff').get()
        toList = []
        for py in ref.each()[1:]:
            day = py.val()['day']
            month = py.val()['month']
            year = py.val()['year']
            hour = py.val()['hour']
            minn = py.val()['min']
            sec = py.val()['sec']
            tag = py.val()['tag']
            event = py.val()['event']
            channel = py.val()['channel']
            comment = event['comment']
            company = event['company']
            displayName = event['displayName']
            email = event['email']
            name = event['firstname']
            picture = event['picture']
            product = event['product']
            tel = event['tel']
            other = event['other']
            token = event['token']
            group = {'Name': name, 'Product': product, 'Other': other, 'Company': company,
                     'Tel': tel, 'Email': email, 'EmailLiff': token, 'Message': comment,
                     'Profile': displayName, 'Date': (f'{day}-{month}-{year}'), 'Time': (f'{hour}:{minn}:{sec}'),
                     'Picture': picture, 'Tag': tag,
                     'Channel': channel}
            toList.append(group)
        return toList

    @staticmethod
    def information_excel_all(db2):
        ref = db2.child('RestCustomer').get()
        toList = []
        for i in ref.each()[1:]:
            profile = i.val()['profile']
            cTime = i.val()['time']
            cDate = i.val()['date']
            company = i.val()['company']
            email = i.val()['email']
            pEmail = i.val()['emailliff']
            message = i.val()['message']
            picture = i.val()['picture']
            product = i.val()['product']
            tag = i.val()['tag']
            tel = i.val()['tel']
            name = i.val()['name']
            username = i.val()['username']
            ImportDate = i.val()['date_insert']
            ImportTime = i.val()['time_insert']
            authorized = i.val()['authorized']
            position = i.val()['position']
            tax = i.val()['tax']
            group = {'Name': name, 'Product': product, 'Company': company, 'Tel': tel, 'Email': email,
                     'EmailLiff': pEmail, 'Message': message, 'Profile': profile, 'Date': cDate, 'Time': cTime,
                     'Picture': picture, 'Username': username, 'Tag': tag,
                     'ImportDate/Time': f'{ImportDate} {ImportTime}', 'Tax': tax, 'Authorized': authorized,
                     'Position': position}
            toList.append(group)
        return toList

    @staticmethod
    def demo_excel_all(db2):
        ref = db2.child('requestDemo').get()
        toList = []
        for i in ref.each()[1:]:
            cTime = i.val()['Time']
            cDate = i.val()['Date']
            company = i.val()['event']['company']
            email = i.val()['event']['email']
            message = i.val()['event']['message']
            product = i.val()['event']['product']
            tel = i.val()['event']['tel']
            tag = i.val()['tag']
            name = i.val()['event']['fname']
            group = {'Name': name, 'Product': product, 'Other': '', 'Company': company, 'Tel': tel, 'Email': email,
                     'Message': message, 'Date': cDate, 'Time': cTime, 'Tag': tag, 'Channel': 'GetDemo'}
            toList.append(group)
        return toList

    @staticmethod
    def demo_excel(e, db2):
        i = db2.child('requestDemo').child(e).get()
        cTime = i.val()['Time']
        cDate = i.val()['Date']
        company = i.val()['event']['company']
        email = i.val()['event']['email']
        message = i.val()['event']['message']
        product = i.val()['event']['product']
        tel = i.val()['event']['tel']
        tag = i.val()['tag']
        name = i.val()['event']['fname']
        group = {'Name': name, 'Product': product, 'Other': '', 'Company': company, 'Tel': tel, 'Email': email,
                 'Message': message, 'Date': cDate, 'Time': cTime, 'Tag': tag, 'Channel': 'GetDemo'}
        return group

    @staticmethod
    def contract_excel(e, db2):
        contract = db2.child('requestContract').child(e).get()
        event = contract.val()['event']
        contact_email = event['contact_email']
        contact_message = event['contact_message']
        contact_name = event['contact_name']
        contact_name_company = event['contact_name_company']
        contact_subject = event['contact_subject']
        contact_tel = event['contact_tel']
        cdate = contract.val()['Date']
        ctime = contract.val()['Time']
        tag = contract.val()['tag']
        group = {'Name': contact_name, 'Product': contact_subject, 'Company': contact_name_company, 'Tel': contact_tel,
                 'Email': contact_email,
                 'Message': contact_message, 'Date': cdate, 'Time': ctime, 'Tag': tag, 'Channel': 'ติดต่อเรา'}
        return group

    @staticmethod
    def insert_to_information(e, username, date, time, db2):
        py = db2.child('LineLiff').child(e).get()
        day = py.val()['day']
        month = py.val()['month']
        year = py.val()['year']
        hour = py.val()['hour']
        minn = py.val()['min']
        sec = py.val()['sec']
        tag = py.val()['tag']
        event = py.val()['event']
        channel = py.val()['channel']
        comment = event['comment']
        company = event['company']
        displayName = event['displayName']
        email = event['email']
        name = event['firstname']
        picture = event['picture']
        product = event['product']
        tel = event['tel']
        other = event['other']
        token = event['token']
        group = {'name': name, 'product': product, 'other': other, 'company': company,
                 'tel': tel, 'email': email, 'emailliff': token, 'message': comment,
                 'profile': displayName, 'date': (f'{day}-{month}-{year}'), 'time': (f'{hour}:{minn}:{sec}'),
                 'picture': picture, 'username': username, 'date_insert': date, 'time_insert': time, 'tag': tag,
                 'channel': channel, 'tax': '', 'authorized': '', 'position': ''}
        return group

    @staticmethod
    def chart_demo(key, username, date, time, db2):
        i = db2.child('requestDemo').child(key).get()
        cTime = i.val()['Time']
        cDate = i.val()['Date']
        company = i.val()['event']['company']
        email = i.val()['event']['email']
        message = i.val()['event']['message']
        product = i.val()['event']['product']
        tel = i.val()['event']['tel']
        tag = i.val()['tag']
        name = i.val()['event']['fname']
        group = {'name': name, 'product': product, 'other': '', 'company': company,
                 'tel': tel, 'email': email, 'emailliff': '', 'message': message,
                 'profile': '', 'date': cDate, 'time': cTime, 'picture': '',
                 'username': username, 'date_insert': date, 'time_insert': time, 'tag': tag,
                 'channel': 'GetDemo', 'tax': '', 'authorized': '', 'position': ''}
        return group

    @staticmethod
    def chart_contract(key, username, date, time, db2):
        contract = db2.child('requestContract').child(key).get()
        event = contract.val()['event']
        contact_email = event['contact_email']
        contact_message = event['contact_message']
        contact_name = event['contact_name']
        contact_name_company = event['contact_name_company']
        contact_subject = event['contact_subject']
        contact_tel = event['contact_tel']
        cdate = contract.val()['Date']
        ctime = contract.val()['Time']
        tag = contract.val()['tag']
        group = {'name': contact_name, 'product': contact_subject, 'other': '', 'company': contact_name_company,
                 'tel': contact_tel, 'email': contact_email, 'emailliff': '', 'message': contact_message,
                 'profile': '', 'date': cdate, 'time': ctime, 'picture': '',
                 'username': username, 'date_insert': date, 'time_insert': time, 'tag': tag,
                 'channel': 'contact', 'tax': '', 'authorized': '', 'position': ''}
        return group

    @staticmethod
    def get_link(x):
        message = 'link'
        profile = '[ตัวลิงค์จะไม่สามารถได้ชื่อคน]'
        stf = datetime.today()
        stff = stf.strftime('%B')
        day = datetime.today().day
        month = datetime.today().month
        second = datetime.today().second
        minute = datetime.today().minute
        hour = datetime.today().hour
        year = datetime.today().year
        result = {'profile': profile, 'message': message, 'reply': x, 'hour': hour, 'min': minute,
                  'sec': second, 'day': day, 'month': month, 'year': year, 'now': stff}
        return result

    @staticmethod
    def req_path(tag, ref, upper, db2):
        tags = ['CB010', 'CC010', 'CG010', 'CI010', 'CJ010', 'CM010',
                'CF010', 'CP010', 'CE010', 'CH010', 'CK010', 'CN010', 'CD010',
                'RC010', 'RA010', 'RB010']
        lst = []
        eCount = 1
        fire = FirebaseNewCustomer(db2)
        getDemo = fire.demoCustomer()
        information = fire.restCustomer()
        _import = fire.liffCustomer()
        len_getDemo = len(getDemo)
        len_information = len(information)
        len_import = len(_import)
        for i in ref.each()[1:]:
            if tag in i.val()[upper]:
                k = i.key()
                user = dict(i.val())
                user.update({'index': str(eCount), 'key': k})
                lst.append(user)
                eCount = eCount + 1
        data = {
            'lst': lst,
            'tag': tags,
            'amount_getDemo': len_getDemo,
            'amount_information': len_information,
            'amount_import': len_import,
        }
        return data

    @staticmethod
    def req_path_list(tag, ref, upper, db2):
        tags = ['CB010', 'CC010', 'CG010', 'CI010', 'CJ010', 'CM010',
                'CF010', 'CP010', 'CE010', 'CH010', 'CK010', 'CN010', 'CD010',
                'RC010', 'RA010', 'RB010']
        lst = []
        eCount = 1
        fire = FirebaseNewCustomer(db2)
        getDemo = fire.demoCustomer()
        information = fire.restCustomer()
        _import = fire.liffCustomer()
        len_getDemo = len(getDemo)
        len_information = len(information)
        len_import = len(_import)
        for i in ref.each()[1:]:
            for a in tag:
                if a in i.val()[upper]:
                    k = i.key()
                    user = dict(i.val())
                    user.update({'index': str(eCount), 'key': k})
                    lst.append(user)
                    eCount = eCount + 1
                    break
        data = {
            'lst': lst,
            'tag': tags,
            'amount_getDemo': len_getDemo,
            'amount_information': len_information,
            'amount_import': len_import,
        }
        return data


class FirebaseAPI:
    def __init__(self, db):
        self.db = db

    def popChip(self, transaction, id, tag, value):
        ref = self.db.child(transaction).child(id).get().val()[tag]
        x = value
        y = ''.join(x)
        count = 0
        for i in ref:
            toCount = ref[count]
            if y == toCount:
                ref.pop(count)
            count += 1
        if ref:
            final = self.db.child(transaction).child(id).update({'tag': ref})
        else:
            final = self.db.child(transaction).child(id).update({'tag': ''})
        return print(final)

    def groupToInsert(self, d, value):
        group = {'authorized': d['authorized'], 'channel': d['channel'],
                 'company': d['company'], 'date': d['date'], 'date_insert': d['date_insert'],
                 'email': d['email'], 'emailliff': d['emailliff'], 'message': d['message'],
                 'name': d['name'], 'other': d['other'], 'picture': d['picture'], 'position': d['position'],
                 'product': d['product'], 'profile': d['profile'], 'tax': d['tax'], 'tel': d['tel'],
                 'time': d['time'], 'time_insert': d['time_insert'], 'username': d['username'],
                 'datetime': d['datetime'], 'datetime_insert': d['datetime_insert'], 'id': d['id'], 'tag': value}
        return group

    def information(self, transaction):
        lst = []
        lst_date = []
        products = []
        lst_time = []
        ref = self.db.child(transaction).get()
        for i in ref.each()[1:]:
            key = i.key()
            name = i.val()['name']
            tag = i.val()['tag']
            profile = i.val()['profile']
            channel = i.val()['channel']
            company = i.val()['company']
            other = i.val()['other']
            email = i.val()['email']
            liff = i.val()['emailliff']
            picture = i.val()['picture']
            position = i.val()['position']
            tax = i.val()['tax']
            tel = i.val()['tel']
            time = i.val()['time']
            lst_time.append(time)
            date = i.val()['date']
            lst_date.append(date)
            message = i.val()['message']
            authorized = i.val()['authorized']
            date_insert = i.val()['date_insert']
            time_insert = i.val()['time_insert']
            username = i.val()['username']
            product = i.val()['product']
            products.append(product)
            group = {
                'id': key, 'name': name, 'tag': tag, 'product': product, 'email': email, 'other': other,
                'emailliff': liff, 'company': company, 'tel': tel, 'channel': channel, 'message': message,
                'profile': profile, 'picture': picture, 'username': username, 'time': time, 'date': date,
                'date_insert': date_insert, 'time_insert': time_insert, 'datetime': f'{date} {time}',
                'position': position, 'tax': tax, 'authorized': authorized,
                'datetime_insert': f'{date_insert} {time_insert}'
            }
            lst.append(group)
        return lst[::-1], lst_time, lst_date, products

    def requestDemo(self, transaction):
        ref = self.db.child(transaction).get()
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


class FirebaseCustomer:
    def __init__(self, db):
        self.db = db

    def importCustomer(self):
        by = []
        count = 1
        ref = self.db.child('trainCustomer').get()
        for r in ref.each()[1:]:
            key = r.key()
            users = r.val()
            users = dict(users)
            users.update({'index': str(count), 'key': key})
            by.append(users)
            count += 1
        return by


class FirebaseNewCustomer:
    def __init__(self, db):
        self.db = db

    def restCustomer(self):
        rest = self.db.child('RestCustomer').get()
        by = []
        count = 1
        for r in rest.each()[1:]:
            k = r.key()
            users = r.val()
            users = dict(users)
            users.update({'index': str(count), 'key': k})
            by.append(users)
            count += 1
        return by

    def liffCustomer(self):
        by = []
        eCount = 1
        ref = self.db.child('LineLiff').get()
        for e in ref.each()[1:]:
            k = e.key()
            users = e.val()
            users = dict(users)
            users.update({'index': str(eCount), 'key': k})
            by.append(users)
            eCount = eCount + 1
        return by

    def lenLIFF(self):
        ref = self.db.child('LineLiff').get()
        lst = []
        for e in ref.each()[1:]:
            lst.append(e.val())
        return len(lst)

    def demoCustomer(self):
        test = []
        ref = self.db.child('requestDemo').get()
        count = 1
        for demo in ref.each()[1:]:
            key = demo.key()
            company = demo.val()['event']['company']
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
                       'Date': date, 'Channel': 'GetDemo'}
            test.append(apiDemo)
            count += 1
        return test

    def contractCustomer(self):
        lst = []
        contracts = self.db.child('requestContract').get()
        count = 1
        for contract in contracts.each()[1:]:
            key = contract.key()
            event = contract.val()['event']
            contact_email = event['contact_email']
            contact_email_div = event['contact_email_div']
            contact_message = event['contact_message']
            contact_name = event['contact_name']
            contact_name_company = event['contact_name_company']
            contact_subject = event['contact_subject']
            contact_tel = event['contact_tel']
            date = contract.val()['Date']
            time = contract.val()['Time']
            tag = contract.val()['tag']
            apiContract = {'Index': count, 'key': key, 'tag': tag, 'Email': contact_email,
                           'email_div': contact_email_div, 'Message': contact_message, 'Name': contact_name,
                           'Company': contact_name_company, 'Product': contact_subject, 'tel': contact_tel,
                           'date_time': f'{date} {time}', 'Channel': 'Contract'}
            count += 1
            lst.append(apiContract)
        return lst

    def lenProduct(self, db, product):
        lst = []
        ref = self.db.child(db).get()
        for i in ref.each()[1:]:
            lst.append(i.val()['product'])
        result = [x for x in lst if product in x]
        return result

    def post_marketing_update(self, id, channel, comment, company, tag,
                              displayName, other, email, firstname, product, tel, token):
        ref = self.db.child('LineLiff').child(id).get()
        userId = ref.val()['event']['userId']
        picture = ref.val()['event']['picture']
        groupBy = {'tag': tag,
                   'event': {'channel': channel, 'comment': comment, 'company': company, 'displayName': displayName,
                             'email': email, 'firstname': firstname, 'other': other, 'product': product,
                             'tel': tel, 'token': token, 'userId': userId, 'picture': picture}}
        return groupBy


class WebScraping:
    @classmethod
    def humility(cls):
        r = requests.get("https://weather.com/weather/today/l/13.72,100.40?par=google&temp=c")
        soup = BeautifulSoup(r.content, "html.parser")
        temp = soup.find('span', {'data-testid': 'TemperatureValue'})
        feelLike = soup.find('div', {'data-testid': 'FeelsLikeSection'})
        HighLow = soup.find('div', {'data-testid': 'WeatherDetailsLabel'})
        valueTemp = soup.find('div', {'data-testid': 'wxData'})
        humility = soup.find('span', {'data-testid': 'PercentageValue'})
        x = 'Temperature : {}\n{}\n{}  {}\nHumidity  {}'.format(temp.text, feelLike.text, HighLow.text, valueTemp.text,
                                                                humility.text)
        return x

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


class FAQ:
    whatever = ['คือ', 'อะไรอะ', 'คืออะไร', 'คือไร', 'คือไง', 'อิหยังวะ', 'อิหยัง']
    areSure = ['ไรงะ', 'หรอ', 'ใช่หรอ', 'งั้นหรอ', 'งะ']
    mango = ["แมงโก้", "แมงโก", "mango", "โก้"]
