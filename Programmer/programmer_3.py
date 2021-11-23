"""
独学プログラマー

第３部

Bash : コマンドラインインターフェース

フラグ : - や --に続けてフラグ名を書きます

隠しファイル : .〜で書く

パイプ : |あるコマンドの実行結果を別のコマンドの入力として渡すことができる

環境変数 : OSに値を記録しておくための変数(export 変数名 = 変数の値)

パーミッション(権限) : whoami
"""


"""
正規表現 : 連続した文字列の検索パターン定義
"""
import re

l = 'Beautiful is better than ugly.'
# findall()関数で見つけた部分をリスト化する、大文字小文字の違いを無視する場合は,３つ目の引数にre.IGNORECASEを渡す
matches = re.findall('beautiful', l, re.IGNORECASE)

print(matches)


print('----------------------')

# 前方一致と後方一致
zen = """Although never is
ofthen better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!"""

# 複数行のテキストを複数行として扱うためにre.MULTILINEフラグを使う
m = re.findall('^If', zen, re.MULTILINE)
print(m)


print('----------------------')

# 複数文字との一致
string = 'Two too'
# tで始まり、その次にoかwの文字が来て、次にoがくることを期待している
m = re.findall('t[ow]o', string, re.IGNORECASE)
print(m)


print('----------------------')

# 数値との一致
line = '123 hi 34 hello.'
m = re.findall('\d', line, re.IGNORECASE)
print(m)


print('----------------------')

#　繰り返し
t = '__one__ __two__ __three__'
found = re.findall('__.*?__', t)
for match in found:
    print(match)


print('----------------------')

# エスケープ
line = 'I love $'
m = re.findall('\\$', line, re.IGNORECASE)
print(m)