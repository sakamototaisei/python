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