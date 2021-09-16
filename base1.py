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
# --------------------------------------------------------------------

# リスト
# list_a = [1,2,3,4]
# list_b = []

# print(list_a)
# print(list_a[-1])

# list_a = [1, [1,2,'apple'],3,'banana']
# print(list_a[1][2])
# print(list_a)
# list_a[1][2] = 'lemon'
# print(list_a)

# リストのメソッド
# list_a = [1,2,3,4,5]

# list_b = list_a[1:4]
# print(list_b)

# # append(要素の追加), extend(リストの拡張), insert(特定の場所に要素を追加), clear(リストのクリア)
# list_a.append('apple')
# print(list_a)
# list_a.extend(['banana', 'melon'])
# print(list_a)
# list_a.insert(1, 'grape')
# print(list_a)
# list_a.clear()
# print(list_a)

# remove(要素の削除), pop(要素の取り出し), count(要素のカウント), index(要素の検索)
# list_a = [0,1,1,2,2,3,3,3,4]
# list_a.remove(3)
# print(list_a)

# value = list_a.pop()
# print(list_a, value)

# print(list_a.count(1))

# print(list_a.index(2))

# # copy(リストの中身のコピーを返す)
# print(list_a)
# list_b = list_a.copy()
# list_b[0] = 'AAAAA'
# print(list_a)

# # sort(要素の昇順並び替え), reverse(要素の逆順並び替え)
# list_a = ['banana', 'apple', 'lemon', 'grape']

# print(list_a)
# # list_a.sort()
# list_a = sorted(list_a)
# list_a.reverse()
# print(list_a)
# -----------------------------------------------------------------------

# Dictionary(辞書型)

# car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015, 1: 100}

# print(car['brand'])
# print(car.get('bran', 12))
# print(car.get(1))

# print(car.keys()) # キー一覧
# print(car.values()) # 値一覧
# print(car.items()) # キー　＋　値

# for k, v in car.items():
#   print('key = {}, value = {}'.format(k, v))

# if 'brand' in car:
#   print('carのブランドは{}'.format(car['brand']))

# 辞書型のメソッド

# car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}

# tmp_car = {'country': 'Japan', 'prefecture': 'Aichi', 'model': 'カローラ'}

# car.update(tmp_car)  # 追加、更新
# print(car)

# car['city'] = 'Toyota-shi'
# car['year'] = 2017
# print(car)

# value = car.popitem()  # 一番最後のアイテムを取り出す
# print(car)
# print(value)

# value = car.pop('model')  # 値を取り出す
# print(car)
# print(value)

# car.clear()  # 中身を削除
# print(car)

# del car  # del 変数そのもの削除
# print(car)
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

# タプルは、リストと似ていて値を複数入れる。変更追加できない,ハッシュ化して辞書型のキーとして利用する

# fruit = ('apple', 'banana', 'lemon')

# print(fruit)
# print(type(fruit))
# print(fruit[0])
# # fruit[1] = 'grape' エラー
# fruit = fruit + ('grape',)
# print(fruit)

# list_fruit = ['apple', 'banana']
# fruit = tuple(list_fruit)  # タプル変換
# print(fruit)
# print(fruit.count('apple'))  # 要素の個数
# print(fruit.index('apple'))  # 要素の場所、インデックス番号で,ない時はエラー

# pos = (135, 35)

# countries = {pos: 'Japan'}
# print(countries.get((135, 35)))
# ----------------------------------------------------------------------

# セット

# set_a = {'a', 'b', 'c', 'd', 'a', 12}
# print(set_a)
# print('e' in set_a) # 指定要素あるか？true false
# print('a' in set_a)
# print('a' not in set_a) # 指定要素がないか？ true false

# print(len(set_a)) # 要素の個数

# # add, remove, discard, pop, clear

# set_a.add('A') # 追加
# print(set_a)

# set_a.remove('a') # 削除 存在しない要素を指定するとエラーになる
# print(set_a)

# set_a.discard(13) # 存在しない要素を指定してもエラーにならない
# print(set_a)

# val = set_a.pop() # 取り出し
# print(val, set_a)

# set_a.clear()
# print(set_a) # 中身を空に

# s = {'a', 'b', 'c', 'd'}
# t = {'c', 'd', 'e', 'f'}

# u = s | t  # 和集合
# # u = s.union(t)
# print(u)

# u = s & t  # 積集合
# # s.intersection(t)
# print(u)

# u = s - t  # 差集合 sに含まれていてtに含まれていない
# # s.difference(t)
# print(u)

# u = s ^ t  # 対象差 両方に被っていない
# # s.symmetric_difference(t)
# print(u)

# s |= t  # 要素を追加する
# print(s)

# # issubset, issuperset, isdisjoint
# s = {'apple', 'banana'}
# t = {'apple', 'banana', 'lemon'}
# u = {'cherry'}

# print(s.issubset(t))  # sはt「に」全部含まれてるか? true false
# print(s.issuperset(t))  # sはt「を」全部含んでいるか? true false

# print(t.isdisjoint(s)) # 重なっている要素がひとつもない場合true
# print(t.isdisjoint(u))

