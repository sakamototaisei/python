"""
独学プログラマー

第二部

プログラミングパラダイム : プログラミングのスタイル・手法のこと
状態(ステート) : プログラムが動いている時の変数の値のこと
グローバルステート : プログラム実行中のグローバル変数の値のこと
"""


class Orange(object):

    def __init__(self, w, c):
        """weight(重さ)はグラム"""
        self.weight = w
        self.color = c
        self.mold = 0
        print('Created!')

    def rot(self, days, temp):
        """temp(湿度)は摂氏"""
        self.mold = days * temp


orl = Orange(10, 'dark orange')
print(orl)
print(orl.weight)
print(orl.color)

print('-----------------------')

orl.weight = 100
orl.color = 'green'

print(orl.weight)
print(orl.color)

print('-----------------------')

orange = Orange(200, 'orange')
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)


print('-----------------------')


class Rectangle(object):

    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())

rectangle.change_size(20, 40)
print(rectangle.area())


print('-----------------------')


"""
オブジェクト指向プログラミングの４大要素

カプセル化
オブジェクトによって複数の変数とメソッドをまとめること
データをクラス内に隠蔽して外から見えないようにすること

抽象化
対象から小さな特徴を除いて、本質的な特徴だけを集めた状態にする手順

ポリモーフィズム
同じインターフェースでありながらデータ型に合わせて異なる動作をする機能
ex)print(), type()関数など引数によって動作が変わる

継承

"""


class PublicPrivateExample(object):

    def __init__(self):
        self.public = 'self'
        self._unsafe = 'unsafe'

    def public_method(self):
        pass

    def _unsafe_method(self):
        pass


print('-----------------------')


class Shape(object):

