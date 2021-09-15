# 標準入出力、コメント文、変数

# print('Hello World')

"""
あああいいいい
"""

# name = input('あなたの名前はなんですか？：　')
# print(name)
# age = 25
# # format関数
# print('私の名前は = {}, 年齢は{}'.format(name, age))

# a = b = 'hello'
# print(a, b)
# -------------------------------------------------------

# # 変数の応用
# animal = 'dog'
# 動物 = 'cat'
# print(動物)

# # 定数
# LEGAL_AGE = 20
# age = 25
# if age < LEGAL_AGE:
#     print('未成年')
# else:
#     print('成人')

# # format文
# print(f'age = {age}')
# print(f'{age=}')
# ---------------------------------------------------------

# # 論理型
# is_animal = True
# if is_animal:
#   print('動物です！')

# is_man = True
# is_adult = True

# # or文
# if is_man or is_adult:
#   print('男が大人です')
# # and
# if is_man and is_adult:
#   print('男は成人です')
# --------------------------------------------------------

# 数値型
# value = 1
# print(value)
# value = -2
# print(value)
# value = value + 4
# print(value * 4)
# print(value / 3)
# value = 10
# print(value // 3)
# print(value % 3)
# value = 1
# value += 3
# print(value)
# print(value ** 3)
# 浮動小数点数
# height = 175.5

# print(height)
# print(type(height))
# value = 8
# print(value >> 2)
# print(value << 3)

# print(12 & 21) # 01100 and 10101 = 00100 => 4
# print(12 | 21) # 01100 or 10101 = 11101 => 29
# -----------------------------------------------------

# 2進数、８進数、１６進数
# age = 0b111
# print(age)
# age = 0o11
# print(age)
# age = 0x11
# print(age)

# # ２進数＝＞文字列
# print(bin(15))
# print(oct(15))
# print(hex(15))
# --------------------------------------------------

# 複素数
# a = 1 + 3j
# b = 3 + 5j
# print(a, b)
# print(a + b)
# print(a - b)
# print(a * b)

# complex
# a = complex(1, 3)
# b = complex(3, 5)
# print(a, b)
# print(a + b)
# print(a - b)
# print(a * b)

# print(a.real)
# print(a.imag)
# -----------------------------------------------

# 文字列型
# fruit = 'apple'
# print(fruit)
# print(type(fruit))
# print(fruit * 10)
# fruit_10 = fruit * 10
# print(fruit_10)

# new_fruit = fruit + ' banana'
# print(new_fruit)

# fruits = """apple
# banana
# grape
# """
# print(fruits)

# fruit = 'banana'
# print(fruit[-2])

# # encode, decode => bytes
# byte_fruit = fruit.encode('utf-8')
# print(byte_fruit)
# print(type(byte_fruit))

# str_fruit = byte_fruit.decode('utf-8')
# print(str_fruit)
# print(type(str_fruit))

# count
# msg = 'ABCDEABC'
# print(msg.count('ABC'))

# # starswith, ebdswith
# print(msg.startswith('ABCD'))
# print(msg.endswith('C'))

# # strip(両端), rstrip(右端), lstrip(左端)
# msg = ' ABC '
# print(msg)
# print(msg.strip())
# msg = 'ABCDEFABC'
# print(msg.strip('CBA'))
# print(msg.rstrip('CBA'))
# print(msg.lstrip('CBA'))

# # upper, lower, swapcase, replace, capitalize

# msg = 'abcABC'
# msg_u = msg.upper() # 大文字に
# msg_l = msg.lower() # 小文字に
# msg_s = msg.swapcase() # 大文字小文字入れ替え
# print(msg_u, msg_l, msg_s)

# msg = 'ABCDEABC'
# msg_r = msg.replace('ABC', 'FFF', 1)
# print(msg_r)

# msg = 'hello world'
# print(msg.capitalize())
# -----------------------------------------------------

# 文字列の一部取り出し、format, isloewr, isupper

# msg = 'hello, my name is sakatai'
# print(msg[1:10:2])
# print('hello {}'.format('sakatai'))
# name = 'sakatai'
# print(f'hello {name}')
# print(f'{name=}')

# msg = 'apple'
# print(msg.islower()) # 小文字か？ true false
# print(msg.isupper()) # 大文字か？ true false

# # find, index, rfind, rindex 検索
# msg = 'ABCDEABC'
# print(msg.find('ABC')) # 場所を数値で返す 見つからない場合−１
# print(msg.rfind('ABC')) # 右から探す
# print(msg.index('ABC'))# 見つからない場合エラーが起こり処理がストップ
# print(msg.rindex('ABC'))
# --------------------------------------------------------------

# int str 変換
# int_num = 12
# str_num = str(int_num)
# print(str_num)
# print(type(str_num))
# print('num = ' + str(int_num))
# float_num = 20.5
# str_float = str(float_num)
# print(str_float)
# print(type(str_float))

# # str => int, float
# msg = '12'
# int_msg = int(msg)
# float_msg = float(msg)

# print('value = {}, type = {}'.format(int_msg, type(int_msg)))
# print('value = {}, type = {}'.format(float_msg, type(float_msg)))