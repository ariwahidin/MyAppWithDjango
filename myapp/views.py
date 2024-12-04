from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from .forms import RegisterForm

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "message": "Invalid credentials"})
    return render(request, "myapp/login.html")

@login_required
def home_view(request):
    return render(request, "myapp/home.html")

@login_required
def product_view(request):
    return render(request, "myapp/product.html")

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product berhasil ditambahkan!")
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'myapp/product_form.html', {'form': form, 'title': 'Tambah Produk'})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product berhasil diupdate!")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'myapp/product_form.html', {'form': form, 'title': 'Edit Produk'})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product berhasil dihapus!")
        return redirect('product_list')
    return render(request, 'myapp/product_confirm_delete.html', {'product': product})

def logout_view(request):
    logout(request)
    return redirect("login")

def register(request):
    last_message = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            last_message = "Registrasi berhasil! Silakan login."
            messages.success(request, last_message)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'myapp/register.html', {'form': form, 'title': 'Register', 'last_message': last_message})
