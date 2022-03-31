import datetime
from django.db import models
from django.forms.widgets import PasswordInput
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, render,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from bookstore.models import Author, Book,Category, Publisher, Subcategory, mainSliderImages,Messages
from bookstore.forms import LoginForm,SignUpForm,AddBook,UpdateBook
from django.http import HttpResponseRedirect
from bookstore.models import Login,User
from django.urls import reverse

class HomeModel(ListView):
    model=Book
    template_name="bookstore/home.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["categories"]=Category.objects.all()
        context["mainslider_images"]=mainSliderImages.objects.all()
        

        return context

def loginView(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            try:
             user=User.objects.get(email=username) 
            #  loginuser=Login.objects.get(username=username,password=password)
             user_id=user.pk
            except (User.DoesNotExist):
                return render(request,'bookstore/login.html',{'form':form,"login_error":"No such user exists",})
                
            else:
              try:
                  loginuser=Login.objects.get(password=password,user=user)
              except (Login.DoesNotExist):
                  return render(request,'bookstore/login.html',{'form':form,"login_error":"Username or Password is Incorrect",})
              else:
                return HttpResponseRedirect(reverse("bookstore:dashboard",args=(user_id,)))
    else:
     form=LoginForm()
    return render(request,'bookstore/login.html',{"form":form,"login_error":"",})

def signup(request):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
           if form.save():
               email=form.cleaned_data["email"]
               return HttpResponseRedirect(reverse("bookstore:setpassword",args=(email,)))
           else:
              return render(request,"bookstore/signup.html",{"form":form,})
        else:
            return render(request,"bookstore/signup.html",{"form":form,})
    else:
        form=SignUpForm()
    return render(request,"bookstore/signup.html",{"form":form})

def setpassword(request,user_email):
    if request.method == "POST" :
        user=User.objects.get(email=user_email)
        user_id=user.pk
        user_name=request.POST["set_username"]
        passwrd=request.POST["set_password"]
        newLogin=Login(username=user_name,password=passwrd,user=user)
        newLogin.save()
        return HttpResponseRedirect(reverse("bookstore:dashboard",args=(user_id,)))
    else:

        return render(request,"bookstore/setpassword.html",{"email":user_email,})

def dashboard(request,user_id):
    user=User.objects.get(pk=user_id)
    addBookForm=AddBook(initial={"user":user,})
    messages=Messages.objects.all()
    try:
        profile_image=user.profile_image.url
        profile_image=True
    except :
        profile_image=False
    return render(request,"bookstore/dashboard.html",{"user":user,"user_id":user_id,"profile_image":profile_image,"messages":messages,"addBookForm":addBookForm,})

class BookDetails(ListView):
    
    template_name="bookstore/details.html"
    
    def get_queryset(self):
         self.selected_book=Book.objects.get(pk=self.kwargs['book_id'])
         try:
             book_pdf=self.selected_book.pdf_file.url
             if book_pdf:
                 self.book_pdf=True
         except:
             self.book_pdf=False

         self.categories=Category.objects.all()
         return Book.objects.filter(category__in=self.selected_book.category.all())

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["selected_book"]=self.selected_book
        context["categories"]=self.categories
        context["book_pdf"]=self.book_pdf

        return context
def addBook(request,user_id):
    u=User.objects.get(pk=user_id)
    if request.method=="POST":
        
        bookForm=AddBook(request.POST,request.FILES)
        if bookForm.is_valid():
            bookForm.save(commit=False)
           
            bookForm.save()
            

            # bookForm.user=u
            # bookForm.save()
            Messages.objects.create(message="Added a new Book ")
            return HttpResponseRedirect(reverse("bookstore:dashboard",args=(user_id,)))
        else:
            bookForm=AddBook(request.POST,request.FILES)
            return HttpResponseRedirect(reverse("bookstore:dashboard",args=(user_id,)))
    else:
        return  render(request,"bookstore/dashboard.html")

def categoryView(request,category_id):
    print("category_id: ",category_id)
    category=Category.objects.get(pk=category_id)
    print("got category")
    books=category.book_set.all()
    print("got bookset")
    mainslider_images=mainSliderImages.objects.all()
    categories=Category.objects.all()
    return render(request,"bookstore/categories.html",{"books":books,"category":category.name,"categories":categories,"mainslider_images":mainslider_images,})

def subcategoryView(request,subcategory_id):
    subcategory=Subcategory.objects.get(pk=subcategory_id)
    print("subcategory name: ",subcategory.name)
    books=subcategory.book_set.all()
    mainslider_images=mainSliderImages.objects.all()
    categories=Category.objects.all()
    return render(request,"bookstore/categories.html",{"books":books,"category":subcategory.name,"categories":categories,"mainslider_images":mainslider_images,})

def deleteBook(request):
    bookId=request.POST.get("book_id")
    userId=request.POST.get("user_id")
    try:
        user=User.objects.get(pk=userId)
        book=Book.objects.get(pk=bookId)
        m=Messages(user=user,message="Successfully Deleted {0} at {1}.".format(book.title,datetime.datetime.now()))
        m.save()
        book.delete()
        
        return JsonResponse({"data":"deleted successfully"})
    except:
        return JsonResponse({"data":"Could not complete requested option"})

def updateBook(request,user_id):
    user=User.objects.get(pk=user_id)
    if request.method=="POST":
        bookId=request.POST.get("book_id")
        bookTitle=request.POST.get("book_title")
        publisherId=request.POST.get("publisher_id")
        authorsIds=request.POST.getlist("authors_id")
        categoryIds=request.POST.getlist("category_id")
        subcategoryIds=request.POST.getlist("subcategory_id")
        publicationDate=request.POST.get("publication_date")
        description=request.POST.get("book_description")
        price=request.POST.get("book_price")
        image=request.FILES.get("book_image")
        pdfFile=request.FILES.get("book_pdffile")
        print("publisher_id: ",publisherId)
        publisher=Publisher.objects.get(pk=publisherId)
        print("categories: ",categoryIds,"subcategories: ",subcategoryIds,
        "authors: ",authorsIds,"bookid:",bookId,"bookImg: ",image,"pdf: ",pdfFile)
        try:
            book=Book.objects.get(pk=bookId)
            book.title=bookTitle
            book.description=description
            book.price=price
            book.image=image
            book.pdf_file=pdfFile
            book.publication_date=publicationDate
            # book.publisher_set.add(publisher)
            # book.save()
            
            print(book)
            # book=Book(user=user,title=bookTitle,description=description,price=price,
            # image=image,pdf_file=pdfFile,publisher=publisherId)
            for aid in authorsIds:
                a=Author.objects.get(aid)
                book.authors.add(a)
            for cid in categoryIds:
                a=Category.objects.get(cid)
                book.category.add(a)
            for scid in subcategoryIds:
                a=Subcategory.objects.get(scid)
                book.subcategory.add(a)
            book.save()
            print("success")
            return HttpResponseRedirect(reverse("bookstore:dashboard",args=(user_id,)))
        except:
            print("fail")
            return HttpResponseRedirect(reverse("bookstore:dashboard",args=(user_id,)))

def getBookImage(request):
    bookId=request.GET.get("book_id")
    try:
        book=Book.objects.get(pk=bookId)
        bookImage=book.image.url
        return JsonResponse({"data":bookImage},safe=False)
    except:
        return JsonResponse({"data":"Book Image not found"},safe=False)

def getCategories(request):
     categories=[[c.name,c.pk] for c in Category.objects.all()]
     return JsonResponse({"data":categories})

def getSubcategories(request):
     subcategories=[[c.name,c.pk] for c in Subcategory.objects.all()]
     return JsonResponse({"data":subcategories})

def getPublishers(request):
    publishers=[[p.name,p.pk] for p in Publisher.objects.all()]
    return JsonResponse({"data":publishers})

def getAuthors(request):
    authors=[[a.first_name +" "+ a.last_name,a.pk] for a in Author.objects.all()]
    return JsonResponse({"data":authors})


            


    


