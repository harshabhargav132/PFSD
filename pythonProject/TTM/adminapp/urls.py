from django.urls import path
from .import views
urlpatterns = [
    path("ttmhome", views.ttmhome, name="ttmhome"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("checkRegister",views.checkRegister,name="checkRegister"),
    path("checkPackage", views.checkpackage, name="checkPackage"),
    path('changepassword', views.checkchangepassword,name='changepassword'),
    path('checkchangepassword',views.checkchangepassword,name='checkchangepassword')
]
