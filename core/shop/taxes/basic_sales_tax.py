from decimal import Decimal

from core.shop.taxes.tax import Tax


class BasicSalesTax(Tax):
    def __init__(self):
        self._rate = Decimal(0.10)

    @property
    def rate(self):
        return self._rate
