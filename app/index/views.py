from django.shortcuts import render
from product.models import Category

categories = Category.objects.all()[:5]
more_categories = Category.objects.all()[5:]

# Create your views here.
def index(request):
    
    context = {
        "categories": categories,
        "more_categories": more_categories
    }
    
    return render(request, 'index/index.html', context)

def contact(request):
    
    context = {
        "categories": categories,
        "more_categories": more_categories
    }
    
    return render(request, 'index/contact.html', context)