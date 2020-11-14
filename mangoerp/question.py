from datetime import datetime
import requests
from bs4 import BeautifulSoup

class FAQ:
    whatever = ['คือ', 'อะไรอะ', 'คืออะไร', 'คือไร', 'คือไง', 'อิหยังวะ', 'อิหยัง']
    areSure = ['ไรงะ', 'หรอ', 'ใช่หรอ', 'งั้นหรอ', 'งะ']
    mango = ["แมงโก้", "แมงโก", "mango", "โก้"]


class TimeDate:
    day = datetime.today().day
    month = datetime.today().month
    second = datetime.today().second
    minute = datetime.today().minute
    hour = datetime.today().hour
    year = datetime.today().year


class TagChart:
    @staticmethod
    def group_chart(e, db2):
        i = db2.child('RestCustomer').child(e).get()
        profile = i.val()['Profile']
        cTime = i.val()['Time']
        cDate = i.val()['Date']
        company = i.val()['Company']
        email = i.val()['Email']
        pEmail = i.val()['EmailLiff']
        message = i.val()['Message']
        picture = i.val()['Picture']
        product = i.val()['Product']
        other = i.val()['Other']
        tel = i.val()['Tel']
        tag = i.val()['Tag']
        name = i.val()['Name']
        channel = i.val()['Channel']
        username = i.val()['Username']
        date = i.val()['DateInsert']
        time = i.val()['TimeInsert']
        group = {'Name': name, 'Product': product, 'Other': other, 'Company': company, 'Tel': tel, 'Email': email,
                 'EmailLiff': pEmail, 'Message': message, 'Profile': profile, 'Date': cDate, 'Time': cTime,
                 'Picture': picture, 'Username': username, 'DateInsert': date, 'TimeInsert': time, 'Tag': tag,
                 'Channel': channel}
        return group

    @staticmethod
    def push_database(e, username, date, time, db2):
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
                 'Picture': picture, 'Username': username, 'DateInsert': date, 'TimeInsert': time, 'Tag': tag,
                 'Channel': channel}
        return group

    @staticmethod
    def excel_liff(e, db2):
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
    def excel_demo(e, db2):
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
                 'Message': message, 'Date': cDate, 'Time': cTime, 'Tag': tag, 'Channel': 'web mango'}
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
        group = {'Name': name, 'Product': product, 'Other': '', 'Company': company,
                 'Tel': tel, 'Email': email, 'EmailLiff': '', 'Message': message,
                 'Profile': '', 'Date': cDate, 'Time': cTime, 'Picture': '',
                 'Username': username, 'DateInsert': date, 'TimeInsert': time, 'Tag': tag,
                 'Channel': 'web mango'}
        return group



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
                       'Date': date, 'Channel': 'web mango'}
            test.append(apiDemo)
            count += 1
        amount = len(test)
        return test, amount


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