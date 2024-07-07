from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import User
from .forms import UserLoginForm, UserRegisterForm

# Create your views here.
class LoginView(View):
    template_name = 'login.html'
    form_class = UserLoginForm

    def get(self, request):
      form = self.form_class()
      return render(request, self.template_name, { 'form': form })

    def post(self, request):
      form = self.form_class(request.POST)

      if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
          login(request, user)
          return redirect('events:list')

        return render(request, self.template_name, { 'form': form, 'error': 'Email and/or password is incorrect' })

      return render(request, self.template_name, { 'form': form, 'error': 'Fields are requireds' })


class RegisterView(View):
  template_name = 'register.html'
  form_class = UserRegisterForm

  def get(self, request):
    form = self.form_class()
    return render(request, self.template_name, { 'form': form })

  def post(self, request):
    form = self.form_class(request.POST)

    if form.is_valid():
      name = form.cleaned_data.get('name')
      email = form.cleaned_data.get('email')
      password = form.cleaned_data.get('password')

      user = User.objects.create_user(name=name, email=email, password=password)

      login(request, user)
      return redirect('events:list')

    return render(request, self.template_name, { 'form': form, 'error': 'Fields are requireds' })


def logoutUser(request):
  logout(request)
  return redirect('authentication:login')
