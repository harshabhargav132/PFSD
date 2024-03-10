from django.shortcuts import render, HttpResponse

def homePage(request):
    return render(request, 'index.html')

def contactPage(request):
    return render(request, 'contact.html')

def loginPage(request):
    return render(request, 'login.html')

def aboutPage(request):
    return render(request, 'about.html')

def signupPage(request):
    return render(request, 'signup.html')