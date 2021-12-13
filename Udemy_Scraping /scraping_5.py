"""
BeautifulSoup(解析対象のHTML/XML, 利用するパーサー)
パーサー
html.parser : 追加ライブラリが不要
lxml        : 高速に処理ができる
xml         : XMLに太陽し、高速の処理ができる
html5lib    : 正しくHTML5を処理できる

情報の抽出方法
・HTML階層を移動して、HTMLタグの該当する左書を検索
・find, find_allメソッドにより、HTMLタグの該当すsルカ書を検索
・selectメソッドにより、CSSセレクタで該当する箇所を指定
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

soup = BeautifulSoup(html, 'html.parser')
print(soup)
# 階層化して表示する
print(soup.prettify())

print('-----------------------')

print(soup.html.head.title)
print(soup.title)
print(soup.title.string)
print(soup.title.name)
print(type(soup.title))
print(type(soup))

print('-----------------------')
# 最初のp要素を取得している
print(soup.body.p)
# 次の要素を取得している
print(soup.body.p.next_sibling.next_sibling.a.string)
print(soup.body.p.next_sibling.next_sibling.a['href'])

print('-----------------------')

# 引数に一致する最初find() 全部find_all() 何もなければNone
# print(soup.find_all('a'))

for tag_a in soup.find_all('a'):
    print(tag_a.string)
    print(tag_a['href'], end='\n\n')

print('-----------------------')

# soup.select('CSSセレクタ')取得できたタグをリストで返す、なければ殻のリストで返す
print(soup.select('body > p.end > b')[0].string)
