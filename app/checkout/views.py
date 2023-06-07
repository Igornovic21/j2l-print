from django.shortcuts import render, redirect

from product.models import Category, Product
from checkout.forms import UserEstimateForm

categories = Category.objects.all()[:5]
more_categories = Category.objects.all()[5:]

# Create your views here.
def checkout(request, category_name, product_name):
    category = Category.objects.filter(name=category_name.replace("-", " ")).first()
    product = Product.objects.filter(name=product_name.replace("-", " ")).first()

    variables = request.session['variables']
    
    context = {
        "categories": categories,
        "more_categories": more_categories,
        "category": category,
        "product": product,
    }
    
    if request.method == 'POST':
        configurations = request.POST.dict()
        configurations.pop("csrfmiddlewaretoken")

        for variable in variables:
            for k, v in variable.items():
                if v["default"] and k in configurations.keys() and v["values"][configurations[k]] != "-----":
                    print(v["name"] + " : ", v["values"][configurations[k]])
    else:
        return redirect("detail", category_name=category_name, product_name=product_name)
    return render(request, "checkout/checkout.html", context)

def estimate(request):
    if request.method == 'POST':
        registerForm = UserEstimateForm.Register(request.POST)
        if registerForm.is_valid():
            print("valid")
        else:
            print("not valid")