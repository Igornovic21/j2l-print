import os
import requests

from django.shortcuts import render

from product.models import Category, Product
from product.utils import Variables

categories = Category.objects.all()[:5]
more_categories = Category.objects.all()[5:]

SHOP_ID = os.environ.get('SHOP_ID')
API_KEY = os.environ.get('API_KEY')

# Create your views here.
def product(request, category_name):
    category = Category.objects.filter(name=category_name.replace("-", " ")).first()
    products = Product.objects.filter(category=category)
    
    context = {
        "categories": categories,
        "more_categories": more_categories,
        "category": category,
        "products": products
    }
    
    return render(request, 'product/product.html', context)


def detail(request, category_name, product_name):
    category = Category.objects.filter(name=category_name.replace("-", " ")).first()
    product = Product.objects.filter(name=product_name.replace("-", " ")).first()
    
    config_data = {
        'shop_id': SHOP_ID,
        'api_key': API_KEY,
        'product': product.ref
    }
    config_response = requests.post('https://www.realisaprint.com/api/configurations', data=config_data)
    
    stock = list(config_response.json()["stocks"].items())[0][0]
    var_id = list(config_response.json()["variables"].items())[0][0]
    var_val = 1
    for val in list(list(config_response.json()["variables"].items())[0][1]["values"].keys()):
        var_val = int(val) if int(val) < 1000 else var_val

    show_variables_post_data = 'shop_id={SHOP_ID}&api_key={API_KEY}&product={product}&stock={stock}&variables%5B{var_id}%5D={var_val}'.format(
        SHOP_ID=SHOP_ID,
        API_KEY=API_KEY,
        product=product.ref,
        stock=stock,
        var_id=var_id,
        var_val=var_val
    )
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'PHPSESSID=qp1g35n8fhsifc7gi7qrdhovjv'
    }

    show_variables_response = requests.post('https://www.realisaprint.com/api/show_variables', headers=headers, data=show_variables_post_data)
    images = list(show_variables_response.json()["pictures"].values())
    show_variables = list(show_variables_response.json().keys())
    
    first_zone_variables = []
    second_zone_variables = []
    
    for k, v in config_response.json()["variables"].items():
        if k in show_variables:
            if v["area"] == "1":
                first_zone_variables.append(
                    Variables(id=k, name=v["name"], type=v["type"], default=v["default"],
                            values=v["values"], readonly=v["readonly"], quantity=v["quantity"],
                            production_time=v["production_time"], area=v["area"], position=v["position"]))
            else:
                second_zone_variables.append(
                    Variables(id=k, name=v["name"], type=v["type"], default=v["default"],
                            values=v["values"], readonly=v["readonly"], quantity=v["quantity"],
                            production_time=v["production_time"], area=v["area"], position=v["position"]))

    # print(first_zone_variables[0].id)
    # print(first_zone_variables[0].name)
    # print(first_zone_variables[0].type)
    # print(first_zone_variables[0].default)
    # print(first_zone_variables[0].values)
    # print(first_zone_variables[0].readonly)
    # print(first_zone_variables[0].quantity)
    # print(first_zone_variables[0].production_time)
    # print(first_zone_variables[0].area)
    # print(first_zone_variables[0].position)
    
    context = {
        "categories": categories,
        "more_categories": more_categories,
        "category": category,
        "first_zone_variables": first_zone_variables,
        "second_zone_variables": second_zone_variables,
        "images": images,
    }
    
    return render(request, 'product/detail.html', context)
    