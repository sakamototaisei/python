""""
BeautifulSoupで読売新聞オンラインからニュースを取得

"""
import requests
from bs4 import BeautifulSoup


url = 'https://www.yomiuri.co.jp/'
res = requests.get(url)
# リクエストを送り確認
print(res.status_code)
print('---------------------', end='\n\n')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')

elems = soup.select('div.home-2020-prime-headline > ul[data-category="総合"]')
elems_news = elems[0].find_all('h3')

i = 1
for elem in elems_news:
    print(str(i), ':', elem.a.string)
    print(elem.a['href'], end='\n\n')
    i += 1