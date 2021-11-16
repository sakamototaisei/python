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