from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name="login"),
    path('home/',views.home,name="home"),
    path('logindata/',views.logindata,name="logindata"),
    path('addproducts/',views.addproducts,name="addproducts"),
    path('prodata/',views.prodata,name="prodata"),
    path('viewproducts/',views.viewproducts,name="viewproducts"),
    path('editpro/<int:dataid>',views.editpro,name="editpro"),
    path('edit/<int:dataid>',views.edit,name="edit"),
    path('delete/<int:dataid>',views.delete,name="delete"),
    path('',views.shop,name="shop"),
    path('single/<int:dataid>/',views.single,name="single"),
    path('addtocart/',views.addtocart,name="addtocart"),
    path('mycart/',views.mycart,name="mycart"), 
    path('cdelete/<int:dataid>',views.cdelete,name="cdelete"),
     
       
]