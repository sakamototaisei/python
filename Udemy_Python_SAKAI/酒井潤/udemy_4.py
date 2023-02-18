# セクション6 モジュールとパッケージ


print('--------------------')


# ---------------------------------------------------------------
# import文とAS

# import フォルダ名.ファイル名
# import Udemy_lesson.utils

# from フォルダ名 import ファイル名
# from Udemy_lesson import utils as u

# ASでパッケージ名を短く記述することができるが読みづらくなる場合があるためあまり好まれない場合がある

# fromの上記の場合Udemy_lessonという記述は不要となる
# r = u.say_twice('hello')
# r = Udemy_lesson.utils.say_twice('hello')
# print(r)


print('--------------------')


# ---------------------------------------------------------------
# 絶対パスと相対パスのimport

# from Udemy_lesson.talk import human

# print(human.sing())
# print(human.cry())


print('--------------------')


# ---------------------------------------------------------------
# アスタリスクのインポートと__init__.pyと__all_.pyの意味

# from Udemy_lesson.talk import animal

# *のインポートも可能だがおすすめではない
# from Udemy_lesson.talk import *

# print(animal.sing())
# print(animal.cry())


print('--------------------')


# ---------------------------------------------------------------
# importErrorの使い方


try:
    from Udemy_lesson import utils
except ImportError:
    from Udemy_lesson.tools import utils

print(utils.say_twice('word'))


print('--------------------')


# ---------------------------------------------------------------
# setup.pyでパッケージ化して配布する

# ターミナルで python setup.py sdist　で配布するためのパッケージを作成できる


print('--------------------')


# ---------------------------------------------------------------
# 組み込み関数


# print(globals())

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

for key in ranking:
    print(key)

# getで値を基準にソートをしrevers=Trueで並びを大きい順にかえる
print(sorted(ranking, key=ranking.get, reverse=True))


print('--------------------')


# ---------------------------------------------------------------
# 標準ライブラリ


s = "goaihgnvjbnnbodsfhnbsnboishhbldsnfobajhlbvnbpuoqytqb"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1

print(d)

print('--------------------')
# 上記の別解
s2 = "osdhguoadhbfg@oahj"
d2 = {}
for c in s2:
    d2.setdefault(c, 0)
    d2[c] += 1

print(d2)

print('--------------------')
from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)


print('--------------------')


# ---------------------------------------------------------------
# サードパーティのライブラリ


# from termcolor import colored

# print('test')
# print(colored('test', 'green'))


print('--------------------')


# ---------------------------------------------------------------
# importする際の記述の仕方

# インポートは "," で区切って記述可能だが一行ずつ書くのか良い.
# アルファベット順に書く
# ①最初に標準ライブラリから記述していく
# ②サードパーティのライブラリと標準ライブラリとの間一行のスペースを設ける
# ③自分たちの会社チームのパッケージのスペースを設ける
# ④ローカルで作成したパッケージ

import collections
import sys

import termcolor

import Udemy_lesson

print(collections.__file__)
print(termcolor.__file__)
print(Udemy_lesson.__file__)

print(sys.path)


print('--------------------')


# ---------------------------------------------------------------
# __name__と__main__

import Udemy_lesson.talk.animal

import config


def main():
    Udemy_lesson.talk.animal.sing()

if __name__ == '__main__':
    main()

print('lesson', __name__)