from django.urls import path
from . import views
urlpatterns = [
    path('admin_dashboard', views.user_dashboard, name='admin_dashboard'),
    path('admin_login/', views.login_view, name='admin_login'),
    path('logout/', views.logout_view, name='logout'),
]