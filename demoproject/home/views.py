from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import ProductForm
from .models import Product


# Create your views here.


def home(request):
    products = Product.objects.all()  # retrieve all products from the database
    print(products)  # Print the products to the console
    return render(request, 'home.html', {'products': products})


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return redirect('signin')

    return render(request, 'sign_up.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            lname = user.last_name
            return render(request, 'user_dashboard.html', {'fname': fname, 'lname': lname})
        else:
            messages.error(request, "Invalid credentials")
            return redirect('signin')

    return render(request, 'sign_in.html')


def signout(request):
    logout(request)
    return redirect('home')


def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, 'Successfully Added The Product')
    product_form = ProductForm()
    return render(request, 'add_product.html', {'form': product_form})


def Home(request):
    return redirect('home')


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, 'Successfully Edited')
    product_form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': product_form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'delete_product.html', {'product': product})


def featured_products_view(request):
    featured_products = Product.objects.filter(is_featured=True)
    return render(request, 'featured_products.html', {'featured_products': featured_products})


@login_required(login_url='signin')
def user_dashboard(request):
    fname = request.user.first_name
    lname = request.user.last_name
    return render(request, 'user_dashboard.html', {'fname': fname, 'lname': lname})




