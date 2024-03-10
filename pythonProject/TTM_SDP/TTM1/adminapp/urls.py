from django.urls import path
from . import views

urlpatterns = [
    path('ttmhome', views.ttmhome, name='ttmhome'),
    path('checkadminlogin', views.checkadminlogin, name='checkadminlogin'),
    path('checkregistration', views.checkregistration, name='checkregistration'),
    path("viewplaces", views.viewplaces, name="viewplaces"),
    path("addpackage", views.addpackage, name="addpackage"),
    path("checkpackage", views.checkpackage, name="checkpackage"),
    path("changepassword", views.changepassword, name="changepassword"),
    path("checkchangepassword", views.checkchangepassword, name="checkchangepassword"),
    path("logoutthepage", views.logoutthepage, name="logoutthepage"),
    path("logoutpage", views.logoutpage, name="logoutpage"),

]