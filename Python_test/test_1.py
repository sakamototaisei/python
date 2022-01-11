"""
1: Pythonインタプリタの中で存在するもの
IPython

2: 対話型環境でのヒストリ情報が保存されているファイルは
.python_history

3: コマンドライン引数を取得するためのモジュール
sys

4: sys.pathで初期化で参照されないもの
スクリプトが存在するフォルダのシンボリックリンク先

5: バイナリデータレコードの処理を行うモジュール
struct

6: 仮想環境にインストールされたすべてのパッケージを表示するpipオプション
pip list

7: クリーンアップ動作を定義してあるオブジェクトに対して、クリーンアップ動作を保証した形で利用するための構文
with

8: コンパイル済Pythonファイルの拡張子
pyc

9: Pythonの変数に関する記述
関数内で変数に代入を行うと、その値がローカル変数のシンボル表に記録される

10: ログを取得するためのモジュール
logging

11: 対話モード時に、最後に表示した式を格納している
変数: _

12: ビルドイン関数dir()について
モジュールが定義している名前を確認することができる

13: Pythonにおけるタブ補完について
変数とモジュール名の補完はインタプリタの起動時に自動で有効になっており、[Tab]キーで補完機能が呼び出せる

14: 条件についての説明
比較はブール演算のandおよびorによって組み合わせることができ、また比較の結論はnotにより否定できる。
これらの優先順位は比較演算子よりも高い

15: Pythonの関数について正しいもの
関数をコールするときは、必ず位置引数が先でキーワード引数を後にしなければならない。

16: mutableなもの(値を変更できるオブジェクトのこと)
リスト

17: 仮想環境を生成、管理するのに使われているスクリプト
pyvenv

18: 

"""

def dive_info_code(teacher, L=[]):
    L.append(teacher)
    return L

print(dive_info_code('Noro'))
print(dive_info_code('Nakao'))
print(dive_info_code('Miyashita'))


print('---------------------------------')


from datetime import date

now = date.today()
print(now)


print('---------------------------------')


for i in range(20):
    if i % 3 == 0:
        print('{}は3で割り切れます'.format(i), end=' ')
    elif i > 8 and i % 2 == 0:
        break
    else:
        continue
print()


print('---------------------------------')


i = 10

def num(arg=i):
    print(arg)

i = 7

num()


print('---------------------------------')


import reprlib
# reprlibは表示させる文字集を制限し、setは重複を許さず、順序は保証しない
print(reprlib.repr(set('diveintcode')))


print('---------------------------------')


a = 2
b = 5

c = 3.0 + b, 5 * a
print(c)


print('---------------------------------')


x = ['a', 'b', 'c', 'd', 'e']
print(x[:-3])


print('---------------------------------')


print((1, 3, 5,) < (1, 2, 3, 4))


print('---------------------------------')


import json


x = {'name': 'yamada', 'data': [2,3,4]}
dict = json.dumps(x)

print(type(x))
print(type(dict))


print('---------------------------------')


d = 'dive\ninto\ncode\t'

print(d)
print(len(d))


print('---------------------------------')


name1, name2, name3, name4 = '', 'suzuki', 'tanaka', 'sato'
selsect_name = name1 or name2 or name3 or name4
# 一番先の文字列があるやつが表示されている
print(selsect_name)


print('---------------------------------')
import math


print('円周率は%5.3fである。'%math.pi)


print('---------------------------------')


