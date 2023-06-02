from django.urls import path

from product.views import product

urlpatterns = [
    path('<str:category_name>/', product, name="product"),
]
