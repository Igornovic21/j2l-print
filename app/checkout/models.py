from django.db import models

# Create your models here.
class UserEstimate(models.Model):
    first_name = models.CharField(max_length=150, default="")
    last_name = models.CharField(max_length=150, default="")
    organisation = models.CharField(max_length=150, default="")
    phone = models.CharField(max_length=150, default="")
    address = models.CharField(max_length=150, default="")
    postal_code = models.CharField(max_length=150, default="")
    city = models.CharField(max_length=150, default="")
    message = models.TextField(default="")
    email = models.EmailField(unique=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Estimate(models.Model):
    configurations = models.TextField(default="")
    user = models.ForeignKey(UserEstimate, on_delete=models.CASCADE)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return "Estimation by " + self.user.first_name + " " + self.user.last_name