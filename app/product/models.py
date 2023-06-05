from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, default=None, null=True, blank=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name

    def to_url(self) -> str:
        return self.name.replace(" ", "-")


class Product(models.Model):
    ref = models.IntegerField()
    name = models.CharField(max_length=250, default=None, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null=True, blank=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name

    def to_url(self) -> str:
        return self.name.replace(" ", "-")
