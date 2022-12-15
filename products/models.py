from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, null=True, blank=True)
    discount = models.FloatField(default=0)
    image = models.ImageField(upload_to='image/cateogry', null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=220)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

      
class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image/products/', null=True, blank=True)
    price = models.IntegerField()
    digital = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products:single_product", kwargs={"pk": self.pk})



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    trans_id = models.CharField(max_length=50)
    complited = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.user.email


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.title} -> {self.quantity}' 

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=220, null=True, blank=True)
    city = models.CharField(max_length=220, null=True, blank=True)
    state = models.CharField(max_length=220, null=True, blank=True)
    pincode = models.CharField(max_length=220, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer.user.email} from {self.city}'