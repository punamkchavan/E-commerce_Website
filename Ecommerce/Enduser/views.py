from django.shortcuts import render
from .models import Shopee
from .forms import ShopeeForm, UserRegistrationForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(req):
    return render(req,'index.html')

def register(req):
    if req.method =='POST':
        form=UserRegistrationForm(req.POST)
        if form.is_valid():
            user=form.save(commot=False)
            user.set_password(form.changed_data['password1'])
            user.save()
            login(req,user)
            return redirect('tweet_list')
    else:
        form=UserRegistrationForm()
        
    return render(req,'registration/register.html',{'form':form})
    
    

    
    
