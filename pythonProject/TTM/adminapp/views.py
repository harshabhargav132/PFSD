from django.db.models import Q
from django.contrib.auth import  logout
from django.contrib import messages

from django.shortcuts import render
from .models import Admin , Register ,Packages


def ttmhome(request):
    return render(request, "ttmhome.html")

def editpackege(request):
    return render(request, "packege.html")

def addpackage(request):
    return render(request, "package.html")

def logoutpage(request):
    return render(request, "logout.html")
def viewplaces(request):
    data = Packages.objects.all()
    return render(request, "viewplaces.html",{"placesdata":data} )

# Create your views here.
from django.db.models import Q

def checkadminlogin(request):
    if request.method == "POST":
        adminuname = request.POST["uname"]
        adminpwd = request.POST["pwd"]
        admin = Register.objects.filter(username=adminuname, password=adminpwd).first()
        if admin is not None:
            return render(request, "ttmhome.html")
        else:
            return render(request, "loginfail.html")




def checkRegister(request):
    if request.method == "POST":
        name = request.POST["name"]
        address = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        username = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=username).exists():
                messages.info(request, "Username exits")
                return render(request, "register.html")
            else:
                user = Register(name=name, address=address, email=email, phno=phno, username=username, password=pwd)
                user.save()
                return render(request, "login.html")


def checkpackage(request):
    if request.method == "POST":
        tourcode = request.POST["tourcode"]
        tourname = request.POST["tourname"]
        tourpackage = request.POST["tourpackage"]
        desc = request.POST["desc"]
        if Packages.objects.filter(tourcode=tourcode).exists():
            messages.info(request, "Tour code exits")
            return render(request, "package.html")
        else:
            package = Packages(tourcode=tourcode, tourname=tourname, tourpackage=tourpackage, desc=desc)
            package.save()
            return render(request, "ttmhome.html")



def changepassword(request):
    return render(request, "changepassword.html")

def checkchangepassword(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        if Register.objects.filter(username=uname, password=opwd).exists():
            Register.objects.filter(username=uname).update(password=npwd)
            return render(request, "ttmhome.html")
        else:
            return render(request, "changepassword.html")
    else:
        return render(request, "changepassword.html")


def logoutthepage(request):
    logout(request)
    return render(request, 'ttmhome.html')
