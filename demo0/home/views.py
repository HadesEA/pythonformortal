from django.shortcuts import render

# Create your views here.

import random

def index(request):
    r = random.randint(1, 100)
    context = {
        "mensaje": "un mensaje XD",
        "variable": r
    }
    return render(request,"home/index.html", context)

def about_us(request):
    return render(request, "home/about_us.html",{})

def services(request):
    return render(request, "home/services.html",{})

def projects(request):
    return render(request, "home/projects.html",{})

def solutions(request):
    return render(request, "home/solutions.html",{})

def partners(request):
    return render(request, "home/partners.html",{})

def blog_insights(request):
    return render(request, "home/blog_insights.html",{})

def register(request):
    return render(request, "home/register.html",{})

def login(request):
    return render(request, "home/login.html",{})

def profile(request):
    return render(request, "home/profile.html",{})



