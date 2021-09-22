# 関数

# def print_hello():
#     print('Hello World')


# print_hello()


# def num_max(a: int, b: int):
#   print('a = {}, b = {}'.format(a, b))
#   if a > b:
#     return a
#   else:
#     return b

# print(num_max(b=100,a=20))
# print(num_max(10, 20))


# 可変長引数：場合に応じてその都度、引数が変わるもの
# *arg1のように*を１つつけると、可変長のタプル arg2 = (1,2,3)
# **arg2のように*を２つつけると、可変長の辞書 arg3 = {'arg4': 5, 'arg5': 6}

# デフォルト値、可変長引数、複数の戻り値
# 可変長引数は１つまでしか宣言できないが、タプル型と辞書型はできる

# def sample(arg1, arg2=100):
#   print(arg1, arg2)

# # sample(200)

# def spam(arg1, *arg2):
#   print('arg1 = {}, arg2 = {}'.format(arg1, arg2))
#   print(type(arg2))

# spam(1,2,3,4,5)


# def spam_2(arg1, **arg2):
#   print('arg1 = {}, arg2 = {}'.format(arg1, arg2))
#   print(type(arg2))

# spam_2(1, name='Sakatai', age=25)


# def spam_3(arg1, *arg2, **arg3):
#   print(arg1, arg2, arg3)

# spam_3(1,2,3,4,5,name='Sakatai', age=25)


# def sample_2():
#   return 1, 2

# a, b = sample_2()
# print(a, b)
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


# グローなる変数

# def printAnimal():
#     global animal
#     animal = 'Cat'
#     print('関数内animal = {}, id = {}'.format(animal, id(animal)))


# # animal = 'Dog'
# printAnimal()
# print('関数内animal = {}, id = {}'.format(animal, id(animal)))
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


# 関数の内部に関数を書くことをinner関数という
# inner関数の用途::外の関数の外からアクセスできないような関数よ作成する、
# 関数の中で同じ処理が何度も発生する場合１つにまとめる、デコレーター関数を作成

# nonlocalと宣言することによって、外側の関数の変数を変更する事ができる

# inner関数、ノンローカル変数

# def outer():
#   outer_value = '外側の変数'
#   def inner():
#     nonlocal outer_value
#     outer_value = '内側の変数'
#     print('inner: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
#   inner()
#   print('outer: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

# outer()
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


# ジェネレーター関数
# def generator(max):
#     print('ジェネレーター作成')
#     for n in range(max):
#         try:
#             x = yield n
#             print('x = {}'.format(x))
#             print('yield実行')
#         except ValueError as e:
#             print('throwを実行しました')


# gen = generator(10)
# n = next(gen)
# print('n = {}'.format(n))
# n = next(gen)
# print('n = {}'.format(n))

# for x in gen:
#   print('x = {}'.format(x))

# ジェネレーター関数のメソッド
# send():yieldで停止している箇所に値を送る
# throw():指定した例外が発生して処理が終了される
# close():ジェネレーターを正常終了させる

# next(gen)
# gen.send(100)
# gen.throw(ValueError('Invalid Value'))
# gen.close()
# next(gen)
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


# yield fromと記述して、ジェネレーターからサブジェネレーターを呼びタス事ができる


# def sub_sub_generator():
#   yield 'sub subのyield' # 3
#   return 'sub subのretrun'

# def sub_generator():
#   yield 'subのyield' # 2
#   res = yield from sub_sub_generator() # 今回はsub sub のreturnの値が返ってくる
#   print('sub res = {}'.format(res)) # 4
#   return 'subのretrun'

# def generator():
#   yield 'generatorのyield' # 1
#   res = yield from sub_generator()
#   print('gen res = {}'.format(res)) # 5
#   return 'generatorのreturn'


# gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


# ジェネレーターの使い道は？？？
# メモリ使用量を大幅削減することに使う
#  DBから大量のデータを引っ張る時に有効、
#  generatorを使うとメモリをほぼ０にする事ができる(ただしgeneratorの方が処理は遅い)

# list, generator memory

# import sys
# list_a = [i for i in range(100000)]
# def num(max):
#   i = 0
#   while i < max:
#     yield i
#     i += 1

# # for i in num(100000):
# #   print(i)
# gen = num(100000)
# print(sys.getsizeof(list_a)) # インスタンスのメモリのサイズを確認できる
# print(sys.getsizeof(gen))