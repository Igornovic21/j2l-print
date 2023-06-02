from django.urls import path

from index.views import index, contact

urlpatterns = [
    path('', index, name="index"),
    path('contact-us/', contact, name="contact"),
]
