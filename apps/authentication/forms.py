from django import forms

class UserLoginForm(forms.Form):
  email = forms.EmailField(required=True)
  password = forms.CharField(widget=forms.PasswordInput, required=True)

class UserRegisterForm(forms.Form):
  name = forms.CharField(required=True)
  email = forms.EmailField(required=True)
  password = forms.CharField(widget=forms.PasswordInput, required=True)
