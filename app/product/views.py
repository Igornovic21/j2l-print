from django.shortcuts import render

from product.models import Category, Product

categories = Category.objects.all()[:5]
more_categories = Category.objects.all()[5:]

# Create your views here.
def product(request, category_name):
    category = Category.objects.filter(name=category_name).first()
    products = Product.objects.filter(category=category)
    
    context = {
        "categories": categories,
        "more_categories": more_categories,
        "products": products
    }
    
    return render(request, 'product/product.html', context)