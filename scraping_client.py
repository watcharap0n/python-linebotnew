from selenium import webdriver
import os
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys
from typing import Optional


def scarping_token(token, db, condition=False, start=Optional[None], end=Optional[None]):
    driver = webdriver.Chrome(os.path.abspath('chromedriver'))
    driver.get('https://datawarehouse.dbd.go.th')
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.add_cookie({"name": "JSESSIONID", "domain": "datawarehouse.dbd.go.th",
                       "value": token})
    driver.get('https://datawarehouse.dbd.go.th/index')
    driver.get('https://datawarehouse.dbd.go.th/searchJuristicInfo/41002/submitObjCode/1')
    time.sleep(1)
    select = driver.find_element_by_xpath('//*[@id="sortBy"]')
    select.click()
    time.sleep(1)
    option = driver.find_element_by_xpath('//*[@id="sortBy"]/option[5]')
    option.click()
    time.sleep(8)

    i = 1
    n_df = []

    if not condition:
        while True:
            try:
                status = db.child('selenium').get()
                print(status.val()['status'])
                if status.val()['status'] == 'stop':
                    db.child('status_bot').set({'status': 'finished'})
                    break
                else:
                    soup = BeautifulSoup(driver.page_source, 'lxml')
                    content = soup.find_all('table', {'id': 'fixTable'})
                    dfs = pd.read_html(str(content))
                    df = pd.DataFrame(dfs[0])
                    print(df)
                    n_df.append(df)
                    time.sleep(1)
                    btn_next = driver.find_element_by_xpath('//*[@id="next"]')
                    btn_next.click()
                    db.child('status_bot').set({'status': f'Page: {i}'})
                    time.sleep(7)
                    i += 1
            except:
                db.child('status_bot').set({'status': 'finished'})
                break
        result = pd.concat(n_df)
        print(result)
        result.to_excel('static/scraping.xlsx')
        db.child('status_bot').set({'status': 'finished'})
        driver.close()
        driver.quit()
    elif condition:
        page = driver.find_element_by_xpath('//*[@id="cPage"]')
        page.send_keys(Keys.ARROW_RIGHT)
        page.send_keys(Keys.BACKSPACE)
        page.send_keys(str(start))
        page.send_keys(Keys.ENTER)
        endPoint = int(end) - int(start)
        time.sleep(6)
        while i <= endPoint:
            try:
                status = db.child('selenium').get()
                print(status.val()['status'])
                if status.val()['status'] == 'stop':
                    db.child('status_bot').set({'status': 'finished'})
                    break
                else:
                    soup = BeautifulSoup(driver.page_source, 'lxml')
                    content = soup.find_all('table', {'id': 'fixTable'})
                    dfs = pd.read_html(str(content))
                    df = pd.DataFrame(dfs[0])
                    print(df)
                    n_df.append(df)
                    time.sleep(1)
                    btn_next = driver.find_element_by_xpath('//*[@id="next"]')
                    btn_next.click()
                    db.child('status_bot').set({'status': f'Page: {i}'})
                    time.sleep(7)
                    i += 1
            except:
                db.child('status_bot').set({'status': 'finished'})
                break
        result = pd.concat(n_df)
        print(result)
        result.to_excel('static/scraping.xlsx')
        db.child('status_bot').set({'status': 'finished'})
        driver.close()
        driver.quit()
