from unittest import TestCase
from decimal import Decimal

from core.shop.user import User
from core.shop.items.item import Item
from core.shop.items.book import Book
from core.shop.items.food import Food
from core.shop.tax_calculator import TaxCalculator
from core.shop.cash_register import CashRegister


class TestBasic(TestCase):
    def setUp(self) -> None:
        self.user = User()
        self.tax_calculator = TaxCalculator()
        self.cash_register = CashRegister(self.tax_calculator)

    def test_purchase(self):
        book = Book(1, 'book', 12.49)
        music_cd = Item(1, 'music CD', 14.99)
        chocolate_bar = Food(1, 'chocolate bar', 0.85)
        self.user.purchase(book)
        self.user.purchase(music_cd)
        self.user.purchase(chocolate_bar)
        self.assertEqual(3, len(self.user.cart))

    def test_tax_calculator(self):
        book = Book(1, 'book', 12.49)
        basic_tax_book = self.tax_calculator.get_basic_sales_tax(book)
        self.assertEqual(Decimal(0), basic_tax_book)

        music_cd = Item(1, 'music CD', 14.99)
        basic_tax_generic = self.tax_calculator.get_basic_sales_tax(music_cd)
        self.assertEqual(Decimal('1.5'), basic_tax_generic)

    def test_print_receipt(self):
        book = Book(1, 'book', 12.49)
        music_cd = Item(1, 'music CD', 14.99)
        chocolate_bar = Food(1, 'chocolate bar', 0.85)
        self.user.purchase(book)
        self.user.purchase(music_cd)
        self.user.purchase(chocolate_bar)
        receipt = self.cash_register.print_receipt(self.user.cart)
        expected_receipt = ['1 book: 12.49',
                            '1 music CD: 16.49',
                            '1 chocolate bar: 0.85',
                            'Sales Taxes: 1.50',
                            'Total: 29.83']
        self.assertEqual(expected_receipt, receipt)
