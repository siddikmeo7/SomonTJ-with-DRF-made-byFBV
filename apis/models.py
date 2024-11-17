from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__ (self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    def __str__ (self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField()
    location = models.ForeignKey(City,on_delete=models.CASCADE)
    region = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__ (self):
        return f"{self.username}-{self.age} years old!"
    
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title  = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='meida/p_photos',null=True,blank=True),
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__ (self):
        return f"{self.title}:{self.created_at}"
    

class Request(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__ (self):
        return f"{self.user}:{self.product}"