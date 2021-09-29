class Dog:
  count = 0 # countはクラス変数
  def __init__(self, name):
    self.name = name # nameはインスタンス変数
    Dog.count += 1 # インスタンス作成ごとに、countに1を加える


  def __repr__(self): # オブジェクトの表示方法を指定
    return 'Dog object {}'.format(self.name)


  @classmethod # クラスメソッドを示すデコレーター
  def display(cls): # clsはクラス自体を指す
    print('Dogクラスには、犬が{}匹います'.format(cls.count))


pochi = Dog('ぽち')
shiro = Dog('しろ')
hachi = Dog('はち')
print('犬の名前: {}, {}, {}'.format(pochi.name, shiro.name, hachi.name))
# print('犬の数: {}匹'.format(Dog.count))
Dog.display()
print(pochi)