from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('product/<int:pk>', views.ProductPageView.as_view(), name='single_product'),
    path('products', views.AllProductPageView.as_view(), name='all_product'),

]
