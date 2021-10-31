# 多重継承
# なければない方が良いとされている

class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')


class Car(object):
    def run(self):
        print('car run')

# クラスを2つ継承している, 同じメソッド名があったときに、引数の左側の方から見つけたものを実行する
class PersonCarRobot(Car, Person):
    def fry(self):
        print('fry')


person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fry()