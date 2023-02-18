# 制御フローとコード構造


# コメントは上に書く暗黙のルールがある
print('xxxxxx')
"""
test
test
test
"""
print('xxxxxx')

print('--------------------')


# ---------------------------------------------------------------
# 1行が長くなるとき

# 80文字が1行にかける長さである
# ------------------------------------------------------------------------------ここまでで80文字この長さまで

s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     + 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')

x = (1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
     + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1)

print(s)
print(x)

print('--------------------')


# ---------------------------------------------------------------
# if文  Pythonはインデント４暗黙のルール

x = 0

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')


a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

print('--------------------')


# ---------------------------------------------------------------
# デバッガーを使って確認してみる


print('--------------------')


# ---------------------------------------------------------------
# 論理演算子と比較演算子

a = 1
b = 1

# aとbが等しい
if a == b:
    print('equal')

# aがbと異なる
print(a != b)

# a > b
# a >= b
# a < b
# a <= b
# a > 0 and b > 0
# a > 0 or b > 0

print('--------------------')


# ---------------------------------------------------------------
# InとNotの使い方

y = [1, 2, 3]
x = 100

# xはyの中に入っている場合
if x in y:
    print('in')

# xがyの中に入っていない場合
if x not in y:
    print('not in')


a = 1
b = 2

# この使い方は好ましくない
if not a == b:
    print('Not equal')

# こっちの方がいい
if a != b:
    print('Not equal')


is_ok = False

# bool型の時にnotを使う時が多い
if not is_ok:
    print('hello')

print('--------------------')


# ---------------------------------------------------------------
# 値が入ってない判定をするテクニック

# is_ok = True

# 0はFalse それ以上の整数だとTrue
# is_ok = 0

# 文字列が入るとTrueになる、空だとFalse、空白はTrue
# is_ok = ' '

# リストが空だとFalse,あればTrue
is_ok = [1, 2, 3]

# まとめ False, 0, 0.0, '', [], (), {}, set() はFalseでそれ以外はTrueとなる

if is_ok:
    print('OK!')
else:
    print('No!')


print('--------------------')


# ---------------------------------------------------------------
# Noneを判定する場合 is


is_empty = None
# print(help(is_empty))

# isを使ってオブジェクト判定できる(True と　True, None　と　None)
if is_empty is None:
    print('None!!!')


print('--------------------')


# ---------------------------------------------------------------
# while文とcontinue文とbreak文

count = 0

while count < 5:
    print(count)
    count += 1

print('--------------------')

count = 0
while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue
    print(count)
    count += 1

print('--------------------')


# ---------------------------------------------------------------
# while else文

count = 0

while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    # while文のelseはループbreakで抜けなければ処理をする
    print('done')

print('--------------------')


# ---------------------------------------------------------------
# input関数

# while True:
#     word = input('Enter:')
#     num = int(word)
#     if word == 'ok':
#         break
#     elif num == 100:
#         break
#     print('next')

print('--------------------')


# ---------------------------------------------------------------
# for文とbreak文とcontinue文

some_list = [1, 2, 3, 4, 5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

for i in some_list:
    print(i)

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        continue
    print(word)

print('--------------------')


# ---------------------------------------------------------------
# for else文

for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
# for elseはbreakで抜けなければ最後に処理される
else:
    print('I ate all')


print('--------------------')


# ---------------------------------------------------------------
# range関数 range(始, 終, 飛)

# for i in range(2, 10, 3):
#     print(i)

# for文の変数を使わない倍は_で定義すると読みやすいコードになる
for _ in range(10):
    print('hello')


print('--------------------')


# ---------------------------------------------------------------
# enumerate関数 インデックス番号を持たせたい時につく

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)


print('--------------------')


# ---------------------------------------------------------------
# zip関数

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)


print('--------------------')


# ---------------------------------------------------------------
# 辞書型をfor文で処理をする

d = {'x': 100, 'y': 200}

# items() 辞書型をリストの中にタプルとして返している
for k, v in d.items():
    print(k, ':', v)


print('--------------------')


# ---------------------------------------------------------------
# 関数定義

def say_something():
    s = 'hi'
    return s

result = say_something()
print(result)

# タイプfunction
print(type(say_something))

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('red')
print(result)


print('--------------------')


# ---------------------------------------------------------------
# 関数の引数と返り値の宣言

# 引数の型を明示しておくこともできる
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num(10, 20)
print(r)

# 関数でint型と明示していてもエラーを返してくれない
r = add_num('a', 'b')
print(r)


print('--------------------')


# ---------------------------------------------------------------
# 位置引数とキーワード引数とデフォルト引数


def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

# menu('beef', 'beer', 'ice')
menu(entree='beef', dessert='ice', drink='beer')

print('--------------------')


# デフォルト引数
def menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu('chiken', drink='beer')


print('--------------------')


# ---------------------------------------------------------------
# デフォルト引数で気をつけること


# def test_func(x, l=[]):
#     l.append(x)
#     return l

# 解決策空のリストではなくNoneを定義する リストを初期化することができる
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


y = [1, 2, 3]
r = test_func(100, y)
print(r)

y = [1, 2, 3]
r = test_func(200, y)
print(r)

r = test_func(100)
print(r)

# ２回目以降には[100, 100]となる バグに繋がるのでPythonでは空のリストをデフォルト引数には指定しないのが暗黙のルール
r = test_func(100)
print(r)

r = test_func(100)
print(r)


print('--------------------')


# ---------------------------------------------------------------
# 位置引数のタプル化


# 複数の引数の値をタプル化してくれる *args
def say_something(word, *args):
    print('word = ', word)
    for arg in args:
        print(arg)


t = ('Mike', 'Nance')
# *変数,でタプルですよとの意味
say_something('Hi', *t)


print('--------------------')


# ---------------------------------------------------------------
# キーワード変数の辞書化


# 引数**kwargs(キーワードアーギュメンツの略)
def menu(**kwargs):
    # 辞書型で出力する
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
# **変数で辞書型が展開されて関数へ渡してあげる
menu(**d)

print('--------------------')

# *が1つ目から指定する => (**kwargs, *args) これだとエラーになる
def menu(food, *args, **kwargs):
    # 位置引数
    print(food)
    # 残りの引数タプル化
    print('args = ', args)
    # キーワード引数を辞書化
    print('kwargs = ', kwargs)

menu('banana', 'apple', 'orange', entree='beef', drink='coffee')


print('--------------------')


# ---------------------------------------------------------------
# Docstringsとは


# 関数のドキュメントの書き方参考
def example_func(param1, param2):
    """Example function with types documented in the docstrings.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Reterun:
        bool: The return value. True for success, False otherwise.
    """
    print(param1)
    print(param2)
    return True

# __doc__で自分が関数内で書いたドキュメントが出力される help()でも同じ
print(example_func.__doc__)


print('--------------------')


# ---------------------------------------------------------------
# 関数内関数

def outer(a, b):
    # この関数内の中でしか使わない関数など
    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

outer(1, 2)


print('--------------------')


# ---------------------------------------------------------------
# クロージャー すぐに実行したくない時ゆくゆく使う時

def outer(a, b):

    def inner():
        return a + b

    return inner

# inner functionを返している
f = outer(1, 2)
# f()の時点でinnerが実行される
r = f()
print(r)

print('--------------------')


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    # インナーファンクションを実行せずにreturnさせる
    return circle_area


# 関数を入れて後々使えるようにする
ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592653579893238)

# ここでインナー関数が実行される
print(ca1(10))
print(ca2(10))


print('--------------------')


# ---------------------------------------------------------------
# デコレーター

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


# @デコレーター関数 何かを包み込んでいるイメージ デコレーターの順番によって処理が変わる
@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

# f = print_info(add_num)
# r = f(10, 20)
# print(r)

# print('start')
# r = add_num(10, 20)
# print('end')

# print(r)


print('--------------------')


# ---------------------------------------------------------------
# ラムダ式


l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()

# ラムダでかける ファンクションを引数にするときに有効
# sample_func = lambda word: word.capitalize()


change_words(l, lambda word: word.capitalize())
print('--------------------')
change_words(l, lambda word: word.lower())


print('--------------------')


# ---------------------------------------------------------------
# ジェネレーター反復処理


l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print('--------------------')

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

def counter(num=10):
    for _ in range(num):
        yield 'run'


# for g in greeting():
#     print(g)

# ジェネレーター生成
g = greeting()
c = counter()

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))


print('--------------------')


# ---------------------------------------------------------------
# リスト内包表記

t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

l = [i for i in t if i % 2 == 0]
print(l)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

# 上記をリスト内包表記で書くと
# forの中にforなどをリスト内包でかけるが読みにくいため望ましくない場合がある
# おすすめはfor文のifの場合などで使う
r = [i * j for i in t for j in t2]
print(r)


print('--------------------')


# ---------------------------------------------------------------
# 辞書内包表記

w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

# 上記を内包表記で書く
d = {k: v for k, v in zip(w, f)}
print(d)



print('--------------------')


# ---------------------------------------------------------------
# 集合内包表記


s = set()

for i in range(10):
    s.add(i)

print(s)

# 上記を内包表記で書く
s = {i for i in range(10) if i % 2 == 0}
print(s)



print('--------------------')


# ---------------------------------------------------------------
# ジャネレーター内包表記


def g():
    for i in range(10):
        yield i

g = g()
print(next(g))
print(next(g))
print(next(g))

# 上記を内包表記で書く
g = (i for i in range(10) if i % 2 == 0)
# タプルかと思いきやジェネレーターになっている
print(type(g))
print(next(g))
print(next(g))
print(next(g))

# タプル内包表記にはtuple()と宣言する
g = tuple(i for i in range(10) if i % 2 == 0)
print(type(g))
print(g)


print('--------------------')


# ---------------------------------------------------------------
# 名前空間とスコープ


"""
Test Test #########################
"""

# グローバル変数
animal = 'cat'

def f():
    """Test func doc"""
    # グローバル変数を宣言している
    # global animal
    # ローカル変数
    animal = 'dog'
    print('local', locals())
    print('--------------------')

    print(f.__name__)
    print(f.__doc__)

f()
print('global:', __name__)
# print('global:', globals())


print('--------------------')


# ---------------------------------------------------------------
# 例外処理


l = [1, 2, 3]
i = 5
# del l

try:
    l[0]
# エラーをキャッチして処理が行われる
except IndexError as ex:
    print("Don't worry : {}".format(ex))
except NameError as ex:
    print(ex)
# IndexでもNameでもないエラーをキャッチして処理が行われる 細かくキャッチする記述をした方がよい
except Exception as ex:
    print('other : {}'.format(ex))
# exceptがエラーなく抜けた場合実行される
else:
    print('done')
# エラーあってもなくても必ず実行される処理
finally:
    print('clean up')

print('last')



print('--------------------')


# ---------------------------------------------------------------
# 独自の例外の作成


# raise IndexError('test error')

class UppercaseError(Exception):
    pass

def check():
    words = ['apple', 'banana', 'orange']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')
else:
    print('独自のエラー検出されず')
finally:
    print('clean up')


print('--------------------')


# ---------------------------------------------------------------