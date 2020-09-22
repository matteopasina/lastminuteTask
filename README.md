# lastminute.com task
PROBLEM: Sales Taxes

Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical
products that are exempt. Import duty is an additional sales tax applicable on all imported goods
at a rate of 5%, with no exemptions.
When I purchase items I receive a receipt which lists the name of all the items and their price
(including tax), finishing with the total cost of the items, and the total amounts of sales taxes
paid. The rounding rules for sales tax are that for a tax rate of n%, a shelf price of p contains
(np/100 rounded up to the nearest 0.05) amount of sales tax.

The application that I wrote to solve this problem is in python 3, 
the application code is in core/shop while the unittests are in the folder 
tests.

The products that you can buy are in the folder items, 
a generic Item class is provided
and three classes inherit from it: food, book and medical product.
Similarly in the folder taxes you can find the classes related to 
the taxes(basic sales tax and imported duty tax).
The logic is handled by the three classes:
* user: that can add to his cart the items
* tax_calculator: computes the taxes relative to an item
* cash_register: computes the receipt for a cart of a user

This repo is linked to this travis CI build https://travis-ci.org/github/matteopasina/lastminuteTask