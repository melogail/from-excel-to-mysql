#! python3

"""
    Main file to run package code. Import all the table models you desire to use in this file.
    ex: from models.Product import Product
        product = Product()
"""

from models.Brand import Brand
from models.Product import Product

products = Product()

print(products.all())
