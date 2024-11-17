from django.contrib import admin
from django.contrib.auth.models import User  
from .models import *

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ["user","product","created_at","is_active"]
    

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",]
    list_filter = ["name",]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ["username", "first_name", "last_name", "email", "age"]
    list_display = ["username", "first_name", "last_name", "email", "age"]
    list_filter = ["location"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ["user", "title", "price", "category", "description"]
    list_display = ["user", "title", "price", "category", "description"]
    list_filter = ["title", "price"]
