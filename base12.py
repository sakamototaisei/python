# クラス変数やインスタンス変数は外部からアクセスして値を書き換えられたが、アクセスのできない変数(Private変数を定義する)
# ex) __variable Private変数　_を二つつけて定義

class Human:

  __class_val = 'Human'

  def __init__(self, name, age):
    self.__name = name # プライベート変数 クラスの中でしかアクセスできない基本
    self.__age = age

  def print_msg(self):
    print('name = {}, age = {}'.format(self.__name, self.__age))


human = Human('Taro', 25)
human.print_msg()