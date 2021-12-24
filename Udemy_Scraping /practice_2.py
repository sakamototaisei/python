import requests
from bs4 import BeautifulSoup
import time
import re


url = 'https://www.yahoo.co.jp/'
res = requests.get(url)
print(res.status_code)

soup = BeautifulSoup(res.text, 'html.parser')
elems = soup.find_all(href=re.compile('news.yahoo.co.jp/pickup'))

i = 1
pickcup_links = []
# print(elems)
for elem in elems:
    print(str(i), ':', elem.span.string)
    print(elem.attrs['href'], end='\n\n')
    pickcup_links.append(elem.attrs['href'])
    i += 1

j = 1

for pickup_link in pickcup_links:
    pickup_res = requests.get(pickup_link)
    pickup_soup = BeautifulSoup(pickup_res.text, 'html.parser')

    news_link = pickup_soup.find(href=re.compile('news.yahoo.co.jp/articles'))
    # print(news_link.attrs['href'])
    news_res = requests.get(news_link)
    news_soup = BeautifulSoup(news_res.text, 'html.parser')

    print(str(j), ':', news_soup.title.string)
    print(news_link)

    j += 1