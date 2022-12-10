from django.shortcuts import render, redirect
from django.http import Http404
from django.views import View
from .models import Product, Category
from .forms import ProductModelForm



class HomePageView(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.all().order_by('-id')[:6]
        category = Category.objects.all()
        context = {
            'products': product,
            'category': category,
        }
        return render(request, 'products/home.html', context)

class ProductPageView(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            raise Http404()
        context = {'product': product}
        return render(request, 'products/single_product.html', context)


class AllProductPageView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by('-id')
        category = Category.objects.all()
        context = {
            'products': products,
            'category': category,
        }
        return render(request, 'products/products.html', context)