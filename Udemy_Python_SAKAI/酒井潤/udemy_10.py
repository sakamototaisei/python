# クラスメソッドとスタティックメソッド


class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    # オブジェクト生成させる前にも使えるようにする
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

# オブジェクト
a = Person()
print(a.x)
print('a', a.what_is_your_kind())


# クラス
b = Person
print('b', b.what_is_your_kind())

Person.about(1996)