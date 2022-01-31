"""
Seleniumの基本
ブラウザの操作を実行してデータの取得を行う
抽出は遅くなる
"""
from re import X, search
from selenium import webdriver
from time import sleep
# Chromeをいちいち立ち上げないくて済むように
from selenium.webdriver.chrome.options import Options

import csv
import datetime



options = Options()
options.add_argument('--headless')
# ヘッドレスモードに変更(ブラウザを立ち上げずに実行する)
driver = webdriver.Chrome("/Users/sakamototaisei/Desktop/python/Udemy_Scraping /chromedriver", options=options)
driver.get('https://www.google.com/')

# Googleの検索欄の指定
search_bar = driver.find_element_by_name("q")
# textを送る
search_bar.send_keys('Python')
# エンターで検索を実行する
search_bar.submit()

# csvの日付に取得
csv_date = datetime.datetime.today().strftime('%Y%m%d')
csv_fille_name = 'goole_python_' + csv_date + '.csv'

# ファイルのオープン
f = open(csv_fille_name, 'w', encoding='utf_8_sig', errors='ignore')
writer = csv.writer(f, lineterminator='\n')
# ヘッダーの書き込み
csv_header = ['検索順位', 'タイトル', 'URL']
writer.writerow(csv_header)


i = 0
ranking = 1
while True:
    i += 1
    sleep(1)
    # サイトのタイトルの取得(xpath)
    for elem_h3 in driver.find_elements_by_xpath('//a/h3'):
        csv_list = []
        # 順位の格納
        csv_list.append(str(ranking))
        # タイトルの格納
        csv_list.append(elem_h3.text)
        # (..)は親要素という意味,今回ではa要素となる
        elem_a = elem_h3.find_element_by_xpath('..')
        # get_attribute(属性名)、属性名から属性値を取得,URLの格納
        csv_list.append(elem_a.get_attribute('href'))

        # リストに格納した一文を追加する
        writer.writerow(csv_list)

        ranking += 1

    # 次のページのリンクを取得
    next_link = driver.find_element_by_id('pnnext')
    driver.get(next_link.get_attribute('href'))

    if i > 4:
        break
f.close()

