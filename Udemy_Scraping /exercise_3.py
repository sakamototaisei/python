"""
BeautifulSoupの基本演習
"""
from bs4 import BeautifulSoup


html = """
<html>
    <head>
        <title>清水義孝の著書</title>
    </head>
    <body>
        <p class="title">
            <b>清水義孝の最新の著書には、次の本があります。</b>
        </p>
        <p class="recent books">
            <a class="book" href="https://www.amazon.co.jp/dp/B07TN4D3HG" id="link1">Python3によるビジネスに役立つデータ分析入門</a>、
            <a class="book" href="http://www.amazon.co.jp/dp/B07SRLRS4M" id="link2">よくわかるPython3入門2.NumPy・Matplotlib編</a>、
            <a class="book" href="http://www.amazon.co.jp/dp/B07T9SZ96B" id="link3">よくわかるPython3入門4.Pandasでデータ分析編</a>
        </p>
        <p class="end">
            <b>そして、これらの本は好評発売中です。</b>
        </p>
    </body>
</html>
"""

# 課題１ 読み込み
soup = BeautifulSoup(html, 'html.parser')
# 課題２ 整形した形で表示
print(soup.prettify())
# 課題３ titleの表示
print(soup.title.string)
# 課題４ find_allメソッドで全てのaタグを取得し、表示
print(soup.find_all('a'))
for a_tag in soup.find_all('a'):
    # 課題５ a要素から、href属性の値とテキストを表示
    print(a_tag['href'])
    print(a_tag.string, end='\n\n')