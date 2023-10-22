from django.conf import settings
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


# this class  use for category 
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
# this class  use for sub_category 
class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# this class  use for create product
class Product(models.Model):
    Availability = (('In Stock','In Stock'),('Out of Stock','Out of Stock'))
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True,default='')  
    sub_category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE, null=True,default='')  
    image = models.ImageField(upload_to='ecommerce')
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    Availability = models.CharField(choices=Availability,null=True,max_length=100)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name

# # this class  use for Authencation
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={'exists': 'This email already exists'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'Enter username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter Confirm Password'

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']

# this class  use for Contact page
class Contact_us(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField(max_length=100)   
    subject = models.CharField(max_length=100) 
    message = models.CharField(max_length=100) 
    
    
    def __str__(self):
        return self.name        