from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class META:
        verbose_plural_name = 'Categories'
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    price = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
