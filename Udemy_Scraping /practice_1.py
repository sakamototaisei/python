"""
Amazonサイトのスクレイピング練習
"""
import requests
from bs4 import BeautifulSoup


keyword = input('検索 : ')

url = 'https://www.amazon.co.jp/s?k=' + keyword
res = requests.get(url)
# print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')

elems = soup.select('div.s-main-slot.s-result-list.s-search-results.sg-row')
items = elems[0].find_all('')
print(items)

# for item in items:
#     print(item.span.string, end='\n\n')