from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'deskripsi', 'harga', 'stok']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control'}),
            'stok': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label="Konfirmasi Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']