"""
カプセル化

"""

class Dog(object):
    def __init__(self, name, weight):
        # self.nameはパブリック変数
        self.name = name
        # self.__weightはプライベート変数
        self.__weight = weight

    # __weightのゲッター
    def getWeight(self):
        return self.__weight

    # __weightのセッター
    def setWeight(self, weight):
        self.__weight = weight


pochi = Dog('ぽち', 20)
print(pochi.name)

# # このままだとエラーになる
# print(pochi.__weight)

# ゲッターで、__weightの値を取得して表示
print(pochi.getWeight())

# セッターで、__weightに25を設定
pochi.setWeight(25)
print(pochi.getWeight())


print('-----------------------------')


"""
集約(コンポジション)

"""

class Person(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print('こんにちは')


class Dog(object):
    def __init__(self, name, owner):
        self.name = name
        # ownerに、人間クラスのインスタンスを設定
        self.owner = owner

    def hello(self):
        # ownerに、hello()メソッドの実行を委譲
        self.owner.hello()


ken = Person('けん')
pochi = Dog('ぽち', ken)

print(pochi.owner.name)
pochi.hello()


print('-----------------------------')


class Car(object):
    kind = 'Car'

    def __init__(self, name):
        self.name = name

    def run(self):
        print('Car is running')

    def exclaim(self):
        print('I am a car.')


class Truck(Car):
    def exclaim(self):
        # スーパークラスのexclaim()を利用
        super().exclaim()
        print('I am a truck.')

    def baggage(self):
        print('I can carry baggage.')


print(Car.kind)

tesla = Car('Model 1')
cybertuck = Truck('Cyber Truck')

tesla.run()
print(tesla.name)
tesla.exclaim()

print('-----------------------------')

cybertuck.run()
print(cybertuck.name)
cybertuck.exclaim()
cybertuck.baggage()

print('-----------------------------')