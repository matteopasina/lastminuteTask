from decimal import Decimal

RECEIPT_LINE_FORMAT = '{} {}: {:.2f}'
SALES_TAXES = 'Sales Taxes: {:.2f}'
TOTAL = 'Total: {:.2f}'


class CashRegister:
    def __init__(self, tax_calculator):
        self.tax_calculator = tax_calculator

    def print_receipt(self, cart):
        total_tax = total = Decimal(0)
        receipt = []
        for item in cart:
            item_tax = self.tax_calculator.get_total_tax(item)
            total_tax += item_tax

            price_with_tax = item.price + item_tax
            total += price_with_tax

            receipt_line = RECEIPT_LINE_FORMAT.format(item.quantity, item.name, price_with_tax)
            receipt.append(receipt_line)

        receipt.append(SALES_TAXES.format(total_tax))
        receipt.append(TOTAL.format(total))

        for line in receipt:
            print(line)

        return receipt
