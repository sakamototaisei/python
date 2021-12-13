"""
Requests : データの取得に使う

get()     : サーバーから情報を取得するのに使用
post()    : サーバー情報を登録する時に使用
put()     : サーバーの情報を更新する時に使用
delete()  : サーバーの情報を削除する時に使用
"""
import requests


response = requests.get('https://www.yahoo.co.jp/')
# ステータスコードの確認
print(response.status_code)
# rul先のwebページのhtmlを確認
# print(response.text)
# サーバーからのバイナリーデータの表示、これを人間の読めるものに変換したものが.textで表示されたもの
# print(response.content)
print(response.encoding)
# header情報が辞書型で
for key, value in response.headers.items():
    print(key, '   ', value)
# cookie見ている情報を保存されているのを表示する
print(response.cookies)

print('----------------')

# ユーザーエージェント
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'

header = {'user_agent': user_agent}
url = 'https://www.yahoo.co.jp/'
response = requests.get(url, headers=header)
print(response.status_code)
# タイムアウト3秒を指定している
response = requests.get(url, timeout=3)
print(response.text[:500])

print('----------------')

param = {'q': 'python'}
response = requests.get('https://www.google.com/search?q=python', params=param)
print(response.text)