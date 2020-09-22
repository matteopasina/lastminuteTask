from unittest import TestCase
from decimal import Decimal

from core.shop.user import User
from core.shop.items.item import Item
from core.shop.items.food import Food
from core.shop.tax_calculator import TaxCalculator
from core.shop.cash_register import CashRegister


class TestImported(TestCase):
    def setUp(self) -> None:
        self.user = User()
        self.tax_calculator = TaxCalculator()
        self.cash_register = CashRegister(self.tax_calculator)

    def test_purchase(self):
        choco = Food(1, 'imported box of chocolates', 10.00, imported=True)
        perfume = Item(1, 'imported bottle of perfume', 47.50, imported=True)
        self.user.purchase(choco)
        self.user.purchase(perfume)
        self.assertEqual(2, len(self.user.cart))

    def test_tax_calculator(self):
        choco = Food(1, 'imported box of chocolates', 10.00, imported=True)
        basic_tax_choco = self.tax_calculator.get_basic_sales_tax(choco)
        self.assertEqual(Decimal(0), basic_tax_choco)
        import_duty_tax_choco = self.tax_calculator.get_import_duty_tax(choco)
        self.assertEqual(Decimal('0.5'), import_duty_tax_choco)
        total_tax_choco = self.tax_calculator.get_total_tax(choco)
        self.assertEqual(Decimal('0.5'), total_tax_choco)

        perfume = Item(1, 'imported bottle of perfume', 47.50, imported=True)
        basic_tax_perfume = self.tax_calculator.get_basic_sales_tax(perfume)
        self.assertEqual(Decimal('4.75'), basic_tax_perfume)
        import_duty_tax_perfume = self.tax_calculator.get_import_duty_tax(perfume)
        self.assertEqual(Decimal('2.4'), import_duty_tax_perfume)
        total_tax_perfume = self.tax_calculator.get_total_tax(perfume)
        self.assertEqual(Decimal('7.15'), total_tax_perfume)

    def test_print_receipt(self):
        choco = Food(1, 'imported box of chocolates', 10.00, imported=True)
        perfume = Item(1, 'imported bottle of perfume', 47.50, imported=True)
        self.user.purchase(choco)
        self.user.purchase(perfume)
        receipt = self.cash_register.print_receipt(self.user.cart)
        expected_receipt = ['1 imported box of chocolates: 10.50',
                            '1 imported bottle of perfume: 54.65',
                            'Sales Taxes: 7.65',
                            'Total: 65.15']
        self.assertEqual(expected_receipt, receipt)
