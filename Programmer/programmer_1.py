"""
独学プログラマー

第一部
プログラミングを断固継続
"""

print("""こんにちは、sakataiです。
今日はPythonの学習をやっていきます。
将来はアイアンマンのジャービスを作ります。""")


print('-----------------------')


print\
("""こんにちは、sakataiです。今日はPythonの学習をやっていきます。
将来はアイアンマンのジャービスを作ります。""")


print('-----------------------')


try:
    x = 10 / 0
except ZeroDivisionError as e:
    print('0で割ってはいけません')
    print(e)


print('-----------------------')

def f(x):
    return x * 2

r = f(2)
print(r)


print('-----------------------')

# 関数はreturnを記述しなくてもいいが、returnがない場合はNoneを返す
def func():
    r = 1 + 1

r = func()
print(r)


print('-----------------------')


# age = input('Enter your age : ')
# int_age = int(age)
# if int_age < 20:
#     print('You are young!')
# else:
#     print('Wow, you are old!')


print('-----------------------')


def even_odd(x):
    if x % 2 == 0:
        print('偶数です')
    else:
        print('奇数です')

even_odd(25)
even_odd(20)


print('-----------------------')


"""
ドキュメンテーション
関数および引数を定義するとき、引数が特定のデータ型でないと関数が正しく動作しないことがある
関数を呼び出す人に、関数を呼び出す人にm引数のデータ型を伝える
"""

def add(x, y):
    """
    Returns x + y.
    :param x: int.
    :param y: int.
    :return int sum of x and y.
    """
    return x + y

result = add(10, 25)
print(result)


print('-----------------------')


def sample_func1():

    num = input('数字を入力してください : ')
    int_num = int(num)

    return int_num ** 2

# result = sample_func1()
# print(result)


print('-----------------------')


def float_func():
    try:
        num = input('数値を入力してください : ')
        float_num = float(num)
        return float_num
    except ValueError as e:
        print('正しく数値を入力してください')
        print(e)

result = float_func()
print(result)