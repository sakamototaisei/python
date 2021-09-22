# クラスの定義

# class Car:
#   """車クラス"""
#   country = 'Japan'
#   year = 2021
#   name = 'Prius' # プロパティ
#   def print_name(self):
#     print('print_name実行')
#     print(self.name)

# my_car = Car() # インスタンス化
# print(my_car.year)
# my_car.print_name()

# list_a = ['apple', 'banana', Car()]
# # second_car = list_a[2]()
# # second_car.print_name()
# list_a[2].print_name()

# # help(Car)
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー



# インスタンス変数、クラスへんすう

# class SampleA():
#   class_val = 'class val' # クラス変数

#   def set_val(self):
#     self.instance_val = 'instance val' # インスタンス変数

#   def print_val(self):
#     print('クラス変数 = {}'.format(self.class_val))
#     print('インスタンス変数 = {}'.format(self.instance_val))


# isinstance_a = SampleA() # インスタンス化
# isinstance_a.set_val()
# print(isinstance_a.instance_val)
# isinstance_a.print_val()

# print(SampleA.class_val)
# print(isinstance_a.__class__.class_val) # クラス変数の呼び出し

# isinstance_b = SampleA() # インスタンス化
# isinstance_b.set_val()
# isinstance_b.print_val()
# isinstance_a.__class__.class_val = 'class val 2'
# isinstance_b.print_val()

# print('*'*100)
# print(id(isinstance_a.__class__.class_val))
# print(id(isinstance_b.__class__.class_val))
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー



# オブジェクトをインスタンスかする際に呼び出されるメソッドをコンストラクタと言う __init__
# ex)クラスのプロパティを初期化する際などに、コンストラクタを利用する

# class SampleClass:
#   def __init__(self, msg, name=None): # コンストラクタ
#     print('コンストラクタが呼ばれました')
#     self.msg = msg # インスタンス変数
#     self.name = name # インスタンス変数

#   def __del__(self):
#     print('デストラクタが実行されました')
#     print('name = {}'.format(self.name))


#   def print_msg(self):
#     print(self.msg)


#   def print_name(self):
#     print(self.name)


# var_1 = SampleClass('Hello', 'SAKATAI')
# var_1.print_msg()
# var_1.print_name()
# # デストラクタ(__del__)を定義すると、インスタンスを削除する際に呼び出される
# del var_1
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー



# クラスメソッドには、インスタンスメソッド、クラスメソッド、スタティックメソッドの三種類があります

# インスタンスメソッドとは、クラスから作成したオブジェクト(インスタンス)を用いて呼び出すメソッド def メソッド名(self):

# クラスメソッドとは、クラスをインスタンスかせずに実行できるメソッド
# @classmethod
# def メソッド名(cls):
# cls.変数名とする事で、クラス変数にアクセスできる。初期化されていないため、インスタンス変数にアクセスはできない

# スタティックメソッドとは、インスタスタンスメソッドや暗くメソッドのようにインスタンスやクラスが引数に渡されることはしない
# @staticmethod
# def メソッド名():
# クラス変数もインスタンス変数もアクセスできない

# class Human:

#   class_name = "SAKATAI" # クラス変数

#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def print_name_age(self): # インスタンスメソッド
#     print('インスタンスメソッド実行')
#     print('name = {}, age = {}'.format(self.name, self.age))

#   @classmethod
#   def print_class_name(cls, msg): # クラスメソッド
#     print('クラスメソッド実行')
#     print(cls.class_name) # クラス変数
#     print(msg)

#   @staticmethod
#   def print_msg(msg): # スタティックメソッド
#     print('スタティックメソッド実行')
#     print(msg)


# Human.print_class_name('こんにちは') # クラスメソッド

# man = Human('桜木', 18) # インスタンスメソッド
# man.print_name_age()

# man.print_msg('hello static') # スタティックメソッド
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー



# 特殊メソッド、インスタンスにアクセスする際に、特定の処理を実行すると呼び出されるメソッド

# __str__:str(object),print(object)の際に呼び出され、オブジェクトを文字列として返す
# __bool__:if文で理論値を返す事ができる
# __len__:len()実行時に呼び出される
# __eq__:==の際に呼びだされる
# __hash__:文字列をハッシュ値として返す。この関数を定義する事で、クラスを辞書型として扱うときやsetに要素を入れる際に利用する
# __name__:クラスの名前を返す

class Human:

  def __init__(self, name, age, phone_number):
    self.name = name
    self.age = age
    self.phone_number = phone_number


  def __str__(self):
    return self.name + ',' + str(self.age) + ',' + self.phone_number

  def __eq__(self, other):
    return (self.name == other.name) and (self.phone_number == other.phone_number)

  def __hash__(self):
    return hash(self.name + self.phone_number)

  def __bool__(self):
    return True if self.age >= 20 else False

  def __len__(self):
    return len(self.name)


man = Human('Taro', 20, '09088886767')
man2 = Human('Taro2', 18, '09088886767')
man3 = Human('sakatai', 18, '08088886767')

man_str = str(man)
print(man_str)

print(man == man2)

# print(hash('SAKATAI'))
# print(hash('SAKATAI'))
# print(hash('sakatai'))

set_man = {man, man2, man3}
for x in set_man:
  print(x)


if man:
  print('manはTrue')
if man2:
  print('man2はTrue')


print(len(man))
print(len(man2))
print(len(man3))