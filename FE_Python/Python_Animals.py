"""
継承とポリモーフィズムを用いた演習

Animalsクラスにspeakという抽象メソッドを定義

Dogクラスを作成して : speakメソッドを実行すると「わん」
Catクラスを作成して : speakメソッドを実行すると「にゃー」
Sheepクラスを作成して : speakメソッドを実行すると[メー」
Otherクラスを作成して : speakメソッドを実行すると「そんな動物はいない」

ユーザーからの入力を受け付け
1の場合はDogクラスのspeakメソッドを
2の場合はCatクラスのspeakメソッドを
3の場合はSheepクラスのspeakメソッドを
それ以外はOtherクラスのspeakメソッドを
"""
from abc import abstractmethod, ABCMeta

class Animals(metaclass=ABCMeta):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animals):

    def speak(self):
        print('わん')

class Cat(Animals):

    def speak(self):
        print('にゃー')

class Sheep(Animals):

    def speak(self):
        print('めー')

class Other(Animals):

    def speak(self):
        print('そんな動物はいない')

num = input('指定の数字を入力してください. 1:Dog, 2:Cat, 3:Sheep ')
if num == '1':
    animal = Dog()
elif num == '2':
    animal = Cat()
elif num == '3':
    animal = Sheep()
else:
    animal = Other()

animal.speak()