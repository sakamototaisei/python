""""ループ文"""

for i in range(10):
    print(i)


for _ in range(10):
    pass

print('-------------')


for i in range(2, 20, 3):
    print(i)



sample = ['John', 'Paul', 'George', 'Ringo']
for member in sample:
    print(member)

print('-------------')


human = {
    'name': 'sakatai',
    'age': 25,
    'gender': 'man'
}

for h in human:
    print(h, human.get(h))


print('-------------')


# enumerate, zip, while

fruits = ['apple', 'grape', 'pine']

for index, value in enumerate(fruits):
    print('index = {}'.format(index))
    print('value = {}'.format(value))

print('-------------')

classA = ['Taro', 'sakatai', 'yui']
classB = ['tara', 'katuo', 'awabi']

for a, b in zip(classA, classB):
    print('classA student : {}'.format(a))
    print('classB student : {}'.format(b))


print('-------------')


count = 0

while count < 10:
    print('{}hello'.format(count))
    count += 1


print('-------------')


for i in range(10):
    if i == 3:
        continue
        # break
    print(i)
else:
    print('forループの処理終了')


print('-------------')

num = 0
while num < 10:
    if num == 5:
        num += 1
        continue
    # elif num == 7:
    #     break
    print(num)
    num += 1
else:
    print('whileループ終了')


print('-------------')


"""
セイウチ演算子　:=
変数の代入と変数の使用を同時に実行できる
"""

n = 0
while (n := n + 1) < 10:
    print('hello')


print('-------------')


if (n := 10) > 5:
    print('5より大きい : {}'.format(n))


n = 0
while (n := n + 1) < 10:
    print(n)


print('-------------')


"""FizzBuzz"""


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('{} FizzBuzz'.format(i))
    elif i % 3 == 0:
        print('{} Fizz'.format(i))
    elif i % 5 == 0:
        print('{} Buzz'.format(i))
    else:
        print(i)


print('-------------')


"""
例外処理
実行時に発生するエラーを制御して処理を行う

try:
    処理
except エラー名:
    例外発生時の処理
else:
    例外が発生しなかった場合に実行される
finally:
    例外が発生した場合にも、発生しなかった場合にも実行される

"""


try:
    b = [10, 20, 30]
    c = b.method_a()
    a = b[4]
    a = 10 / 0
except ZeroDivisionError as e:
    # 細かくエラーの内容を確認したいとき
    import traceback
    traceback.print_exc()
    # print(e, type(e))
except IndexError as e:
    print('IndexError発生')
except Exception as e:
    print('Exception', e, type(e))
else:
    # エラーがない場合に実行 else内のエラーはキャッチされない。処理を分割したいときに使う
    print('else処理')
finally:
    print('finally処理')


print('処理が完了しました')


print('-------------')


"""raise　例外を返す"""

# 自作の例外
class MyExceptiomn(Exception):
    pass


def devide(a, b):
    if b == 0:
        # 自作の例外
        raise MyExceptiomn('0では割り切れません')
    else:
        return a / b

try:
    c = devide(10, 0)
except Exception as e:
    print(e, type(e))


print('-------------')


"""選択ソート n**"""

list_a = [5, 7, 4, 5, 1, 2, 3, 2, 9, 1, 4]

for i in range(len(list_a)):

    min_idx = i
    for j in range(i+1, len(list_a)):
        if list_a[min_idx] > list_a[j]:
            min_idx = j
    list_a[i], list_a[min_idx] = list_a[min_idx], list_a[i]
print(list_a)



print('-------------')


"""バブルソート"""

list_a = [5, 7, 4, 5, 1, 2, 3, 2, 9, 1, 4]

for i in range(len(list_a)):
    for j in range(0, len(list_a) - i - 1):
        if list_a[j] > list_a[j+1]:
            list_a[j], list_a[j+1] = list_a[j+1], list_a[j]

print(list_a)


print('-------------')


for i in range(9):
    new_l = list(range(0, 9 - i -1))
    print(i, new_l)

print('-------------')

list_b = [10, 1, 1000, 100]
print(list_b)
for i in range(len(list_b)):
    print('i = {}'.format(i))
    for j in range(0, len(list_b) -i -1):
        print('j = {}'.format(j))
        print('list_b[j] = {}, list_b[j+1] = {}'.format(list_b[j], list_b[j+1]))
        if list_b[j] > list_b[j+1]:
            list_b[j], list_b[j+1] = list_b[j+1], list_b[j]
        else:
            print('入れ替えなし')
        print('list_b = {}'.format(list_b))
        print('-'*10)
print(list_b)


print('-------------')


list_c = [100, 1, 10, 1000]
print(list_c)
for i in range(len(list_c)):
    print('i = {}'.format(i))
    min_i = i
    for j in range(i+1, len(list_c)):
        print('j = {}'.format(j))
        print('list_c[min_i] = {}, list_c[j] = {}'.format(list_c[min_i], list_c[j]))
        if list_c[min_i] > list_c[j]:
            min_i = j
            print('最小値更新後の値 = {}'.format(list_c[min_i]))
    list_c[i], list_c[min_i] = list_c[min_i], list_c[i]
    print(list_c)
    print('-'*10)
print(list_c)


print('-------------')


"""関数"""

def print_hello(name):
    print('Hello!' + name)

print_hello('sakatai')


def num_max(a, b):
    print('a = {}, b = {}'.format(a, b))
    if a > b:
        return a
    else:
        return b

print(num_max(b=100, a=10))


print('-------------')


def circle(radius, pi=3.14):
    r = radius * radius * pi
    return r

result = circle(45)
print('結界 = {}'.format(result))


def sample(age, *args):
    print('年齢 = {}, 好きな数字 = {}'.format(age, args))
    print(type(args))

sample(25, 8, 1, 88)

def sample_2(year, **args):
    for k, v in args.items():
        print('現在{}年, {key}の年齢は{value}歳'.format(year, key=k, value=v))
    print('type = {}, dictの中身 = {}'.format(type(args), args))

sample_2(2021, yui = 27, sakatai = 25)


print('-------------')


"""グローバル変数"""


def printAnimal():
    # グローバル変数宣言
    global animal
    animal = 'cat'
    print('関数内animal = {}, id = {}'.format(animal, id(animal)))

animal = 'dog'
printAnimal()
print('関数外animal = {}, id = {}'.format(animal, id(animal)))


print('-------------')


"""inner関数とノンローカル変数"""


def outer():

    outer_value = '外側の変数'

    def inner():
        # ノンローカル変数として宣言　外側の変数も書き変えることができる
        nonlocal outer_value
        outer_value = '内側の変数'
        print('inner : outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
    # 外側の関数から内の関数の処理を呼び出す
    inner()
    print('outer : outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

outer()


print('-------------')


"""ジェネレーター関数"""


def generator(max):
    print('ジェネレーター作成')
    for n in range(max):
        # yield 値 を呼び出し元に返す
        yield n
        print('yield実行')

gen = generator(10)
n = next(gen)
print('n = {}'.format(n))
# yield処理がない場合はエラーになる
n = next(gen)
print('n = {}'.format(n))

for x in gen:
    print('x = {}'.format(x))


print('-------------')



"""
ジェネレーター関数のメソッド

send() : yieldで停止している箇所に値を送る
throw() : 指定した例外が発生して処理が終了させる
close() : ジェネレーターを正常終了させる
"""


def generator_a(max):
    print('ジャネレーター作成')
    for n in range(max):
        try:
            # send()を使うときは変数宣言する
            x = yield n
            print('x = {}'.format(x))
            print('yield実行')
        except ValueError as e:
            print('throwを時効しました')

gen = generator_a(10)
next(gen)
# 値を送り込むことができる
gen.send(100)

# 例外処理を無理やり発生させることができる
gen.throw(ValueError('Invalid Value = throw()によって例外発生させた'))

# ジェネレータを終了させる next(gen)としてもエラーになる
# gen.close()

next(gen)


print('-------------')


"""
サブジェネレーター yield from

メイン処理 => ジェネレーター => サブジェネレーター
"""


def sub_sub_generator():
    yield 'SubSubのyield'
    return 'SunSunのreturn'


def sub_generator():
    yield 'Subのyield'

    # sub_sub_generator()のreturnの値がresに格納される
    res = yield from sub_sub_generator()
    print(('Sub res = {}'.format(res)))
    return 'Subのreturn'


def generator():
    yield 'generatorのyield'

    # sub_generator()のreturnの値が格納される
    res = yield from sub_generator()
    print(('gen res = {}'.format(res)))
    return 'generatorのreturn'


gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))
# print(next(gen))


print('-------------')


"""
ジェネレーターの使い道はメモリの使用量を削減することができる
DBの大量のデータを扱うときが有効だが処理速度は遅くなる
"""

import sys

list_a = [i for i in range(100000)]

def num(max):
    i = 0
    while i < max:
        yield i
        i += 1

# for i in list_a:
#     print(i)


gen = num(100000)
print(sys.getsizeof(list_a))
print(sys.getsizeof(gen))


print('-------------')



"""
高階関数
関数を引数として扱うこともできる、また返り値とすることもできる
"""

# def print_hello():
#     print('hello')


# def print_goodbye():
#     print('goodbye')


# var = ['AA', 'BB', print_hello, print_goodbye]
# var[2]()
# var[3]()


def print_world(msg):
    print('{} world'.format(msg))


def print_konnnitiha():
    print('こんにちは')


def print_hello(func):
    func('hello')
    return print_konnnitiha

var = print_hello(print_world)
var()


print('-------------')


"""
lambda式
lambda 引数:返り値
"""


lambda_a = lambda x:x * x

res = lambda_a(10)
print(res)


lambda_b = lambda x, y, z=5:x * y * z

res = lambda_b(10, 10)
print(res)


lambda_c = lambda x, y:y if x < y else x

res = lambda_c(100, 10)
print(res)


y = 10
x = 0 if y > 0 else 1

# print(x)


lambda_d = lambda x: x * x
print(lambda_d(11))


print('-------------')


"""
再帰
関数から自分の関数を呼び出すこと
実務では滅多に使わない、無限ループになる恐れがあるため
"""

def sample(a):
    if a < 0:
        return
    else:
        print(a)
        sample(a-1)

sample(10)


print('-------------')


# フィボナッチ
def fib(n):
    return 1 if n < 3 else fib(n-1) + fib(n-2)

for x in range(1, 10):
    print(fib(x))


print('-------------')


"""
リスト内包表記
変数名 = [式 for 変数 in リスト (if　条件式)]
"""


list_a = (1, 2, 3, 'a', 4, 'b')

list_b = [x*2 for x in list_a if type(x) == int]
print(list_b)

list_c = [x for x in range(100) if x % 7 == 0]
print(list_c)


dict_a = {
    'a': 'apple',
    'b': 'banana'
}

list_d = [dict_a.get(x) for x in list_a if type(x) == str]
print(list_d)


list_a = (x for x in range(10))
print(list_a, type(list_a))

list_b = tuple(x for x in range(10))
print(list_b, type(list_b))

def func_a(n):
    for x in range(2, n):
        if n % x == 0:
            return True
    return False

list_e = [x for x in range(100) if func_a(x) == False]
print(list_e)


print('-------------')


"""
デコレーター関数
@関数名と関数の前につけることで、デコレーター関数として扱える
"""


def my_decorator(func):

    def wrapper(*args, **kwargs):
        print(args[0])
        if args[0] == 1:
            return 1
        print('*' * 100)
        func(*args, **kwargs)
        print('*' * 100)
    return wrapper


@my_decorator
def func_a(*args, **kwargs):
    print('func_aを実行')
    print(args)


@my_decorator
def func_b(*args, **kwargs):
    print('func_bを実行')
    print(args)


func_a(1, 2, 3)
func_b(4, 5, 6)


print('-------------')


"""
Map関数
リスト、辞書のループ可能なクラスの変数を第２引数で入力として受け取り、実行時に第１引数の関数に代入した値を書つ力する
"""


list_a = [1, 2, 3, 4, 5]

map_a = map(lambda x: x * 2, list_a)

for x in map_a:
    print(x)

man = {
    'name': 'sakatai',
    'age': '25',
    'country': 'japan'
}



map_man = map(lambda x: x + ',' + man.get(x), man)
for x in map_man:
    print(x)


print('-------------')



def calcurate(x, y, z):
    if z == 'plus':
        return x + y
    elif z == 'minus':
        return x - y

map_sample = map(calcurate, range(5), [3,3,3,3,3], ['plus', 'minus', 'plus', 'minus', 'plus'])
for x in map_sample:
    print(x)


print('-------------')


"""
マージソート
列を分割し、１まで分割したら併合しながら整列させる
"""

def merge_sort(arr):
    if len(arr) > 1:

        res, i, j = [], 0, 0
        mid = len(arr) // 2
        print('mid = {}'.format(mid))
        L = arr[:mid]
        R = arr[mid:]
        print('L = {}'.format(L))
        print('R = {}'.format(R))
        L = merge_sort(L)
        R = merge_sort(R)

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                res.append(L[i])
                i += 1
            elif L[i] > R[j]:
                res.append(R[j])
                j += 1
            else:
                res.append(L[i])
                i += 1
            print('res = {}'.format(res))

        while i < len(L):
            res.append(L[i])
            i += 1
        while j < len(R):
            res.append(R[j])
            j += 1

        return res
    else:
        return arr

list_t = [6, 5, 4, 2]
print(merge_sort(list_t))


print('-------------')


"""2文探索"""


def binary_search(arr, target):

    start = 0
    end = len(arr) - 1

    while start <= end:
        search_idx = (start + end) // 2
        print('start = {}, end = {}'.format(start, end))
        print('search_idx = {}'.format(search_idx))
        if arr[search_idx] == target:
            return search_idx
        elif arr[search_idx] < target:
            start = search_idx + 1
        else:
            end = search_idx - 1
    return -1

a = [1, 2, 3, 4, 5 ,6 , 7, 8, 9]
print(binary_search(a, 9))
