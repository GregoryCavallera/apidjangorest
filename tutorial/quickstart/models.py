from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)