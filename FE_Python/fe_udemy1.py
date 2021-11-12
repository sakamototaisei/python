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
