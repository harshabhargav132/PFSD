from django.shortcuts import render


def homePage(request):
    return render(request,"index.html")
def contactPage(request):
    return render(request,"contact.html")
def loginPage(request):
    return render(request,"login.html")
def aboutPage(request):
    return render(request,"about.html")
def RegisterPage(request):
    return render(request,"Register.html")
def AdminPage(request):
    return render(request,"Admin.html")


def logout(request):
    return render(request, "logout.html")

def HomePage(request):
    return render(request,"Home.html")
