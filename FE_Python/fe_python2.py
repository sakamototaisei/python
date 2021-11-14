
class Car(object):
    """車クラス"""

    country = 'japan'
    year = 2021
    name = 'Prius'

    def print_name(self):
        print('print_name実行')
        print(self.name)


my_car = Car()
print(my_car.year)
my_car.print_name()

print('-------------------------')

list_a = ['apple', 'banana', Car]
# second_car = list_a[2]()
# second_car.print_name()
list_a[2]().print_name()

# クラスのドキュメントを確認できる help()関数
# help(Car)


print('-------------------------')


class SampleA(object):
    # クラス変数、直下に記述
    class_val = 'class val'

    def set_val(self):
        # インスタンス変数
        self.instance_val = 'instance val'

    def print_val(self):
        print('クラス変数 = {}'.format(self.class_val))
        print('インスタンス変数 = {}'.format(self.instance_val))

instance_a = SampleA()
instance_a.set_val()
instance_a.print_val()

# 下記クラス変数の呼び出し
print(SampleA.class_val)
print(instance_a.__class__.class_val)


print('-------------------------')


instance_b = SampleA()
instance_b.set_val()
instance_b.print_val()

instance_a.__class__.class_val = 'class val 2'
instance_b.print_val()


print('-------------------------')


print(id(instance_a.__class__.class_val))
print(id(instance_b.__class__.class_val))


print('-------------------------')

