from decimal import Decimal

from core.shop.taxes.tax import Tax


class ImportDutyTax(Tax):
    def __init__(self):
        self._rate = Decimal(0.05)

    @property
    def rate(self):
        return self._rate


