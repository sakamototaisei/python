# セクション7 オブジェクトとクラス


# s = 'aeroiughahgoiua'

# capitalize() => 一番初めを大文字にする
# print(s.capitalize())


# # クラス名(object)は書いておいた方が良い
# class Person(object):
#   def say_something(self):
#     print('hello')


# person = Person()
# person.say_something()



print('--------------------')


# ---------------------------------------------------------------
# クラスの初期化とクラス変数


class Person(object):
  # コンストラクタ
  def __init__(self, name):
    self.name = name
    print(self.name)

  def say_something(self):
    print('I am {}. hello'.format(self.name))
    # 同じクラス内のメソッドをself.メソッド名で呼び出せる
    self.run(10)

  def run(self, num):
    print('run' * num)

  # デストラクタ
  def __del__(self):
    print('Good bye')




person = Person('Mike')
person.say_something()

# 明示的に呼び出す方法で、最後までコードを読みにいかずこの時点で呼び出される
del person


print('--------------------')


# ---------------------------------------------------------------
# コンストラクタとデストラクタ
# デストラクタ __del__(self)
# コードが最後まで読み込まれた後の最後に__del__()が呼び出される



print('--------------------')


# ---------------------------------------------------------------
# クラスの継承


class Car(object):
  def __init__(self, model=None):
    self.model = model

  def run(self):
    print('run')


# Carを継承している
class ToyotaCar(Car):
  def run(self):
    print('first')

# Carを継承している
class TeslaCar(Car):
  def __init__(self, model='Model S', enable_auto_run=False):
    # self.model = model
    # super() => 親クラスの__init__を呼び出して初期化している
    super().__init__(model)
    self.enable_auto_run = enable_auto_run

  def run(self):
    print('super fast')

  def auto_run(self):
    print('auto run')


car = Car()
car.run()
print('--------------------')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('--------------------')
tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.auto_run()
tesla_car.run()



print('--------------------')


# ---------------------------------------------------------------
# メソッドのオーバーライドとsuperによる親メソッドの呼び出し


