class Person:  # 人間クラス
    def __init__(self, name):
        self.name = name

    def hello(self):  # hello()メソッド
        print('こんにちは')  # 実際に挨拶するのは人間


class Dog:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner  # ownerに、人間クラスにインスタンスを設定

    def hello(self):  # hello()メソッド
        self.owner.hello()  # ownerに、hello()メソッドの実行を委譲

ken = Person('けん')
pochi = Dog('ぽち', ken)

print(pochi.owner.name)
print(pochi.name)
pochi.hello()