from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('product/<int:pk>', views.ProductPageView.as_view(), name='detail'),
    path('products', views.AllProductPageView.as_view(), name='all_product'),
    path('dashboard', views.DashboardPageView.as_view(), name='dashboard'),
    path('cart', views.CartPageView.as_view(), name='cart'),
    # path('detail', views.SingleProductPageView.as_view(), name='detail'),
    path('place-order', views.PlaceOrderPageView.as_view(), name='place-order'),
    path('order-complete', views.OrderCompletePageView.as_view(), name='order-complete'),
    path('search-result', views.SearchResultPageView.as_view(), name='search-reault'),

]
