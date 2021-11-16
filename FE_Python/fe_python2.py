
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

    # 文字列をハッシュ値に変換する
    def __hash__(self):
        return hash(self.name + self.phone_number)

    # if文などでTrueFalseを求めるときに呼び出される
    def __bool__(self):
        return True if self.age >= 20 else False

    # len()関数が使われた際に内部的にはこれを実行
    def __len__(self):
        return len(self.name)



man = Human('taisei', 25, '09088881111')
man2 = Human('taisei', 18, '09088881111')
man3 = Human('jo', 18, '09077776666')

# __str__
man_str = str(man)
print(man_str)

# __eq__
print(man == man2)

# __hash__
print(hash('sakatai'))
print(hash(man2.name))

# set
set_man = {man, man2, man3}
for x in set_man:
    print(x)

# __bool__
if man:
    print('manはTrue')
if man2:
    print('man2はTrue')

# len
print(len(man))
print(len(man3))


print('-------------------------')