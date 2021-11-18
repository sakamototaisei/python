"""
独学プログラマー

第一部
プログラミングを断固継続
"""

print("""こんにちは、sakataiです。
今日はPythonの学習をやっていきます。
将来はアイアンマンのジャービスを作ります。""")


print('-----------------------')


print\
("""こんにちは、sakataiです。今日はPythonの学習をやっていきます。
将来はアイアンマンのジャービスを作ります。""")


print('-----------------------')


try:
    x = 10 / 0
except ZeroDivisionError as e:
    print('0で割ってはいけません')
    print(e)


print('-----------------------')

def f(x):
    return x * 2

r = f(2)
print(r)


print('-----------------------')

# 関数はreturnを記述しなくてもいいが、returnがない場合はNoneを返す
def func():
    r = 1 + 1

r = func()
print(r)


print('-----------------------')


# age = input('Enter your age : ')
# int_age = int(age)
# if int_age < 20:
#     print('You are young!')
# else:
#     print('Wow, you are old!')


print('-----------------------')


def even_odd(x):
    if x % 2 == 0:
        print('偶数です')
    else:
        print('奇数です')

even_odd(25)
even_odd(20)


print('-----------------------')


"""
ドキュメンテーション
関数および引数を定義するとき、引数が特定のデータ型でないと関数が正しく動作しないことがある
関数を呼び出す人に、関数を呼び出す人にm引数のデータ型を伝える
"""

def add(x, y):
    """
    Returns x + y.
    :param x: int.
    :param y: int.
    :return int sum of x and y.
    """
    return x + y

result = add(10, 25)
print(result)


print('-----------------------')


def sample_func1():

    num = input('数字を入力してください : ')
    int_num = int(num)

    return int_num ** 2

# result = sample_func1()
# print(result)


print('-----------------------')


def float_func():
    try:
        num = input('数値を入力してください : ')
        float_num = float(num)
        return float_num
    except ValueError as e:
        print('正しく数値を入力してください')
        print(e)

# result = float_func()
# print(result)


print('-----------------------')


"""
コンテナ : 書類棚のようなもの、データ構造を持つ。
ex)リスト、タプル、辞書

メソッド : 特定のデータ型に密接にかんれん付けられている関数。

イテラブル : 繰り返し処理で要素を１つずつ取り出せるオブジェクト(繰り返し可能)

ミュータブル : 変更可能

イミュータブル : 変更不可
"""

print('hello'.upper())
print('hello'.replace('o', '@'))


fruits = ['apple', 'banana', 'melon']
print('banana' in fruits)
print('peach' in fruits)
print(len(fruits))

print('-----------------------')


colors = ['purple', 'orange', 'green']

# while True:
#     guess = input('私の色は何色でしょう?(入力してください) : ')
#     if guess in colors:
#         print('大当たりー！！！')
#         break
#     else:
#         print('ハズレ！再チャレンジ!')
#         print('ヒントは...柑橘系？自然？毒？')


print('-----------------------')


singer = {
    '1': '宇多田ヒカル',
    '2': 'ジャスティン・ビーバー',
    '3': 'コレコレ',
    '4': 'マシュメロ',
    '5': 'アラン・ウォーカー'
}

# n = input('数字を入力してください : ')
# if n in singer:
#     song = singer[n]
#     print(song)
# else:
#     print('見つかりませんでした。')

print('-----------------------')


"""
文字列操作

"""

name = 'my name is sakatai'
print(name.capitalize())


I_AM = ['my', 'name', 'is', 'sakatai']
introduction = ' '.join(I_AM)
print(introduction)

s = '       sakatai       '
print(s)
# 空白除去
s = s.strip()
print(s)

s = 'My name is sakatai'
# 文字列の置換
s = s.replace('a', '@')
print(s)


print('-----------------------')
# 文字を探す
try:
    print(s.index('z'))
except ValueError as e:
    print(e)
    print('Not fount.')