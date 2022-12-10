from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, null=True, blank=True)
    image = models.ImageField(upload_to='image/cateogry', null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
    
    

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image/products/', null=True, blank=True)
    price = models.IntegerField()
    discount_price = models.IntegerField(null=True, blank=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products:single_product", kwargs={"pk": self.pk})
    