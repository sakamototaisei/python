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