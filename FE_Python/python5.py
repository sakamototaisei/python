# クラスの応用


class Dog(object):

    count = 0

    def __init__(self, name):
        self.name = name
        # インスタンス作成ごとに,countに1加えていく
        Dog.count += 1

    # オブジェクトの表現方法を指定
    def __repr__(self):
        return 'Dog object ' + self.name

    # クラスメソッドを表すデコレーター
    @classmethod
    # クラスメソッド。clsはクラス自体を指す
    def display(cls):
        print('Dogクラスには、犬が', cls.count, '匹います。')


pochi = Dog('ぽち')
shiro = Dog('しろ')
hachi = Dog('はち')

print('犬の名前 : ', pochi.name, shiro.name, hachi.name)
# print('犬の数 : ', Dog.count)
Dog.display()


print(pochi)


print('-----------------------------')


from enum import Enum, auto

class Week(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


# week_today = Week.SUNDAY
# print(week_today)

print(Week.SUNDAY.name, Week.SUNDAY.value)


print('-----------------------------')


fruits = ['banana', 'apple', 'melon']

print('original            ', fruits)
print('sorted()            ', sorted(fruits))
print('after sorted        ', fruits)
print('list.sort()         ', fruits.sort())
print('after list.sort()   ', fruits)


print('-----------------------------')


class Practice(object):

    data_list = []

    def add_data_list(self, data):
        self.data_list.append(data)



practice1 = Practice()
practice1.add_data_list('data 1')

practice2 = Practice()
practice1.add_data_list('data 2')


print('data_list : ', end=' ')
for data in practice1.data_list:
    print(data, end=' ')