from django.urls import path

from checkout.views import checkout

urlpatterns = [
    path('<str:category_name>/<str:product_name>/checkout/', checkout, name="checkout"),
]
