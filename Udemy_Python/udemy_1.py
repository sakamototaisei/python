# セクション3 Pythonの基本

num = 1
name = '1'

new_num = int(name)

print(new_num, type(new_num))

# print('Hi', 'Mike', sep=',', end='.')

pi = 3.141592653579893238
print(pi)
print(round(pi, 2))         # round() 引数に値としも何桁で丸めるのか指定できる


# -----------------------------------------------------------------------
# 数学関数
import math

result = math.sqrt(25)      # sqrt 平方根
print(result)

y = math.log2(10)           # log2
print(y)

# print(help(math))           # help() 関数のドキュメントを表示


# -----------------------------------------------------------------------


print('I don\'t know')
print('say "I don\'t know"')
print('hello.\nHow are you?')
print(r'C: \name\name')       # row　データのrを入れると改行されない

# \をうまく使って次書くコードは次の行からですよと伝えてあげる
print('#'*30)
print("""\
line1
line2
line3\
""")
print('#'*30)


print('Hi.' * 3 + 'Mike.')
print('Py''thon')


s = ('aaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbb')

print(s)


# -----------------------------------------------------------------------
# 文字列のインデックスとスライス


word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print('------------------')
print(word[0:2])
print(word[:2])
print('------------------')
print(word[2:])
print('------------------')
word = 'j' + word[1:]  # 足し合わせて上書きしてあげる
print(word[:])
n = len(word)
print(n)


# -----------------------------------------------------------------------
# 文字のメソッド


s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')     # startswith()引数の文字から始まっているか？判定
is_start2 = s.startswith('x')
print(is_start)
print(is_start2)

print('------------------')

print(s.find('Mike'))             # find() 引数の文字がどこにあるか整数で返す
print(s.rfind('Mike'))            # rfind() findの後ろから探索する版
print(s.count('Mike'))            # count() 引数の文字列が何個含まれているか整数で返す
print(s.capitalize())             # capitalize() 初めの文字だけ大文字にして他は小文字に変換される
print(s.title())                  # title() 全ての文字群の先頭を大文字に変換する
print(s.upper())                  # upper() 全てを大文字に変換
print(s.lower())                  # lower()　全てを小文字に変換する
print(s.replace('Mike', 'Sakatai'))

print('------------------')


# -----------------------------------------------------------------------
# 文字列の代入 format() 整数も文字列変換される


print('a is {} {} {}'.format(1, 2, 3))
print('a is {0} {1} {2}'.format(1, 2, 3))
print('a is {2} {1} {0}'.format(1, 2, 3))

print('My name is {0} {1}. Watashi ha {1} {0}'.format('Taisei', 'Sakamoto'))
print('My name is {name} {family}. Watashi ha {family} {name}'.format(name='Taisei', family='Sakamoto'))

print('------------------')


# -----------------------------------------------------------------------
# f-strings 新しいスタイルで処理も早い

a = 'a'

print(f'a is {a}')


x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Sakatai'
family = 'Sakamoto'
print(f'My name is {name} {family}. Watasgi ha {family} {name}')