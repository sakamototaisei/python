""""
クラスの継承

ポリモーフィズム : サブクラスを複数作成して、サブクラスごとに同じ名前のメソッドをそれぞれ作成して、処理の中身を変える。
ex)話すというメソッドで、日本語を話すものと英語を話す的な

オーバーライド : 親クラスのメソッドを上書きして新たに定義すること
オーバーロード : 引数や戻り値が異なるが、名称が同一のメソッドを複数定義すること

"""

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print('hello {}'.format(self.name))

    def say_age(self):
        print('{} years old'.format(self.age))

# 親クラスPersonを継承
class Employee(Person):

    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number = number

    def say_number(self):
        print('my number is = {}'.format(self.number))

    # 親クラスのメソッドをオーバーライド
    def greeting(self, msg=None):
        # 親クラスのgreeting()を呼び出している
        super().greeting()
        print('オーバーライド : I\,m employee phone_number = {}'.format(self.number))

    # Pythonはオーバーロードができない
    # def greeting(self, age):
    #     print('オーバーロード')


man = Employee('sakatai', 25, '09088881111')
man.greeting()
man.say_age()
man.say_number()


print('------------------------')


"""
多重継承

class クラス名(継承先1, 継承先２):
"""


class ClassA(object):

    def __init__(self, name):
        self.a_name = name

    def print_a(self):
        print('ClassAのメソッド')
        print('a = {}'.format(self.a_name))

    def print_hi(self):
        print('A hi')


class ClassB(object):

    def __init__(self, name):
        self.b_name = name

    def print_b(self):
        print('ClassBのメソッド')
        print('b = {}'.format(self.b_name))

    def print_hi(self):
        print('B hi')


class NewClass(ClassA, ClassB):

    def __init__(self, a_name, b_name, name):
        ClassA.__init__(self, a_name)
        ClassB.__init__(self, b_name)
        self.name = name

    def print_new_name(self):
        print('NewClassのメソッド')
        print('name = {}'.format(self.name))

    def print_hi(self):
        ClassA.print_hi(self)
        ClassB.print_hi(self)
        print('NewClass hi')


sample = NewClass('A name', 'B name', 'New name')

sample.print_a()
sample.print_b()
sample.print_new_name()
sample.print_hi()


print('------------------------')


"""
メタクラス

クラスの再定義をするクラスと考えて良い
クラスをチェックする際に適切

class Meta(type):
    def __new__(metacls, name, bases, class_dict):
        # クラスのチェックを行う
        # name : クラスの名前
        # bases : 継承しているクラス
        # class_dict : クラスの持っている値、関数等
        return super().__new__(metacls, name, bases, class_dict)
"""

class MetaException(Exception):
    pass


# type(デフォルトのメタクラス)
class Meta1(type):

    def __new__(metacls, name, bases, class_dict):
        print('metacls = {}'.format(metacls))
        print('name = {}'.format(name))
        print('bases = {}'.format(bases))
        print('class_dict = {}'.format(class_dict))
        # if 'my_var' not in class_dict.keys():
        #     raise MetaException('my_varを定義してください')
        # 継承しているクラス
        # for base in bases:
        #     if isinstance(base, Meta1):
        #         # finalクラス
        #         raise MetaException('継承できません')

        return super().__new__(metacls, name, bases, class_dict)


# ClassAを定義した際にMeta1クラスが呼ばれている、引数で指定しているため
class ClassA(metaclass=Meta1):
    a = '123'
    my_var = 'AAA'
    pass


class ClassB(ClassA):
    pass


print('------------------------')


"""
ポリモーフィズム
サブクラスを複数作成し、同じメソッドを定義して呼び出す際にどのクラスか意識せずに呼び出すこと

from abc import abstractmethod, ABCMeta
"""

from abc import abstractmethod, ABCMeta

class Human(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def say_something(self):
        pass

    def say_name(self):
        print(self.name)


class Woman(Human):

    def say_something(self):
        print('女性 : 名前は = {}'.format(self.name))


class Man(Human):

    def say_something(self):
        print('男性 : 名前は = {}'.format(self.name))

# ポリモーフィズム
# while True:
#     num = input('0か1を入力してください : ')
#     if num == '0':
#         human = Man('sakatai')
#         break
#     elif num == '1':
#         human = Woman('nobu')
#         break
#     else:
#         print('入力が間違っています')
#         continue

# human.say_something()


print('------------------------')


"""
プライベート変数
"""


class Human(object):
    # クラス変数のプライベート変数
    __class_val = 'Human'

    def __init__(self, name, age):
        # __変数名でプライベート変数となる,クラスの外からはアクセスできない
        self.__name = name
        self. __age = age

    def print_msg(self):
        # クラス内からプライベート変数にアクセスしている
        print('name = {}, age = {}'.format(self.__name, self.__age))


human = Human('sakatai', 25)
# プライベート変数を呼び出すことはできるが、あまり使われることはない
print(human._Human__name)

human.print_msg()


print('------------------------')


"""
カプセル化 : プライベート変数を使う際には外部から変数が見えないようにするん必要がある
setterとgetter

def get_変数名():
def set_変数名():

property(get_変数名, set_変数名)
"""

class Human(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print('getter name を実行')
        return self.__name

    def get_age(self):
        print('getter age を実行')
        return self.__age

    def set_name(self, name):
        print('setter name を実行')
        self.__name = name

    def set_age(self, age):
        print('setter age を実行')
        self.__age = age

    # ここでgetterとsetterの呼び出しがされるようになる
    name = property(get_name, set_name)
    age = property(get_age, set_age)

    def print_msg(self):
        print(self.name, self.age)


human = Human('Toro', 25)

# setterの利用
human.name = 'sakatai'
human.age = 26

# getterの利用
name = human.name
age = human.age
print(name, age)

human.print_msg()


print('------------------------')


"""
getterとsetterの2つ目の一般的な利用の仕方
"""


class Human(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # getterの処理
    @property
    def name(self):
        print('getter name 実行')
        return self.__name

    # getterの処理
    @property
    def age(self):
        print('getter age 実行')
        return self.__age

    # setterの処理
    @name.setter
    def name(self, name):
        print('setter name 実行')
        self.__name = name

    # setterの処理
    @age.setter
    def age(self, age):
        print('setter age 実行')
        if age < 0:
            print('0以上を設定してください')
            return
        self.__age = age

human = Human('Maro', 25)
human.name = 'sakatai'
print(human.name)

human.age = -1
print(human.age)


print('------------------------')