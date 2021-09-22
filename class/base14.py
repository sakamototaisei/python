# getter, setter その2

class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        print('getter nameが呼ばれました')
        return self.__name

    @property
    def age(self):
        print('getter ageが呼ばれました')
        return self.__age

    @name.setter
    def name(self, name):
        print('setter nameが呼ばれました')
        self.__name = name

    @age.setter
    def age(self, age):
        print('setter ageが呼ばれました')
        if age < 0:
            print('0以上の値を設定して下さい')
            return
        self.__age = age


human = Human('Koichi', 22)
human.name = 'Makoto'
print(human.name)
human.age = -1
print(human.age)
