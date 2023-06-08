from django.urls import path

from checkout.views import checkout, estimate

urlpatterns = [
    path('<str:category_name>/<str:product_name>/checkout/', checkout, name="checkout"),
    path('<str:category_name>/<str:product_name>/checkout/devis/', estimate, name="estimate"),
]
