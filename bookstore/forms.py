from django.db import models
from django.db.models.fields import DateField
from django.forms import Form,ModelForm, widgets
from django.forms import fields
from django.forms.fields import CharField
from .models import Book, User
from django.forms import ModelForm

class LoginForm(Form):
    username=CharField(max_length=100)
    password=CharField(max_length=100)
    
class SignUpForm(ModelForm):
    class Meta:
        model=User
        fields="__all__"
class AddBook(ModelForm):
    class Meta:
        model=Book
        fields=("title","publisher","authors","category","subcategory","image","description","price","publication_date","user")

class UpdateBook(ModelForm):
   class Meta:
       model=Book
       fields="__all__"