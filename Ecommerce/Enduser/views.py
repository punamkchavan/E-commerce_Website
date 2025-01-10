from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from superadmin.models import Product
from .models import Cart
# Create your views here.

#home_view
def home_view(request):
    return render(request, 'home.html')

#user_dashboard
def user_dashboard(request):
    return render(request, 'user_dashboard.html')

#Registration_view
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)   
        if form.is_valid():
            user = form.save()  
            login(request, user)   
            messages.success(request, "Registration successful.")
            return redirect('login') 
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserRegistrationForm()  
    return render(request, 'register.html', {'form': form})

# Login_view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_dashboard')   
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout_view
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')
    
def product_list(request):
    products = Product.objects.all()
    return render(request, 'end_user/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    Cart.objects.create(session_id=session_id, product=product, quantity=1)
    return redirect('cart')

def cart_view(request):
    session_id = request.session.session_key
    cart_items = Cart.objects.filter(session_id=session_id)
    return render(request, 'end_user/cart.html', {'cart_items': cart_items})
