# 関数もオブジェクトの一つに過ぎないため変数として扱うこともできます。また、関数を他の関数の引数として渡したり、返り値として扱うこともできます
# 関数を引数２したり、返り値にする関数を高階関数という

# def print_hello():
#   print('hello')

# def print_goodbye():
#   print('goodbye')

# var = ['AA', 'BB', print_hello, print_goodbye]
# var[2]()
# var[3]()

# def print_world(msg):
#   print('{} world'.format(msg))

# def print_konnichiwa():
#   print('こんにちは')

# def print_hello(func):
#   func('hello')
#   return print_konnichiwa

# var = print_hello(print_world)
# var()
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー



# 1行で終わるような関数をよういる場合には、lambda式という無名関数を用いる事があります。
# lambda 引数：返り値
# lambda_a = lambda x,y,z=5:x*y*z
# # ↓
# # def func(x):
# #   return x*x
# res = lambda_a(3,4)
# print(res)

# y = 10
# x = 0 if (y-20) > 0 else 1
# # print(x)

# lambda_a = lambda x: x * x

# print(lambda_a(10))
# lambda_b = lambda x, y, z=5: x * y * z
# print(lambda_b(2,3))
# print(lambda_b(2,3,4))

# # 条件式つきlambda
# lambda_c = lambda x, y: y if x < y else x
# print(lambda_c(10, 100))
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


# 再帰とは関数から関数を呼び出すこと
# どうしても再起出ないといけない場合しか使わない フィボナッチ数列

# def sample(a):
#   if a < 0:
#     return
#   else:
#     print(a)
#     sample(a-1)

# sample(10)



# def fib(n):
#   return 1 if n < 3 else fib(n-1) + fib(n-2)

# for x in range(1, 10):
#   print(fib(x))
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


# ループと条件式を使って、一行でリストを作成する方法(リストない表記)
# 変数名 = [式 for 変数 in リスト (if 条件式)]

# list_a = (1,2,3,'a',4,'b')

# list_b = [x*2 for x in list_a if type(x) == int] # list_aのリスト
# print(list_b)
# list_c = [x for x in range(100) if x % 7 == 0]
# print(list_c)

# dict_a = {
#   'a': 'Apple',
#   'b': 'Banana'
# }
# list_c = [dict_a.get(x) for x in list_a if type(x) == str]
# print(list_c)

# list_a = tuple(x for x in range(100))
# print(type(list_a))

# def func(n):
#   for x in range(2, n):
#     if n % x == 0:
#       return True
#     return False

# list_a = [x for x in range(100) if func(x) == False]
# print(list_a)
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


# @関数名とつける事で、デコレーター関数を利用できる
# デコレーター関数は、関数オブジェクトを引数にとって、引数にとった関数に実行を加えます
# デコレーターは関数間で、ある処理を共通に利用したい場合によく使う

# def my_decorator(func):
#   def wrapper(*args, **kwargs):
#     print('*' * 100)
#     func(*args, **kwargs)
#     print('*' * 100)
#   return wrapper


# @my_decorator
# def func_a(*args, **kwargs):
#   print('func_aを実行')
#   print(args)

# @my_decorator
# def func_b(*args, **kwargs):
#   print('func_bを実行')
#   print(args)

# func_a(1,2,3)
# func_b(1,2,3)
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


# map関数：リスト、辞書のループ可能なクラスの変数を第２引数で入力として受け取り、実行時に第１引数の関数に代入した値を出力する
# list_a = [1,2,3,4,5]
# map_a = map(lambda x: x * 2, list_a)

# for x in map_a:
#   print(x)


# man = {
#   'name': 'sakatai',
#   'age': '25',
#   'country': 'japan'
# }

# map_man = map(lambda x: x + ',' + man.get(x), man)
# for x in map_man:
#   print(x)

# def calcurate(x,y,z):
#   if z == 'plus':
#     return x + y
#   elif z == 'minus':
#     return x - y

# map_sample = map(calcurate, range(5), [3,3,3,3,3], ['plus', 'minus', 'plus', 'minus', 'plus'])
# for x in map_sample:
#   print(x)