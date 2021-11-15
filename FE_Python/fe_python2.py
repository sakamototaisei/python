
class Car(object):
    """車クラス"""

    country = 'japan'
    year = 2021
    name = 'Prius'

    def print_name(self):
        print('print_name実行')
        print(self.name)


my_car = Car()
print(my_car.year)
my_car.print_name()

print('-------------------------')

list_a = ['apple', 'banana', Car]
# second_car = list_a[2]()
# second_car.print_name()
list_a[2]().print_name()

# クラスのドキュメントを確認できる help()関数
# help(Car)


print('-------------------------')


class SampleA(object):
    # クラス変数、直下に記述
    class_val = 'class val'

    def set_val(self):
        # インスタンス変数
        self.instance_val = 'instance val'

    def print_val(self):
        print('クラス変数 = {}'.format(self.class_val))
        print('インスタンス変数 = {}'.format(self.instance_val))

instance_a = SampleA()
instance_a.set_val()
instance_a.print_val()

# 下記クラス変数の呼び出し
print(SampleA.class_val)
print(instance_a.__class__.class_val)


print('-------------------------')


instance_b = SampleA()
instance_b.set_val()
instance_b.print_val()

instance_a.__class__.class_val = 'class val 2'
instance_b.print_val()


print('-------------------------')


print(id(instance_a.__class__.class_val))
print(id(instance_b.__class__.class_val))


print('-------------------------')


"""コンストラクタ"""


class SampleClass(object):

    def __init__(self, msg, name=None):
        print('コンストラクタが呼ばれました')
        self.msg = msg
        self.name = name

    def __del__(self):
        print('デストラクタが実行されました')
        print('name = {}'.format(self.name))

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)


var_1 = SampleClass('Hello!', 'sakatai')
var_1.print_msg()
var_1.print_name()

"""
デストラクタ
インスタンスを削除する際に呼び出される
"""
del var_1


print('-------------------------')


"""
インスタンスメソッド

クラスメソッド
インスタンス化せずに実行することができる,インスタンス変数にはアクセスすることはできない
class_name = 'myclass'

@classmethod
def sample_func(cls):
    print('Hello' + cls.class_name)

スタティックメソッド
ただの普通の関数、クラス変数にもインスタンス変数にもアクセスできない
@staticmethod
def sample_func():
    print('Hello)
"""


class Human(object):

    class_name = 'Human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name_age(self):
        print('インスタンスメソッド実行')
        print('name = {}, age = {}'.format(self.name, self.age))

    @classmethod
    def print_class_name(cls, msg):
        print('クラスメソッド実行')
        print(cls.class_name)
        print(msg)

    @staticmethod
    def print_msg(msg):
        print('スタティックメソッド実行')
        print(msg)

# インスタンス化せずに実行できるが、コンストラクタの値は実行できない
Human.print_class_name('こんにちは')

man = Human('sakatai', 25)
man.print_name_age()

man.print_msg('スタティックメソッド')
Human.print_msg('スタティックメソッドをクラスから呼び出し')


print('-------------------------')


"""
特殊メソッド
"""


class Human(object):

    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return self.name + ', ' + str(self.age) + ', ' + self.phone_number

    # == の時実行される、名前と電話番号が同じならTrueを返すように記述している、今回はman=self man2==otherで比較される
    def __eq__(self, other):
        return (self.name == other.name) and (self.phone_number == other.phone_number)



man = Human('sakatai', 25, '09088881111')
man2 = Human('sakatai', 5, '09088881111')

man_str = str(man)
print(man_str)

print(man == man2)