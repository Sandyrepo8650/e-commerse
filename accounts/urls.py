from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register', views.UserRegisterPageView.as_view(), name='register'),
    path('login', views.UserLoginPageView.as_view(), name='login'),
    path('logout/<int:id>', views.UserLogoutPageView.as_view(), name='logout'),
]