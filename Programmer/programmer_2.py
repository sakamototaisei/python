"""
独学プログラマー

第二部

プログラミングパラダイム : プログラミングのスタイル・手法のこと
状態(ステート) : プログラムが動いている時の変数の値のこと
グローバルステート : プログラム実行中のグローバル変数の値のこと
"""


class Orange(object):

    def __init__(self, w, c):
        """weight(重さ)はグラム"""
        self.weight = w
        self.color = c
        self.mold = 0
        print('Created!')

    def rot(self, days, temp):
        """temp(湿度)は摂氏"""
        self.mold = days * temp


orl = Orange(10, 'dark orange')
print(orl)
print(orl.weight)
print(orl.color)

print('-----------------------')

orl.weight = 100
orl.color = 'green'

print(orl.weight)
print(orl.color)

print('-----------------------')

orange = Orange(200, 'orange')
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)


print('-----------------------')


class Rectangle(object):

    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())

rectangle.change_size(20, 40)
print(rectangle.area())


print('-----------------------')


"""
オブジェクト指向プログラミングの４大要素

カプセル化
オブジェクトによって複数の変数とメソッドをまとめること
データをクラス内に隠蔽して外から見えないようにすること

抽象化
対象から小さな特徴を除いて、本質的な特徴だけを集めた状態にする手順

ポリモーフィズム
同じインターフェースでありながらデータ型に合わせて異なる動作をする機能
ex)print(), type()関数など引数によって動作が変わる

継承

"""


class PublicPrivateExample(object):

    def __init__(self):
        self.public = 'self'
        self._unsafe = 'unsafe'

    def public_method(self):
        pass

    def _unsafe_method(self):
        pass


print('-----------------------')


class Shape(object):

    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print('{} by {}'.format(self.width, self.len))


class Square(Shape):

    def area(self):
        return self.width * self.len

    # 親クラスのメソッドオーバーライド
    def print_size(self):
        print('I am {} by {}'.format(self.width, self.len))


my_shape = Shape(20, 25)
my_shape.print_size()

print('-----------------------')

squqre_a = Square(20, 20)
squqre_a.print_size()
print(squqre_a.area())

print('-----------------------')


"""
コンポジション
has-a関係を表し、別のクラスのオブジェクトを変数として持たせる
"""

class Dog(object):

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person(object):

    def __init__(self, name):
        self.name = name


sakatai = Person('Sakatai')
# 引数にPerson()クラスで作成したオブジェクトをownerに設定
stan = Dog('mi-tan', 'tinntira', sakatai)

print(stan.owner.name)


print('-----------------------')


"""
もっとオブジェクト指向プログラミング
"""

class Square(object):
    pass

print(Square)

print('-----------------------')


class Rectangle(object):
    recs = []

    def __init__(self, w, l):
        # インスタンス変数
        self.width = w
        self.len = l
        # タプルでrecsに追加している
        self.recs.append((self.width, self.len))

    def print_size(self):
        print('{} by {}'.format(self.width, self.len))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)


print('-----------------------')


class Lion(object):

    def __init__(self, name):
        self.name = name

    # オブジェクトをprint()に渡すと、objectクラスから継承した__repr__という特殊メソッドを呼び出す
    def __repr__(self):
        return self.name


lion = Lion('sakatai')
print(lion)

print('-----------------------')


class AlwaysPositive(object):

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        """abs()関数は絶対値を求める"""
        return abs(self.number + other.number)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)


print('-----------------------')


"""
is
isキーワードは、前後のオブジェクトが同一のオブジェクトならTrueを返す。
同じでないならFalseを返す
"""


class Person(object):

    def __init__(self):
        self.name = 'Sakatai'

sakatai = Person()
same_sakatai = sakatai
print(sakatai is same_sakatai)


another_sakatai = Person()
print(sakatai is another_sakatai)


print('-----------------------')


x = 10
if x is None:
    print('x はNone')
else:
    print('x はNoneじゃない')

x = None
if x is None:
    print('x はNone')
else:
    print('x はNoneじゃない')