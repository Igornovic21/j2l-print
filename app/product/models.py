from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, default=None, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    ref = models.IntegerField()
    name = models.CharField(max_length=250, default=None, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name