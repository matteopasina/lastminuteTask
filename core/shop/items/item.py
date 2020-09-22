from decimal import Decimal


class Item:
    def __init__(self, quantity, name, price, imported=False):
        self.name = name
        self.quantity = quantity
        self.imported = imported
        self.price = Decimal(price).quantize(Decimal('.01'))

