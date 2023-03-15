from django import forms
from.models import *
class Loginform(forms.ModelForm):
    class Meta:
        model=Login
        fields="__all__"
class RegisterForm(forms.ModelForm):
    class Meta:
        model= Register
        fields="__all__"
class BooKForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"
