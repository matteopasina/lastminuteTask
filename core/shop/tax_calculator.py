from decimal import Decimal, ROUND_UP

from core.shop.items.book import Book
from core.shop.items.medical_product import MedicalProduct
from core.shop.items.food import Food
from core.shop.taxes.import_duty_tax import ImportDutyTax
from core.shop.taxes.basic_sales_tax import BasicSalesTax

BasicSalesTaxExceptions = (Book, MedicalProduct, Food)


class TaxCalculator:
    def __init__(self):
        pass

    def get_basic_sales_tax(self, item):
        if not isinstance(item, BasicSalesTaxExceptions):
            return self.round_up(item.price * BasicSalesTax().rate)
        return Decimal(0)

    def get_import_duty_tax(self, item):
        if item.imported:
            return self.round_up(item.price * ImportDutyTax().rate)
        return Decimal(0)

    def get_total_tax(self, item):
        return self.get_basic_sales_tax(item) + self.get_import_duty_tax(item)

    @staticmethod
    def round_up(amount):
        amount = amount.quantize(Decimal('.01'))
        return (amount * 2).quantize(Decimal('.1'), rounding=ROUND_UP) / 2

