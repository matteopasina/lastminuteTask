from unittest import TestCase
from decimal import Decimal

from core.shop.user import User
from core.shop.items.item import Item
from core.shop.items.food import Food
from core.shop.items.medical_product import MedicalProduct
from core.shop.tax_calculator import TaxCalculator
from core.shop.cash_register import CashRegister


class TestComplex(TestCase):
    """
    This class tests Input 3:
    1 imported bottle of perfume at 27.99
    1 bottle of perfume at 18.99
    1 packet of headache pills at 9.75
    1 box of imported chocolates at 11.25
    """
    def setUp(self) -> None:
        self.user = User()
        self.tax_calculator = TaxCalculator()
        self.cash_register = CashRegister(self.tax_calculator)

    def test_purchase(self):
        imported_perfume = Item(1, 'imported bottle of perfume', 27.99, imported=True)
        perfume = Item(1, 'bottle of perfume', 18.99)
        headache_pills = MedicalProduct(1, 'packet of headache pills', 9.75)
        chocolate_bar = Food(1, 'imported box of chocolates', 11.25, imported=True)
        self.user.purchase(imported_perfume)
        self.user.purchase(perfume)
        self.user.purchase(headache_pills)
        self.user.purchase(chocolate_bar)
        self.assertEqual(4, len(self.user.cart))

    def test_tax_calculator(self):
        imported_perfume = Item(1, 'imported bottle of perfume', 27.99, imported=True)
        basic_tax_perfume = self.tax_calculator.get_basic_sales_tax(imported_perfume)
        self.assertEqual(Decimal('2.8'), basic_tax_perfume)

        imported_tax_perfume = self.tax_calculator.get_import_duty_tax(imported_perfume)
        self.assertEqual(Decimal('1.4'), imported_tax_perfume)

        imported_tax_perfume = self.tax_calculator.get_total_tax(imported_perfume)
        self.assertEqual(Decimal('4.2'), imported_tax_perfume)

        headache_pills = MedicalProduct(1, 'packet of headache pills', 9.75)
        total_tax_pills = self.tax_calculator.get_total_tax(headache_pills)
        self.assertEqual(Decimal(0), total_tax_pills)

        chocolate_bar = Food(1, 'imported box of chocolates', 11.25, imported=True)
        total_tax_choco = self.tax_calculator.get_total_tax(chocolate_bar)
        self.assertEqual(Decimal('0.6'), total_tax_choco)

    def test_print_receipt(self):
        imported_perfume = Item(1, 'imported bottle of perfume', 27.99, imported=True)
        perfume = Item(1, 'bottle of perfume', 18.99)
        headache_pills = MedicalProduct(1, 'packet of headache pills', 9.75)
        chocolate_bar = Food(1, 'imported box of chocolates', 11.25, imported=True)
        self.user.purchase(imported_perfume)
        self.user.purchase(perfume)
        self.user.purchase(headache_pills)
        self.user.purchase(chocolate_bar)
        receipt = self.cash_register.print_receipt(self.user.cart)
        expected_receipt = ['1 imported bottle of perfume: 32.19',
                            '1 bottle of perfume: 20.89',
                            '1 packet of headache pills: 9.75',
                            '1 imported box of chocolates: 11.85',
                            'Sales Taxes: 6.70',
                            'Total: 74.68']
        self.assertEqual(expected_receipt, receipt)
