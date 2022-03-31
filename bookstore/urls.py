from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from bookstore.views import HomeModel, categoryView, deleteBook, getAuthors, getBookImage, getCategories, getPublishers, getSubcategories,loginView,dashboard, setpassword, signup,BookDetails,addBook, subcategoryView, updateBook
app_name="bookstore"
urlpatterns=[
   path('',HomeModel.as_view(),name='home'),
   path('login/',loginView,name="login"),
   path('dashboard/<int:user_id>/',dashboard,name="dashboard"),
   path('signup/',signup,name="signup"),
   path('setpassowrd/<str:user_email>/',setpassword,name="setpassword"),
   path('bookdetails/<int:book_id>/',BookDetails.as_view(),name="bookdetails"),
   path("addbook/<int:user_id>/",addBook,name="addbook"),
   path("categories/<int:category_id>/",categoryView,name="categories"),
   path("subcategories/<int:subcategory_id>/",subcategoryView,name="subcategories"),
   path("deletebook/",deleteBook),
   path("updatebook/<int:user_id>/",updateBook,name="updatebook"),
   path("bookimage/",getBookImage),
   path("publishers/",getPublishers),
   path("authors/",getAuthors),
   path("categories/",getCategories),
   path("subcategories/",getSubcategories),
]