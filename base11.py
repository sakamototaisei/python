# サブクラスを作成し、同じメソッドを定義して呼び出す際にどのクラスか意識せずに呼び出すこと

from abc import abstractclassmethod, ABCMeta

class Human(metaclass=ABCMeta): # 親クラス

  def __init__(self, name):
    self.name = name

  @abstractclassmethod
  def say_someting(self):
    pass

  def say_name(self):
    print(self.name)


class Woman(Human):

  def say_someting(self):
      print('女性：名前は = {}'.format(self.name))


class Man(Human):
  def say_someting(self):
      print('男性：名前は = {}'.format(self.name))


# ポリモーフィズム
num = input('0か1を入力して下さい ')
if num == '0':
  human = Man('Taro')
elif num == '1':
  human = Woman('Hanako')
else:
  print('間違っています')
human.say_someting()