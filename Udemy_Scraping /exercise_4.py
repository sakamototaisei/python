"""
Yahoo!
ニュースタイトル・URL一覧の取得
遷移後の情報の取得
"""
import requests
from bs4 import BeautifulSoup
import time
import re


url = 'https://www.yahoo.co.jp/'
res = requests.get(url)
# print(res.status_code)

soup = BeautifulSoup(res.text, 'html.parser')

elems = soup.find_all(href=re.compile('news.yahoo.co.jp/pickup'))
# print(elems)

i = 1
pickup_links = []
# 課題１の主要ニュースのタイトルとURLの取得と表示
for elem in elems:
    print(str(i), ':', elem.span.string)
    print(elem.attrs['href'], end='\n\n')
    pickup_links.append(elem.attrs['href'])
    i += 1

print('---------------------')

j = 1
# 課題２のリンクをたどって複数のページを遷移する
for pickup_link in pickup_links:
    pickup_res = requests.get(pickup_link)
    pickup_soup = BeautifulSoup(pickup_res.text, 'html.parser')
    pickup_elem = pickup_soup.select('.sc-eZbwru.hEUNkD')
    # print(j, ':', pickup_elem[0].attrs['href'])

    news_link = pickup_elem[0].attrs['href']
    news_res = requests.get(news_link)
    news_soup = BeautifulSoup(news_res.text, 'html.parser')

    # 遷移後のタイトル、URL、本文の表示
    print(str(j), ':', news_soup.title.string)
    print(news_link)

    detail_text = news_soup.find(class_=re.compile('yjSlinkDirectlink'))
    print(detail_text.text if hasattr(detail_text, 'text') else '', end='\n\n')
    j += 1

    time.sleep(2)