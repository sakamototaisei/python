from menuitem import MenuItem


class Food(MenuItem):
    def __init__(self, name, price, calorie):
        super().__init__(name, price)
        self.calorie = calorie

    def info(self):
        return self.name + ': ' + str(self.price) + '円' + str(self.calorie) + 'kcal'