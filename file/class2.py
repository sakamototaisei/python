class Car:
    # kind = 'car'

    # def __init__(self, name):
    #   self.name = name

    # def run(self):
    #   print('Car is running.')

    def exclaim(self):
        print('I am car.')


class Truck(Car):
    def exclaim(self):
        super().exclaim() # スーパークラスのexclaim()を使用
        print('I am truck.')

    def baggage(self):
        print('I can carry baggage')

# tesla = Car()
# tesla.run()
# tesla = Car('model 3')
# print(tesla.name)
# cybertruck = Truck('Cyber Truck')
# print(cybertruck.name)


# tesla = Car()
cybertruck = Truck()
# tesla.exclaim()
cybertruck.exclaim()
# cybertruck.baggage()
