
from django.db import models
from django.db.models.base import Model
from django.conf import settings
import datetime



class Author(models.Model):
    SALUTATION_CHOICES=[
        ("Mr","Mr"),
        ("Mrs","Mrs"),
        ("Other","Other"),
    ]
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    salutation=models.CharField(max_length=6,choices=SALUTATION_CHOICES,default="Mr")
    email=models.EmailField(max_length=200,default="youremail@gmail.com")
    profile_photo=models.ImageField(upload_to="author_profiles/")
    website=models.URLField(max_length=200,null=True,blank=True)

    def __str__(self):
      return self.first_name

class Publisher(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=100,null=True,blank=True)
    Country=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to="publisher_profiles/")
    city=models.CharField(max_length=50)
    website=models.URLField(max_length=200,null=True,blank=True)
    def __str__(self):
      return self.name

class Book(models.Model):
    title=models.CharField(max_length=255)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    authors=models.ManyToManyField(Author)
    category=models.ManyToManyField("Category")
    subcategory=models.ManyToManyField("Subcategory")
    reviews=models.PositiveBigIntegerField(default=0)
    image=models.ImageField(upload_to="books_images/")
    pdf_file=models.FileField(upload_to="book_pdfs/",null=True,blank=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=8,decimal_places=2,default=0.00)
    publication_date=models.DateField()
    likes=models.PositiveBigIntegerField(default=0)
    dislikes=models.PositiveBigIntegerField(default=0)
    user=models.ForeignKey("User",on_delete=models.CASCADE,null=True)
    

    def __str__(self):
      return self.title

class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
      return self.name
   

class Subcategory(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
      return self.name

class Messages(models.Model):
  message=models.CharField(max_length=200)
  time=models.DateField(default=datetime.datetime.now())

  
class User(models.Model):
    SALUTATION_CHOICES=[
        ("Mr","Mr"),
        ("Mrs","Mrs"),
        ("Other","Other"),
    ]
    GENDER_CHOICES=[
      ("Male","Male"),
      ("Female","Female"),
      ("Other","Other"),
    ]
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    salutation=models.CharField(max_length=6,choices=SALUTATION_CHOICES,default="Mr")
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES,default="M")
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=100,default="youremail@gmail.com",unique=True)
    profile_image=models.ImageField(upload_to="user_profiles/",default="/media/user_profiles/user.svg")
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    about=models.TextField(blank=True,null=True)
    def __str__(self):
      return self.first_name

class Login(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    user=models.OneToOneField(User,null=False,on_delete=models.CASCADE)

    def __str__(self):
      return self.username

class mainSliderImages(models.Model):
    image=models.ImageField(upload_to="mainsliderimgs/")

class Messages(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date=models.DateTimeField(auto_now=True)
    message=models.TextField()



    


    