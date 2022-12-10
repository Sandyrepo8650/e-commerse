from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.generic import View
from .forms import UserRegistrationForm

User = get_user_model()


class UserRegisterPageView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)
    
    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('accounts:login')


class UserLoginPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/login.html')

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is None:
            raise ValueError("you don't have any account")
        login(request, user=user)
        return redirect('products:home')


class UserLogoutPageView(View):
    def get(self, request, id, *args, **kwargs):
        user = User.objects.get(id=id)
        context = {'user': user}
        return render(request, 'accounts/logout.html', context)

    def post(self, request, id, *args, **kwargs):
        user = User.objects.get(id=id)
        logout(request)
        return redirect('accounts:login')


class UserProfilePageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'accounts/profile.html', context)