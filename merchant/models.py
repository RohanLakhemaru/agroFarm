from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from customer.models import *

# Create your models here.

class BaseModel(models.Model):
    uid = models.AutoField(primary_key=True, editable=False, unique=True)
    created = models.DateField(auto_now_add = True)
    modified = models.DateField(auto_now= True)
    class Meta:
        abstract = True


class Address(BaseModel):
    country = models.CharField(max_length=25, default='Unknown')
    state  = models.CharField(max_length=25, default='Unknown')
    district = models.CharField(max_length=25, default='Unknown')
    municipality = models.CharField(max_length=30, default='Unknown')
    zip_code = models.CharField(max_length=25, default='Unknown')
    street = models.CharField(max_length=25, default='Unknown')
    def __str__(self):
        return self.street

class ExtraUserDetails(BaseModel):
    userID = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = PhoneNumberField()
    # addressID = models.OneToOneField(Address,on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.user.username

class User_Address(BaseModel):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    addressID = models.ForeignKey(Address, on_delete=models.CASCADE)
    def __str__(self):
        return self.userID.first_name

class Category(BaseModel):
    title = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.title

class Tag(BaseModel):
    title = models.CharField(max_length=30, default='')
    def __str__(self):
        return self.title

class Product(BaseModel):
    merchantID = models.ForeignKey(User, on_delete=models.CASCADE,default=00)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    tagID = models.ManyToManyField(Tag)
    name = models.CharField(max_length=30,default="unknown")
    featuredimage = models.CharField(max_length=1024, default='') 
    description = models.CharField(max_length=100,default="unknown")
    rate = models.DecimalField(max_digits=5, decimal_places=2,default="unknown")
    is_availble = models.BooleanField(default=False)
    def __str__(self):
        return self.name

# class Product_Tag(BaseModel):
#     tagID = models.ForeignKey(Tag, on_delete=models.CASCADE)
#     produtID = models.ForeignKey(Product, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.title
    
class Review(BaseModel):
    userID = models.ForeignKey(User,on_delete=models.CASCADE)
    productId = models.ForeignKey(Product,on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    comment = models.TextField()
    def __str__(self):
        return self.rating

class Store(BaseModel):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    addressID = models.ForeignKey(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='Unknown')
    pan = models.CharField(max_length=15, default='Unknown')
    def __str__(self):
        return self.name

class Order(BaseModel):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    addressID = models.ForeignKey(Address, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=4, decimal_places=0, default='Unknown')
    rate = models.DecimalField(max_digits=10, decimal_places=2, default='Unknown')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default='Unknown')
    is_pending = models.BooleanField(default='True')
    is_complete = models.BooleanField(default='False')
    is_cancelled = models.BooleanField(default='False')
    is_cashOnDelivery = models.BooleanField(default='True')
    is_online = models.BooleanField(default='False')