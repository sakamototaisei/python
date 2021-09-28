# ポリモーフィズムのための標準ライブラリabcからインポート
from abc import ABCMeta, abstractmethod

# 基となる動物クラスAnimal
class Animal(metaclass=ABCMeta): # 抽象クラスABCmetaを利用
  @abstractmethod # インポートした抽象メソッドabstractmethodを使用
  def cry(self): # 抽象メソッドcry()を定義
    pass


class Dog:
  # def cry(self): # cry()をオーバーライド
  #   print('わん')
  def __init__(self, name, weight): # 初期化する特殊メソッド__init__
    self.name = name # self.nameはパブリック変数
    self.__weight = weight # self.__weightはプライベート変数


  def getWeight(self): # __weightのゲッター
    return self.__weight # __weightの値を返却


  def setWeight(self, weight): # __weightのセッター
    self.__weight = weight # __weihgtに値を設定


class Cat(Animal):
  def cry(self):
    print('にゃー')

pochi = Dog('ぽち', 20)
# print(pochi.name)
# print(pochi.__weight)
print(pochi.getWeight()) # ゲッターで、__weightを取得して表示
pochi.setWeight(25)
print(pochi.getWeight())