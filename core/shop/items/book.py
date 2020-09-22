from core.shop.items.item import Item


class Book(Item):
    def __init__(self, quantity, name, price, imported=False):
        super().__init__(quantity, name, price, imported)
