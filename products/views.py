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
        return render(request, 'products/index.html', context)

class ProductPageView(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            raise Http404()
        context = {'product': product}
        return render(request, 'products/product-detail.html', context)


class AllProductPageView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by('-id')
        category = Category.objects.all()
        count = products.count()
        context = {
            'products': products,
            'category': category,
            'count': count
        }
        return render(request, 'products/store.html', context)


class DashboardPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'products/dashboard.html')

    
class CartPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'products/cart.html')


# class SingleProductPageView(View):
#     def get(self, request, *args, **kwargs):
#         try:
#             product = Product.objects.get(id=pk)
#         except Product.DoesNotExist:
#             raise Http404()
#         context = {'product': product}
#         return render(request, 'products/product-detail.html')


class PlaceOrderPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'products/place-order.html')


class OrderCompletePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'products/order_complete.html')


class SearchResultPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'products/search-result.html')