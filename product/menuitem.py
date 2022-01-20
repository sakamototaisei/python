class MenuItem(object):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': ' + str(self.price) + '円'

    def get_total_price(self, count):
        total_price = self.price * count
        if count >= 3:
            total_price *= 0.9
        return total_price