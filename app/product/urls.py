from django.urls import path

from product.views import product, detail

urlpatterns = [
    path('<str:category_name>/', product, name="product"),
    path('<str:category_name>/<str:product_name>/', detail, name="detail"),
]
