from django.contrib import admin
from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderItem
# Register your models here.
  
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    list_editable = ('price', 'stock')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price', 'created_at')
    search_fields = ('customer__first_name', 'customer__last_name', 'id')
    list_filter = ('created_at',)
    inlines = [OrderItemInline]
        

        

