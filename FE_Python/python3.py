"""基本情報技術者 Python 対策"""

# 2進数=>10進数は先頭に0b
print(0b11)

# 8進数=>10進数は先頭に0o
print(0o11)

# 16進数=>10進数は先頭に0x
print(0x11)

print('----------------------------------')

# 10進数=>2進数
print(bin(3))

# 10進数=>8進数
print(oct(9))

# 10進数=>16進数
print(hex(17))

print('----------------------------------')


"""
代表的な文字列のメソッド

str.lstrip()        文字列の先頭の空白文字を除去する
str.rstrip()        文字列の末尾の空白文字を除去する
str.strip()         文字列の先頭及び末尾の空白文字を除去する
str.lower()         文字列の大文字を全て小文字にする
str.upper()         文字列の小文字を大文字にする
str.split(sep)      文字列をsepを区切り文字にして分割し、リストにする
"""

s = 'hello'
s1 = 'HELLO'
s2 = ' sakatai '
s3 = 'My name is sakatai'


print(s2.lstrip())
print(s2.rstrip())
print(s2.strip())
print(s1.lower())
print(s.upper())

l = s3.split(' ')
print(l)

print('----------------------------------')


"""
リストの主なメソッド

list.append()           リストの末尾に要素を1つ追加する
list.extend(iterable)   イテレーターを示す変数の全ての要素を対象の要素に追加し、リストを拡張する
list.insert(i, x)       添字のiで指定した位置に要素をxに挿入する
list.remove(x)          リストの中でxと等しい値を持つ最初の要素を削除する。該当する要素がなければValueErrorとなる
list.pop([i])           添字のiの位置にある要素をリストから削除し、その要素返す。添字を指定しないlist.pop()はリストの末尾の要素を追加して返す。
list.clear()            リストの中の全ての要素を削除する
list.index(x)           リストの中でxと等しい値を持つ最初の要素の位置をゼロから始まる添字で返す。該当する要素がなければValueErrorとなる
list.count(x)           リストでのxの出現回数を返す
list.sort(key, reverse) リストの項目をインプレース演算でソートする。key, reverseはオプションの引数で、ソート方法のカスタマイズに使用できる
list.reverse()          リストの要素をインプレース演算で逆順にする
"""


l = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

l.append(11)
print(l)

l.extend(l2)
print(l)

l.insert(2, 'sakatai')
print(l)

l.remove('sakatai')
print(l)

l.pop()
print(l)

print(l2)
l2.clear()
print(l2)

print(l.index(11))

print(l.count(11))

l.sort()
print(l)

l.reverse()
print(l)

del l[0]
print(l)

del l[2:5]
print(l)

del l[:]
print(l)


print('----------------------------------')


a, b, c = 10, 5, 100

if a > b > c:
    print('OK')
else:
    print('NO')

l = list(range(1, 10, 3))

print(l)

# リスト内包表記
l2 = [i for i in range(1,100) if i % 5 == 0]
print(l2)

# while True:
#     pass


squares = [n**2 for n in range(1, 6) if n % 2 == 1]
print(squares)


# 多重ループ

alpha_list = ['A', 'B', 'C']
num_list  = [1, 2, 3]

for alpha in alpha_list:
    for num in num_list:
        if alpha == 'B':
            break
        elif num == 2:
            continue
        print(alpha, num)


print('----------------------------------')

multiple = []
for i in range(1, 4):
    for j in range(1,4):
        print(i * j)


print('----------------------------------')


for i in range(1, 8, 1):
    print(i)

print('----------------------------------')


"""
ファイルの入出力

r       読み込み専用
w       新規の書き込み専用。既存ファイルがあれば切り詰めて新しく書き込まれる
x       新規作成。すでにファイルなどがあると失敗する
a       既存ファイルの末尾に追記
t       文字などのテキストエディタをテキストモードで扱う
b       画像などのバイナリデータをバイナリーモードで扱う
+       読み書きの両方を行う場合に使用
"""

print('----------------------------------')

"""
例外処理

try:
    通常行う処理
except 特定の例外処理:
    特定の例外が発生したとき行う処理
"""

# try:
#     d = int(input('数字を入力してください'))
#     print(d * 2)
# except ValueError:
#     print('それは数字ではありません')
# finally:
#     print('処理を終了します')



with open('sample.txt', 'w') as f:
    f.write('25')

try:
    with open('sample.txt', 'r') as f:
        line = f.readline()
        num = int(line)
except OSError:
    print('OSのエラーです')
except (ValueError, ZeroDivisionError, TypeError):
    print('数値演算のエラーです')
except Exception:
    print('通常のエラーです')
# 例外が発生しなかった時の処理
else:
    print('結果は{}歳です'.format(num))


print('----------------------------------')


# 特定の例外を発生させる方法 raise エラー名

try:
    raise ValueError('値のエラー')
except ValueError as msg:
    print('{}という例外なのです'.format(msg))


# 自作のエラーを作成できる
class AnonymousError(Exception):
    pass

try:
    raise AnonymousError
except AnonymousError:
    print('AnonymousErrorというエラーです')


print('----------------------------------')

"""
Python標準ライブラリ

string          文字列操作を行う
re              正規表現を使用する
datetime        日付や時間を扱う
time            時刻やデータへのアクセスと変換
calender        カレンダーを扱う
math            数学関数
decima          固定および浮動小数点の演算
random          擬似乱数の生成
statistics      数理統計関数
os              OSに依存する機能を利用する
os.path         OS共通のディレクトリ操作
shutil          高水準のファイル操作
sqlite3         SQLLiteデータベースに対するAPIインターフェース
zlib            gzip互換の圧縮
zipfile         ZIPファイルの処理
csv             CSVの読み書き
hashlib         セキュアハッシュ及びメッセージダイジェスト
hmac            メッセージ認証のために鍵付きハッシュ化
logging         Python用のロギング機能
socket          ネットワークインターフェース
ssl             TLS/SSLを利用
email           電子メールとMIME処理のためのパッケージ
json            JSONエンコーダー及びデコーダー
base64          Base16 Base32 Base64 Base85 データの符号化
html            HTMLのサポート
http            HTTPモジュール群
xml             XLMモジュール群
cgi             CGIのサポート
urllib          URLを扱うモジュール群
sys             システムを操作
warnings        警告の表示を制御する
"""


import requests
url = "https://www.udemy.com"
# requests.get(変数名)でwebページにアクセスする
response = requests.get(url)
# status_codesは正常に通信されたかを表すコードを返す
print(response.status_code)


print('----------------------------------')

# セキュリティ

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"Secret!")
print(token)
print(f.decrypt(token))