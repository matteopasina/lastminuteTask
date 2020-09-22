

class User:
    def __init__(self):
        self.cart = []
        self.total_tax = 0
        self.total_price = 0
        self.total = 0

    def purchase(self, item):
        self.cart.append(item)
