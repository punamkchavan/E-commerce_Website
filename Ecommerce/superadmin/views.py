from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Host
from django.contrib.auth.hashers import make_password,check_password
from .models import Product, Order


# hashed_password = make_password('')
# print(hashed_password)

#Admin_Login
def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            admin = Host.objects.get(username=username)

            if check_password(password, admin.password):
                
                request.session['is_logged_in'] = True
                request.session['username'] = username
                return redirect('/admin_dashboard') 
            else:
                messages.error(request, "Invalid username or password")
                return redirect('/admin_login')
        
        except Host.DoesNotExist:
            messages.error(request, "Invalid username or password")
            return redirect('/admin_login')

    return render(request, 'admin_login.html')

@login_required
def admin_dashboard(request):
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    return render(request, 'admin_dashboard.html', {
        'total_products': total_products,
        'total_orders': total_orders,
    })

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})