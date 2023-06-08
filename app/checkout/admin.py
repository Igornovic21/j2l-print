from django.contrib import admin

from checkout.models import UserEstimate, Estimate

# Register your models here.
admin.site.register(UserEstimate)
admin.site.register(Estimate)