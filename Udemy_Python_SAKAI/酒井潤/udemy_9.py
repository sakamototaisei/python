# クラス変数


class Person(object):
    # クラス変数 クラスの内の全てのオブジェクトで共有される _＿init__などで初期化しなくて良いもの共有したいものに使う
    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()

a = Person('B')
a.who_are_you()

print('--------------------')


class T(object):

    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)


c = T()
c.add_word('add 1')
c.add_word('add 2')
print(c.words)


d = T()
d.add_word('add 3')
d.add_word('add 4')
# クラス変数だとリストが共有されてしまう
print(d.words)