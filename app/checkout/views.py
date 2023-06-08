import json

from django.shortcuts import render, redirect

from product.models import Category, Product

from checkout.models import Estimate, UserEstimate
from checkout.forms import UserEstimateForm
from checkout.utils import send_mail_estimate

categories = Category.objects.all()[:5]
more_categories = Category.objects.all()[5:]

# Create your views here.
def checkout(request, category_name, product_name):
    category = Category.objects.filter(name=category_name.replace("-", " ")).first()
    product = Product.objects.filter(name=product_name.replace("-", " ")).first()

    userEstimateForm = UserEstimateForm()
    
    context = {
        "categories": categories,
        "more_categories": more_categories,
        "category": category,
        "product": product,
        "form": userEstimateForm
    }
    
    if request.method == 'POST':
        variables = request.session['variables']
        configurations = request.POST.dict()
        configurations.pop("csrfmiddlewaretoken")
        config_choose = []

        for variable in variables:
            for k, v in variable.items():
                if v["default"] and k in configurations.keys() and v["values"][configurations[k]] != "-----":
                    config_choose.append({v["name"]: v["values"][configurations[k]]})
        
        request.session.setdefault('config_choose', config_choose)
    else:
        return redirect("detail", category_name=category_name, product_name=product_name)
    return render(request, "checkout/checkout.html", context)


def estimate(request, category_name, product_name):
    category = Category.objects.filter(name=category_name.replace("-", " ")).first()
    product = Product.objects.filter(name=product_name.replace("-", " ")).first()
    

    if request.method == 'POST':
        userEstimateForm = UserEstimateForm()

        context = {
            "categories": categories,
            "more_categories": more_categories,
            "category": category,
            "product": product,
            "form": userEstimateForm
        }
        
        config_choose = request.session['config_choose']
        userEstimateForm = UserEstimateForm(request.POST or None)

        if userEstimateForm.is_valid():
            userEstimateForm.save()
            userEstimate = UserEstimate.objects.get(email=userEstimateForm.cleaned_data["email"])
            Estimate.objects.get_or_create(configurations=json.dumps(config_choose), user=userEstimate)
            res = send_mail_estimate(userEstimate, config_choose)
            print(res)
            return render(request, "checkout/devis.html", context)
        else:
            for err in list(userEstimateForm.errors.values()):
                if err[0] == "User estimate with this Email already exists.":
                    userEstimate = UserEstimate.objects.get(email=request.POST["email"])
                    Estimate.objects.get_or_create(configurations=json.dumps(config_choose), user=userEstimate)
                    res = send_mail_estimate(userEstimate, config_choose)
                    print(res)
                    return render(request, "checkout/devis.html", context)
        return render(request, "checkout/checkout.html", context)
    else:
        return redirect("checkout", category_name=category_name, product_name=product_name)
