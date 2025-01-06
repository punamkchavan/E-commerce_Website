from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Product   
# Create your views here.

def index(req):
    return render(req,'index.html')

#registrtion view
def register(req):
    if req.method == 'POST':
        form = UserRegistrationForm(req.POST)   
        if form.is_valid():
            user = form.save()   
            login(req, user)   
            messages.success(req, "Registration successful.")
            return redirect('login')  
        else:
            messages.error(req, "Unsuccessful registration. Invalid information.")
    else:
        form = UserRegistrationForm()  
    return render(req,'registration/register.html',{'form':form})

# Login view
def login_view(req):
    if req.method == 'POST':
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect('register/')  
            else:
                messages.error(req, "Invalid username or password.")
        else:
            messages.error(req, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(req, 'registration/login.html', {'form': form})
    

# Logout view
@login_required
def logout_view(req):
    logout(req)
    messages.success(req, "You have successfully logged out.")
    return redirect('login')
    
#Product View
def product_view(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'home.html', {'products': products})