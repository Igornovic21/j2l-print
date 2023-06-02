from django.conf import settings

import json

from product.models import Category, Product

def insert_category():
    with open(str(settings.BASE_DIR) + "\product\data\categories.json", "r") as outfile:
        categories = json.load(outfile)
        for category in categories:
            category_obj, _ = Category.objects.get_or_create(name=category["name"])
            print(category_obj)
            print(_)

def insert_product():
    with open(str(settings.BASE_DIR) + "\product\data\products.json", "r") as outfile:
        products = json.load(outfile)
        for product in products:
            category_obj = Category.objects.get(name=product['category'])
            product_obj, _ = Product.objects.get_or_create(ref=product['id'], name=product['name'], category=category_obj)
            print(product_obj)
            print(_)